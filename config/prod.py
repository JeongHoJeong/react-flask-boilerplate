from config import BaseConfig


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'postgresql://example:example@db:5432/example'
