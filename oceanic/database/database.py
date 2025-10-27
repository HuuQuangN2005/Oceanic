import sys
from oceanic import app
from flask_sqlalchemy import SQLAlchemy
from oceanic.config import settings
from sqlalchemy import text
from colorama import Fore

def connect_db():
    try:
        db_url = f"mysql+pymysql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}?charset=utf8mb4"
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        db =  SQLAlchemy(app)
        
        with app.app_context():
            db.session.execute(text("SELECT 1"))

        print(Fore.GREEN + "[INFO] Database connection successful.")
        return db
        
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to connect to database: {e}")
        sys.exit(1)


db = connect_db()