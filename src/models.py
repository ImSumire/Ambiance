# Librairies
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Date, Time

# Modules
from __main__ import db


date = float
time = float


# Songs database
class Genre(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # Foreign links
    songs: Mapped[list['Song']] = relationship("Song", back_populates="genre")


class Album(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"), nullable=False)

    # Foreign links
    artist: Mapped['Artist'] = relationship("Artist", back_populates="albums")
    song: Mapped[list['Song']] = relationship("Song", back_populates="album")


class Artist(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # Foreign links
    albums: Mapped[list[Album]] = relationship("Album", back_populates="artist")


class Song(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    length: Mapped[time] = mapped_column(Time)
    creation: Mapped[date] = mapped_column(Date)

    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), nullable=False)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"), nullable=False)

    # Foreign links
    genre: Mapped[Genre] = relationship("Genre", back_populates="songs")
    album: Mapped[Album] = relationship("Album", back_populates="song")


# User back-end
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    birth_date: Mapped[date] = mapped_column()
    
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"), nullable=False)
    
    # Foreign links
    contract: Mapped['Contract'] = relationship("Contract", back_populates="users")
    activities: Mapped[list['Activity']] = relationship("Activity", back_populates="user")


class Contract(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    capacity: Mapped[int] = mapped_column()

    # Foreign links
    users: Mapped[list[User]] = relationship("User", back_populates="contract")


class Activity(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_date: Mapped[date] = mapped_column(Date)
    elapsed: Mapped[int] = mapped_column()  # Percentage
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    song_id: Mapped[int] = mapped_column(ForeignKey("song.id"), nullable=False)

    # Foreign links
    user: Mapped[User] = relationship("User", back_populates="activities")
    song: Mapped[Song] = relationship("Song")


""" # Old

class Artist(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    songs: Mapped[list['Song']] = relationship("Song", back_populates="artist")


class Song(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"), nullable=False)
    artist: Mapped['Artist'] = relationship("Artist", back_populates="songs")
 """