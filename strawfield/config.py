import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings:
    #your app secret keys 
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    # Database settings
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_USER")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    
    
    
settings = Settings