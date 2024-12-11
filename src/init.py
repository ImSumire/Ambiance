from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import requests
from keys import LASTFM_API_KEY


LASTFM_API_URL = "http://ws.audioscrobbler.com/2.0/"


app = Flask("Spotifi")

app.secret_key = b"50e95ff5e87fd328665cf763900bb5a9"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spotifi.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import Genre, Album, Artist, Song


def parse_date(date_str):
    """Convert a published date string to SQL date format."""
    try:
        parsed_date = datetime.strptime(date_str, "%d %b %Y, %H:%M").date()
        return parsed_date
    except (ValueError, TypeError):
        return "Unknown"


def fetch_track_info(artist, track_title):
    """Fetch detailed track info including album, genre, and release date."""
    params = {
        "method": "track.getInfo",
        "artist": artist,
        "track": track_title,
        "api_key": LASTFM_API_KEY,
        "format": "json",
    }

    try:
        response = requests.get(LASTFM_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(
            f"Error fetching track info for {track_title} by {artist}: {response.status_code}"
        )
        return None


def fetch_top_tracks(artist, limit=50):
    """Fetch top tracks for an artist."""
    params = {
        "method": "artist.gettoptracks",
        "artist": artist,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": limit,
    }

    try:
        response = requests.get(LASTFM_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching tracks for artist {artist}: {response.status_code}")
        return None


def scrape_music_data(artists, output_file, track_limit=20000):
    """Main function to scrape music data"""
    genres = {}  # name -> Genre object
    albums = {}  # title -> Album object
    artists_map = {}  # name -> Artist object

    count = 0

    for artist in artists:
        artist_obj = artists_map.get(artist) or Artist(name=artist)
        if artist not in artists_map:
            db.session.add(artist_obj)
            artists_map[artist] = artist_obj

        top_tracks = fetch_top_tracks(artist, limit=50)
        if (
            not top_tracks
            or "toptracks" not in top_tracks
            or "track" not in top_tracks["toptracks"]
        ):
            continue

        for track in top_tracks["toptracks"]["track"]:
            title = track.get("name")
            artist_name = track.get("artist", {}).get("name", "Unknown")

            track_info = fetch_track_info(artist_name, title)
            if not track_info or "track" not in track_info:
                continue

            track_details = track_info["track"]
            album_title = track_details.get("album", {}).get("title", "Unknown")
            duration = (
                int(track_details.get("duration", 0)) // 1000
            )  # Convert ms to seconds
            date = track_details.get("wiki", {}).get("published", "Unknown")
            genre_list = track_details.get("toptags", {}).get("tag", [])
            genre_name = genre_list[0]["name"].title() if genre_list else "Unknown"

            if duration != 0 and album_title != "Unknown" and date != "Unknown":
                parsed_date = parse_date(date)

                genre_obj = genres.get(genre_name) or Genre(name=genre_name)
                if genre_name not in genres:
                    db.session.add(genre_obj)
                    genres[genre_name] = genre_obj

                album_obj = albums.get(album_title) or Album(
                    title=album_title, artist=artist_obj
                )
                if album_title not in albums:
                    db.session.add(album_obj)
                    albums[album_title] = album_obj

                song_obj = Song(
                    title=title,
                    length=duration,
                    creation=parsed_date,
                    genre=genre_obj,
                    album=album_obj,
                )
                db.session.add(song_obj)

                count += 1
                if count >= track_limit:
                    break

        if count >= track_limit:
            break

    db.session.commit()
    print(f"Scraping completed. Added {count} tracks to the database.")


if __name__ == "__main__":
    # List of popular artists to scrape from
    artists = [
        "The Beatles",
        "Taylor Swift",
        "Drake",
        "Adele",
        "Eminem",
        "BTS",
        "Ed Sheeran",
        "Coldplay",
        "Lady Gaga",
        "Kanye West",
    ]

    with app.app_context():
        scrape_music_data(artists, output_file="scrapping/data.json", track_limit=100)
