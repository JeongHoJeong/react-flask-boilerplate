import os
import subprocess

from flask import Flask, send_file


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_PATH = os.path.join(CURRENT_DIR, '../build')


def create_app(config_object=None):
    app = Flask(
        __name__,
        static_url_path='/static',
        static_folder=BUILD_PATH,
    )

    from .example import bp
    app.register_blueprint(bp)

    env = os.environ
    if config_object:
        app.config.from_object(config_object)
    elif 'APP_CONFIG_OBJECT' in env:
        cfg_object = env['APP_CONFIG_OBJECT']
        app.config.from_object(cfg_object)
    else:
        print(
            'Warning: Configuration object is not set!\n' +
            'Set `APP_CONFIG_OBJECT` or run `create_app` with `config_object`.'
        )
        app.config.from_object('config.BaseConfig')

    @app.route('/', methods=['GET'])
    def index():
        return send_file(os.path.join(BUILD_PATH, 'index.html'))

    @app.shell_context_processor
    def make_shell_context():
        return dict(app=app)

    @app.cli.command()
    def test_command():
        subprocess.run(['pytest'])

    @app.cli.command('reset-db')
    def reset_db_command():
        from app.db import reset_db
        reset_db()

    return app
