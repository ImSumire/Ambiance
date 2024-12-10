CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS artist (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
    id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE IF NOT EXISTS song (
    id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    length INTEGER,
    creation DATE,
    genre_id INTEGER NOT NULL,
    album_id INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(id),
    FOREIGN KEY (album_id) REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS contract (
    id INTEGER PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    capacity INTEGER
);

CREATE TABLE IF NOT EXISTS "user" (  -- user is a sql reserved word, it’s quoted to avoid conflicts
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    birth_date DATE,
    contract_id INTEGER NOT NULL,
    FOREIGN KEY (contract_id) REFERENCES contract(id)
);

CREATE TABLE IF NOT EXISTS activity (
    id INTEGER PRIMARY KEY,
    start_date DATE,
    elapsed INTEGER,
    user_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (song_id) REFERENCES song(id)
);

-- CREATE TABLE IF NOT EXISTS connection (
--     id INTEGER PRIMARY KEY,
--     ip_address VARCHAR NOT NULL,
--     user_id INTEGER NOT NULL,
--     created_at DATE NOT NULL,
--     expires_at DATE NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES "user"(id)
-- );
