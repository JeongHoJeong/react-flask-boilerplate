from config import BaseConfig


class TestConfig(BaseConfig):
    TESTING = True
    DATABASE_URI = 'postgresql://example:example@localhost/test'
