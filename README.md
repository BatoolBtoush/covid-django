# Covid19 Statistics

## Features

- Home Page:
    - Has cards that show the world total statistics.
    - A search feature where you'd be able to type in the country's name, start and end dates and get this specific country's covid19 statistic.
- All Countries Page:
    - Has cards that show covid19 statistics about all the countries
    - "Add To My Records" button on each card, to add the country's data to Django's database on the admin dashboard.
- My Records Page:
    - Displays "No Available Records!" if Django's database is empty, aka: when we haven't clicked on the "Add To My Records" button earlier
    - Displays cards with statistics about the countries in Django's database.
    - Each country's card has a "Delete" button, to delete this said database entry

## Fullfiled Requirements:

- Python, django for the backend and Template langauge for the frontend
- Docker for containerization 
- PostgreSQL database

## Running the Project:

```
$ git clone the_url_to_this_repo
$ cd inside "covid-django" poetry project
$ run >> poetry install
$ activiate the powershell by running >> poetry shell
$ make sure you have Docker installed on your machine, and open it
$ run >> docker-compose build
$ run >> docker-compose up
$ run >>> docker-compose up -d, as to not keep interuppting the server and shutting it down constantly
$ instead of shutting down the server and losing the data, with >> $ docker-compose down
	instead run >>> docker-compose stop
		        >>> docker-compose start
```