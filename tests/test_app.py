from app import hello


def test_app():
    assert hello() == 'hello'
