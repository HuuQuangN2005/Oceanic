from oceanic import app
from oceanic.url import *
from oceanic.database import db

if __name__ == "__main__":
    with app.app_context():

        app.run(debug=True)