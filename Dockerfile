# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install binaries for psycopg2. From https://hub.docker.com/r/tedder42/python3-psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc
# need gcc to compile psycopg2

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

RUN apt-get autoremove -y gcc

# create directory for the app user
RUN mkdir -p /home/app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

ADD . $APP_HOME


#entry point debe hacer collectstatic y ejecutar las migraciones de la db.
ADD initDocker.sh .
RUN ["chmod", "+x", "initDocker.sh"]
ENTRYPOINT ["./initDocker.sh"]

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser $APP_HOME
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "storylink_dev.wsgi"]

