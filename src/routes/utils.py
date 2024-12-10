from functools import wraps
from datetime import timedelta

from sqlalchemy.sql import func
from sqlalchemy import cast, Float
from flask import request, redirect, url_for, wrappers

from routes import db, Connection, Activity, User, Genre, Song


def format_time(seconds: int) -> str:
    return str(timedelta(seconds=seconds))


def get_user() -> User | None:
    addr = request.remote_addr

    if not addr:
        return None
    
    connection = Connection.query.filter_by(ip_address=addr).first()

    if connection:
        return connection.user

    return None


def get_user_id() -> int | None:
    addr = request.remote_addr

    if not addr:
        return None
    
    connection = Connection.query.filter_by(ip_address=addr).first()

    if connection:
        return connection.user_id

    return None


def get_user_number_listens(user_id: int) -> int:
    return (
        db.session.query(func.count(Activity.song_id.distinct()))
        .filter(Activity.user_id == user_id, Activity.elapsed > 0)
        .scalar() or 0
    )


def get_user_percentage_sum(user_id: int) -> int:
    return (
        db.session.query(
            func.sum(Activity.elapsed)
        )
        .select_from(Activity)
        .filter(Activity.user_id == user_id, Activity.elapsed > 0)
        .scalar() or 0
    )


def get_user_listening_time(user_id: int) -> int:
    return (
        db.session.query(
            func.sum(cast(Activity.elapsed, Float) / 100 * cast(Song.length, Float))
        )
        .select_from(Activity)  # Explicitly set Activity as the starting point
        .join(Song, Activity.song_id == Song.id)  # Explicit join with ON clause
        .filter(Activity.user_id == user_id, Activity.elapsed > 0)  # Filtering condition
        .scalar() or 0  # Get the result or default to 0
    )


def get_favorite_genre(user_id: int) -> Genre | None:
    favorite_genre = (
        db.session.query(Genre, db.func.count(Activity.id).label("activity_count"))
        .join(Song, Song.genre_id == Genre.id)  # Join Genre -> Song
        .join(Activity, Activity.song_id == Song.id)  # Join Song -> Activity
        .filter(Activity.user_id == user_id)  # Filter by the current user
        .group_by(Genre.id)  # Group by genre
        .order_by(db.func.count(Activity.id).desc())  # Order by activity count descending
        .first()  # Get the top result
    )

    return favorite_genre[0] if favorite_genre else None


def requiere_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = get_user_id()  # Get the current user ID
        if user_id is None:
            return redirect(url_for("signin"))  # Redirect to login if not authenticated
        return func(*args, **kwargs)
    return wrapper
