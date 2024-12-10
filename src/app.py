# Librairies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("Spotifi")

app.secret_key = b"50e95ff5e87fd328665cf763900bb5a9"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spotifi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modules
from routes import *


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
