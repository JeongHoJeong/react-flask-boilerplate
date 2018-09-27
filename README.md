# React + Flask boilerplate

## how to run
### setup
```bash
pipenv --python 3.6.1
pipenv install --dev
pipenv shell
```

Create `.env` file to provide environment variables.

```bash
APP_CONFIG_OBJECT=config.dev.DevelopmentConfig
FLASK_ENV=development
```

### run
```bash
# development
flask run

# production
gunicorn --bind 0.0.0.0:5000 "app:create_app('config.prod.ProductionConfig')"
```
