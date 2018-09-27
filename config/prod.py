from config import BaseConfig


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'postgresql://example:example@localhost/example'
