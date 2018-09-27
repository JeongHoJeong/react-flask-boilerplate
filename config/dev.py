from config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DATABASE_URI = 'postgresql://example:example@localhost/example'
