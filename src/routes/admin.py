from datetime import date

from flask import request, flash, redirect, url_for

from routes import app, db, Song, Artist, Genre, Album, Contract, User, Activity


@app.route("/add_genre", methods=["POST"])
def add_genre():
    name = request.form["name"]

    genre = Genre(name=name)
    db.session.add(genre)
    db.session.commit()

    flash("Genre added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_album", methods=["POST"])
def add_album():
    title = request.form["title"]
    artist_id = request.form["artist_id"]

    album = Album(title=title, artist_id=artist_id)
    db.session.add(album)
    db.session.commit()

    flash("Album added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_artist", methods=["POST"])
def add_artist():
    name = request.form["name"]

    artist = Artist(name=name)
    db.session.add(artist)
    db.session.commit()

    flash("Artist added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_song", methods=["POST"])
def add_song():
    title = request.form["title"]
    length = request.form["length"]

    creation: str = request.form["creation"]  # 2024-11-05
    year, month, day = creation.split("-")
    creation = date(int(year), int(month), int(day))

    genre_id = request.form["genre_id"]
    album_id = request.form["album_id"]

    # print(type(title), title)
    # print(type(length), length)
    # print(type(creation), creation)
    # print(type(genre_id), genre_id)
    # print(type(album_id), album_id)

    song = Song(
        title=title, 
        length=length, 
        creation=creation, 
        genre_id=genre_id, 
        album_id=album_id
    )
    db.session.add(song)
    db.session.commit()

    flash("Song added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_contract", methods=["POST"])
def add_contract():
    start = str(request.form["start"])
    year, month, day = start.split("-")
    start = date(int(year), int(month), int(day))

    end = str(request.form["end"])
    year, month, day = end.split("-")
    end = date(int(year), int(month), int(day))

    capacity = request.form["capacity"]

    contract = Contract(
        start_date=start,
        end_date=end,
        capacity=capacity
    )
    db.session.add(contract)
    db.session.commit()

    flash("Contract added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    last_name = request.form["last_name"]

    birth_date = request.form["birth_date"]
    year, month, day = birth_date.split("-")
    birth_date = date(int(year), int(month), int(day))

    contract_id = request.form["contract_id"]

    user = User(
        name=name,
        last_name=last_name,
        birth_date=birth_date,
        contract_id=contract_id
    )
    db.session.add(user)
    db.session.commit()

    flash("User added successfully!", "success")
    return redirect(url_for("admin"))


@app.route("/add_activity", methods=["POST"])
def add_activity():
    user_id = request.form["user_id"]
    song_id = request.form["song_id"]

    elapsed = request.form["elapsed"]

    start_date = request.form["start_date"]
    year, month, day = start_date.split("-")
    start_date = date(int(year), int(month), int(day))

    activity = Activity(
        user_id=user_id,
        song_id=song_id,
        elapsed=elapsed,
        start_date=start_date
    )
    db.session.add(activity)
    db.session.commit()

    flash("Activity added successfully!", "success")
    return redirect(url_for("admin"))
