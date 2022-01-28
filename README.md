## EPAM Final project 'Python Autumn 2021'

This is a simple educational project (from Epam training center) 
on python3 that allows you to collect weather data and get weather 
statistics for a selected city.


##### Used tools and technologies
- Python 3
- Django 4
- SQLite
- Docker

##### Data
- Input data: start data, finish data, city

- Output data: min, max, average temp, 
precipitation info (most frequent, procent of days), 
wind speed and direction


#### How to run
###### Docker
1. Download and install Docker 
2. Download project
3. Run commands in terminal:

       docker-compose build
       docker-compose up 
    
4. Go to http://localhost:8000/


###### As usual on localhost
1. To run app run in command line:

       python manage.py runserver
    
2. Go to http://localhost:8000/


##### The database contains data from 01.01.2010 to 29.01.2022