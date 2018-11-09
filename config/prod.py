from config import BaseConfig
from os import environ


class ProductionConfig(BaseConfig):
    DATABASE_URI = f'\
postgresql://{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}@\
{environ.get("DB_HOST", "127.0.0.1")}:{environ.get("DB_PORT", 5432)}/postgres'
