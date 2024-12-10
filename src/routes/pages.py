from flask import request, render_template, redirect, url_for

from routes import app, db, Genre, Album, Artist, Song, Contract, User, Activity, Connection
from routes.utils import get_favorite_genre, get_user, get_user_id, require_login, get_user_number_listens, get_user_listening_time, format_time, get_user_percentage_sum


@app.route("/about")
@require_login
def about():
    num_genres = Genre.query.count()
    num_songs = Song.query.count()

    profile = get_user()

    return render_template(
        "about.liquid",
        num_genres = num_genres,
        num_songs = num_songs,

        profile=profile
    )


@app.route("/admin")
@require_login
def admin():
    genres = Genre.query.all()
    albums = Album.query.all()
    artists = Artist.query.all()
    songs = Song.query.all()

    users = User.query.all()
    contracts = Contract.query.all()
    activities = Activity.query.all()

    profile = get_user()
    
    return render_template(
        "admin.liquid",
        genres=genres,
        albums=albums,
        artists=artists,
        songs=songs,

        users=users,
        contracts=contracts,
        activities=activities,

        profile=profile
    )


@app.route("/contract", methods=["GET"])
@require_login
def contract():
    day_str = request.args.get("day") or "Not Set"  # e.g., "2023-12-10"
    st_str = request.args.get("st") or "off"  # e.g., "on"

    profile = get_user()

    return render_template(
        "contract.liquid",
        day_str=day_str,
        st_str=st_str,

        profile=profile
    )


@app.route("/")
@require_login
def index():
    genres = Genre.query.all()
    albums = Album.query.all()
    artists = Artist.query.all()
    songs = Song.query.all()

    users = User.query.all()
    contracts = Contract.query.all()

    profile = get_user()
    
    return render_template(
        "index.liquid",
        genres=genres,
        albums=albums,
        artists=artists,
        songs=songs,

        users=users,
        contracts=contracts,

        profile=profile
    )


@app.route("/profile")
@require_login
def profile():
    profile = get_user()

    listened_titles = get_user_number_listens(profile.id)
    listening_time = get_user_listening_time(profile.id)

    if listened_titles != 0:
        percentage = get_user_percentage_sum(profile.id) / listened_titles
    else:
        percentage = 0.0

    favorite_genre = get_favorite_genre(profile.id)
    print(favorite_genre)

    return render_template(
        "profile.liquid",
        listened_titles=listened_titles,
        listening_time=format_time(listening_time),
        percentage=percentage,
        favorite_genre=favorite_genre,

        profile=profile
    )


@app.route("/signin")
def signin():
    profile = User(name="Not connected")
    return render_template(
        "signin.liquid",

        profile=profile
    )


@app.route("/signup")
def signup():
    contracts = Contract.query.all()
    profile = User(name="Not connected")

    return render_template(
        "signup.liquid",
        contracts=contracts,

        profile=profile
    )

@app.route("/login", methods=["POST"])
def login():
    user = get_user_id()
    if user is not None:
        return redirect(url_for("index"))

    name = request.form["name"]
    last_name = request.form["last-name"]
    birth = request.form["birth"]

    user = User.query.filter_by(name=name, last_name=last_name, birth_date=birth).first()

    if user:
        ip = request.remote_addr
        connection = Connection(ip_address=ip, user_id=user.id)
        db.session.add(connection)
        db.session.commit()

        return redirect(url_for("index"))
    else:
        return "User not found. Please register.", 400

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    last_name = request.form["last-name"]
    birth = request.form["birth"]
    contract = request.form["contract"]

    existing_user = User.query.filter_by(name=name, last_name=last_name, birth_date=birth).first()
    if existing_user:
        return "User already exists. Please log in.", 400

    new_user = User(name=name, last_name=last_name, birth_date=birth, contract_id=contract)
    db.session.add(new_user)
    db.session.commit()

    ip = request.remote_addr
    connection = Connection(ip_address=ip, user_id=new_user.id)
    db.session.add(connection)
    db.session.commit()

    return redirect(url_for("index"))
