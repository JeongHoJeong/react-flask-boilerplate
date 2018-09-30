from flask import Blueprint, jsonify, request

from app.db import DBSession
from app.models.example_todo import ExampleTodo


bp = Blueprint('example', __name__, url_prefix='/example')


@bp.route('/todos/', methods=['GET'])
def todos():
    with DBSession() as session:
        todos = session.query(ExampleTodo).order_by(ExampleTodo.id).all()

        return jsonify([
            {
                'id': todo.id,
                'description': todo.description,
            }
            for todo in todos
        ])


@bp.route('/todo/', methods=['POST'])
def create_todo():
    r = request.json
    description = r.get('description', None)

    if description is None:
        return '`description` is missing.', 400

    with DBSession() as session:
        todo = ExampleTodo(description=description)
        session.add(todo)

    return '', 200


@bp.route('/todo/<int:id_>/', methods=['PATCH'])
def update_todo(id_):
    r = request.json
    description = r.get('description', None)

    if id_ is None:
        return '`id` is missing.', 400
    elif description is None:
        return '`description` is missing.', 400

    with DBSession() as session:
        todo = session.query(ExampleTodo).filter_by(id=id_).first()
        if todo is None:
            return f'Invalid ID `{id_}`.', 404
        todo.description = description

    return '', 200


@bp.route('/todo/<int:id_>/', methods=['DELETE'])
def delete_todo(id_):
    with DBSession() as session:
        session.query(ExampleTodo).filter_by(id=id_).delete()
    return '', 200
