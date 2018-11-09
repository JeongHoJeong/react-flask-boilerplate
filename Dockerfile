FROM python:3.7.1

EXPOSE 5000

# Install Node, yarn
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 1.9.4

WORKDIR /app
COPY . .
COPY ./prod.env .env

# Install dependencies & build assets
RUN pip install pipenv
RUN pipenv install
RUN /root/.yarn/bin/yarn install
RUN /root/.yarn/bin/yarn webpack

CMD pipenv run flask reset-db && \
  pipenv run gunicorn --bind 0.0.0.0:5000 "app:create_app('config.prod.ProductionConfig')"
