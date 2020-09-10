# Storylink.club - ![Storylink.logo](https://raw.githubusercontent.com/Martinnqn/storylink_dev/master/static/imgs/ostorylink.png "Storylink")

| Build Github Action | Coverage backend Codecov |
| ------------- | ------------- |
| ![CI master](https://github.com/Martinnqn/storylink_dev/workflows/CI/badge.svg?branch=master)  | [![codecov](https://codecov.io/gh/Martinnqn/storylink_dev/branch/master/graph/badge.svg)](https://codecov.io/gh/Martinnqn/storylink_dev)  |

---

Storylink.club is a platform for write stories in the style of **Choose Your Own Adventure**.

A user can write a story (aka *__storylink__*) and allow others to continue the plot.

---
## Table of contents
- [General info](#general-info)
- [Technologies](#technologies)
- [Environments](#environment)
- [Backend](#backend)
    -[How to run Backend](#How-to-Run-backend-for-develop)
- [Frontend](#frontend)


## General info
Storylink is a platform of interactive stories creation in collaboration.

It is collaborative because a user (writer) can create content (Stories - *__a node__*) and allow others to continue the plot (linking nodes - *__edges__*). This way, different branches are created from one node, forming a tree of stories, like figure:

![Storylink.logo](https://raw.githubusercontent.com/Martinnqn/storylink_dev/master/static/imgs/ejemplo.png "Storylink Tree")

It is interactive because the user (reader) can advance through the branches answering questions or reading subtitles of the Stories.

---

This repository is a personal project when I can improve my skills, and implement technologies.

Feel free to copy and paste, open issues, fork, etc.

The images in the imgs folder are a personal creation, ask me before using them please.

--- 

## Technologies
Project is created with:
* Django 3.0.7 (python 3.7)
* Postgresql version: 11
* Nginx
* Docker, Docker-compose
* Frontend is currently migrating from Templates, Bootstrap 4 and CSS to React 16.13.1 (With hooks and functional components) and Semantic-UI (see react branch).
* Celery and RabbitMQ
* Social Login: Facebook and Twitter.
* Github Actions

## Environments

There are three Dockerfiles and dockers compose, each one for differents environments: production, automatic testing (current only backend -still no tests implemented-) and develop. For develop environment, the app reload automatically with detect changes on code, using Gunicorn server.

For testing, the docker compose is prepared for CI and local test. for CI see docker-test-ci.yml inside .github/workflow/

For local test just build up docker-compose.test.yml, this will run ```python manage.py test``` and show result in console. 

Configuration environment variables are required for each environment. These variables are inside dot files like .env.template. Since these files contain sensitive information, I provide a template file (.env.template) in each appropriate directory for you to fill out. Currently, in the development environment, the database configuration works with the username and password provided in .env.template, for a more agile configuration.

In development environment, the **Data Base** is created with a user admin for Django app. The **username** is *admin* and **password** *admin*.

## Backend
Backend is built inside Docker containers.
There are four containers:
* Postgresql
* Django app with Gunicorn
* Nginx
* Celery and RabbitMQ


### How to Run backend for develop
Backend run in port **8000**, **only** visible for docker network.
It is split in two Dockerfiles: 
* docker-compose.dev.yml: launch the Postgresql, Django (Gunicorn with --reload flag) and Nginx containers.
* docker-compose.async-services.yml: launch Celery and Rabbitmq for asynchronous services (email are send asynchronously).

For running backend for develop use docker-compose with docker-compose.dev.yml file:

```sh
$ docker-compose -f "docker-compose.dev.yml" up 
```

optionally can launch asynchronous services with

```sh
$ docker-compose -f "docker-compose.async-services.yml" up 
```

WARNING: asynchronous services are in async_mail branch, not in master.

WARNING: asynchronous services depends on storylinkdev image, therefor required launch docker-compose.dev first.

WARNING: RabbitMQ requires a username, password, and virtualhost, but these requirements are not currently met.

## Frontend
Frontend is currently built in Django templates, javascript and bootstrap 4. Slowly it is migrating to React and Semantic UI. See the branch react_webp_redux.

### How to Run frontend for develop
The old frontend running in server side because is integrated with Django. So running docker-compose.dev.yml is sufficient for see interface in **localhost:1337** 

The new interface is out of the container, so only run 
```sh
$ yarn start 
```
and open **localhost:3000** (make sure you are on the react_webp_redux branch)
