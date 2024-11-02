from flask import request, flash, redirect, url_for

from __main__ import app, db, Song, Artist, Genre, Album


@app.route("/add_genre", methods=["POST"])
def add_genre():
    name = request.form["name"]

    genre = Genre(name=name)
    db.session.add(genre)
    db.session.commit()

    flash("Genre added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/add_album", methods=["POST"])
def add_album():
    title = request.form["title"]
    artist_id = request.form["artist_id"]

    album = Album(title=title, artist_id=artist_id)
    db.session.add(album)
    db.session.commit()

    flash("Album added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/add_artist", methods=["POST"])
def add_artist():
    name = request.form["name"]

    artist = Artist(name=name)
    db.session.add(artist)
    db.session.commit()

    flash("Artist added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/add_song", methods=["POST"])
def add_song():
    title = request.form["title"]
    length = request.form["length"]
    creation = request.form["creation"]  # 2024-11-05
    genre_id = request.form["genre_id"]
    album_id = request.form["album_id"]

    print(type(title), title)
    print(type(length), length)
    print(type(creation), creation)
    print(type(genre_id), genre_id)
    print(type(album_id), album_id)

    # song = Song(
    #     title=title, 
    #     length=length, 
    #     creation=creation, 
    #     genre_id=genre_id, 
    #     album_id=album_id
    # )
    # db.session.add(song)
    # db.session.commit()

    # flash("Song added successfully!", "success")
    flash("Debug", "success")
    return redirect(url_for("index"))
