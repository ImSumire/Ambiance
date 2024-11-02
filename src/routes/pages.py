from flask import render_template

from __main__ import app, Genre, Album, Artist, Song


@app.route("/")
def index():
    genres = Genre.query.all()
    albums = Album.query.all()
    artists = Artist.query.all()
    songs = Song.query.all()
    
    return render_template(
        "index.liquid",
        genres=genres,
        albums=albums,
        artists=artists,
        songs=songs,
    )
