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
* [Things I Learned](#things-i-learned)

## Overview

## Dependencies
* Python v3.8
* pyenv

## Installation
## Getting Started
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
https://www.youtube.com/watch?v=0sOvCWFmrtA