```
   ___       __  __               ___   ___  ____  ___               __                         __    ______     __           _      __
  / _ \__ __/ /_/ /  ___  ___    / _ | / _ \/  _/ / _ \___ _  _____ / /__  ___  __ _  ___ ___  / /_  /_  __/_ __/ /____  ____(_)__ _/ /
 / ___/ // / __/ _ \/ _ \/ _ \  / __ |/ ___// /  / // / -_) |/ / -_) / _ \/ _ \/  ' \/ -_) _ \/ __/   / / / // / __/ _ \/ __/ / _ `/ / 
/_/   \_, /\__/_//_/\___/_//_/ /_/ |_/_/  /___/ /____/\__/|___/\__/_/\___/ .__/_/_/_/\__/_//_/\__/   /_/  \_,_/\__/\___/_/ /_/\_,_/_/  
     /___/                                                              /_/                                                            
```
## Table Of Contents
* [Overview](#overview)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Getting Started](#getting-started)
    * [Database](#database)
        * [Start PostgreSQL](#start-postgresql)
        * [Connect with PGAdmin](#connect-with-pgadmin)
        * [Migrations](#migrations)
    * [Service](#service)
        * [via Python](#via-python)
        * [via Docker](#via-docker)
* [Deployment](#deployment)
    * [Environments](#environments)
* [Testing](#testing)
* [Things I Learned](#things-i-learned)

## Overview
FastAPI is a "modern", "fast" web framework for building application programming interfaces with Python 3.6 and above. 
It uses Pydantic to validate, serialize/deserialize data and automatically generate Open AI documentation. 

This is a project that is based off of [Free Code Camp's Python API](https://www.youtube.com/watch?v=0sOvCWFmrtA) development course. At the end of this course I was able to learn how to develop the following concepts:
* Database
* Authentication/Authorization
* Integration Testing
* CI/CD
* Jobs/Workers
* Containerization
* Deployment to Cloud Environments

## Dependencies
* [Python v3.8]()
* pyenv
* [PostgreSQL]()
* [Docker]()
* Nginx
* pip3

## Installation
1. Verify that you have the correction Python version 3.8 run `python --version`
2. Install application dependencies by running `pip3 install -r requirements.txt`

## Getting Started
1. Create a `.env` file at the root of the directory.
2. Copy the contents of `.env.template` into the newly created `.env` file.

### Database
Before the API can start it will need to connect to PostgreSQL. Here are the set of instructions to start PostgreSQL locally.

#### Start PostgreSQL
1. Install PostgreSQL.
2. Start Postgres by running `pg_ctl -D /usr/local/var/postgres start`
3. Run `psql postgres` to verify access to PostgreSQL

#### Connect with PGAdmin
A way to tinker with the database, run queries and view the data, use PostgreSQL GUI called [PGAdmin](https://www.pgadmin.org/download/).
1. Download [pgAdmin](https://www.pgadmin.org/download/) based on machine's operating system.
2. Open the application.
3. Create passwords for accessing pgAdmin. 
> **Note**
> These are not passwords for the actual API database. Please write it down for it will be prompted for entry if the application restarts.
4. Right click on the
 
#### Migrations

### Service
#### via Python
#### via Docker

## Deployment
## Environments
## Testing
## Things I Learned
 
## Testing
uvicorn app.main:app --reload
## Things I Learned

* JWT token
* hashing
* postgres with sql alchemy
* Defining schemas
* Setting up environment variables with Fast Service
* Alembic db migration tool. alembic init to setup the db tool to the project. alembic revision is what keep tracks of the changes to the database
* To run alembic command or migrations `alembic upgrade VERSION_NUMBER` or alembic upgrade head or alembic upgrade 1'
* pip freeze > requirements.txt is a way to get a copy of cuurrrent project dependencies

```
1

If you want to do this without dropping your migration files the steps are:

Drop all the tables in the db that are to be recreated.
Truncate the alembic_version table (so it will start from the beginning) - this is where the most recent version is kept.
The you can run:

alembic upgrade head
and everything will be recreated. I ran into this problem when my migrations got in a weird state during development and I wanted to reset alembic. This worked.
```
* `heroku ps:restart` to restart the instance when updating the server
* `git push heroku main` to update branch in heroku
* `heroku apps:info NAME_OF_APP` to view information
* never run `alembic revision` on production server.....NEVER just run `alembic upgrade head`
* To run alembic on the python server run `heroku run alembic upgrade head`
* to view all the users that is available in an ubuntu server run `cat /etx/passwd`
* Restart app in Ubuntu run `systemctl restart postgresql`
* to give roto access to a user run `usermod -aG sudo USER_NAME`
* to start application on prod server `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000`
* created a service file `gunicorn.servce` that get stored at `/etc/systemd/system` in prod its called `api.service`
    * to start the service `systemctl start api` 
    * to restart the service `systemctl restart api` <=== use this to manually restart the service in the server
    * to check statsu `systemctl status api`
* Nginx to manage requests to the four works that run gunicorn which runs the app
    * to start on ubuntu `systemctl start nginx`
    * update default.conf at `/etc/nginx/sites-available`
* Register domain name to ubuntu server https://docs.digitalocean.com/tutorials/dns-registrars/.
    * created A record
* Create a SSL cert and configure it with certbot.https://certbot.eff.org/instructions
* Use built firewall UFW.  
    * Creates a set of rules to determine which ports or Ip addresses are allowed. `sudo ufw allow hhtp`
    * `sudo ufw enable` to start the firewall
* docker-compose 
    * to have docker reflect the changes that was in the app as you make changes and development use `bind mounts`
        ```
        volumes:
            - ./:/usr/src/app
            # path of the files you want to be watched : path of where the files are being stored in the docker container
        ```
      * When having multiple docker-compose files use the -f flag to specifiy which one to start from `docker-compose -f docker-compose-dev.yml up`
* Docker Hub
    * docker login
    * docker push name_of_image => must follow naming convention of user_acount/name_of_image
    * to rename docker image `docker image tag NAME_OF_ORIGINAL_IMAGE NAME_OF_NEW_IMAGE`
* Testing
    * `pytest --disable-warnings` to remove warnings in test
    * `pytest -x` stops test suite when a test fails
    * conftest.pyIs a file that python use for all test to have access to the fixtures. conftest is package specific
    * `pytest  tests/test_user.py -v -s`
    * `@pytest.mark.parametrize` decorator defined at the beginning of test gives you the otpion to pass in multiple parameters for the test to asset upon.
https://www.youtube.com/watch?v=0sOvCWFmrtA