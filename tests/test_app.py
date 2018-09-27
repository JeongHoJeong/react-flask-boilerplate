"""Test for Flask application logic.
Basic idea from: https://github.com/miguelgrinberg/flasky/blob/master/tests/test_api.py  # noqa: E501
"""

import json
import pytest

from app import create_app
from app.db import db
from app.models import metadata


@pytest.fixture(scope='class')
def client(request):
    app = create_app('config.test.TestConfig')
    request.cls.app_context = app.app_context()
    request.cls.client = app.test_client()

    with app.app_context():
        metadata.drop_all(bind=db.engine)
        metadata.create_all(bind=db.engine)

    yield

    with app.app_context():
        metadata.drop_all(bind=db.engine)


@pytest.mark.usefixtures('client')
class TestExample:
    def test_404(self):
        response = self.client.get('/wrong/url')
        assert response.status_code == 404

    def test_initial_state(self):
        response = self.client.get('/example/todos/')
        todos = response.json

        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert len(todos) == 0

    def test_todo_story(self):
        # Create a todo.
        response = self.client.post(
            '/example/todo/',
            data=json.dumps({
                'description': 'Do laundry',
            }),
            content_type='application/json',
        )

        assert response.status_code == 200

        # Now there's one todo.
        response = self.client.get('/example/todos/')
        todos = response.json

        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert len(todos) == 1

        todo = todos[0]

        assert todo['description'] == 'Do laundry'

        # Update a todo.
        response = self.client.patch(
            '/example/todo/{}/'.format(todo['id']),
            data=json.dumps({
                'description': 'Do homework',
            }),
            content_type='application/json',
        )

        assert response.status_code == 200

        # Delete a todo.
        response = self.client.delete('/example/todo/{}/'.format(todo['id']))
        assert response.status_code == 200

        # Now there's 0 todos.
        response = self.client.get('/example/todos/')
        todos = response.json

        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert len(todos) == 0

    def test_updating_non_existing_todo(self):
        response = self.client.patch(
            '/example/todo/{}/'.format(123456),
            data=json.dumps({
                'description': 'Do homework',
            }),
            content_type='application/json',
        )

        assert response.status_code == 404
