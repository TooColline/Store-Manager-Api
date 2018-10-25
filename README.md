# Store-Manager-Api
[![Build Status](https://travis-ci.com/TooColline/Store-Manager-Api.svg?branch=develop)](https://travis-ci.com/TooColline/Store-Manager-Api) [![Coverage Status](https://coveralls.io/repos/github/TooColline/Store-Manager-Api/badge.svg?branch=develop)](https://coveralls.io/github/TooColline/Store-Manager-Api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/d0ed3191e7c3ea7198c6/maintainability)](https://codeclimate.com/github/TooColline/Store-Manager-Api/maintainability)

## Project Overview
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. This repository contains the API Endpoints for the web application.

### Endpoints

#### Auth Endpoints
Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/signup` | Create a new user
POST | `/api/v1/auth/login` | Login a registered user

#### Admin Endpoints
Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/products` | Add a new product
GET | `/api/v1/products` | Get all products
GET | `/api/v1/products/<int:product_id>` | Get specific product
GET | `/api/v1/saleorder` | Get all sale orders
GET | `/api/v1/saleorder/<int:sale_id>` | Get specific sale order

#### Store Attendant Endpoints
Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/products` | Get all products
GET | `/api/v1/products/<int:product_id>` | Get specific product
POST | `/api/v1/saleorder` | Add sale order

### Installing the application
1. Open your terminal and `https://github.com/TooColline/Store-Manager-Api.git`
2. Navigate to the app folder `cd Store-Manager-Api`
3. Create a virtual environment `virtualenv venv` and activate it `source venv/bin/activate` 
4. Install dependencies of the application using `pip3 install -r requirements.txt`
5. Export these environment variables ```export FLASK_APP="run.py"``` for your app and ```export JWT_SECRET_KEY=yourkey```
6. Run the application using `python3 run.py` or `flask run`

### Tests
Run this command inside your virtual environment: `coverage run --source=app.api.v1.views -m pytest /tests/v1 -v -W error::UserWarning && coverage report`

#### Technologies used
1. Python flask framework
2. `pytest` for running tests
3. `flask JWT` for auth
4. `pylint` for python linting library

## Credits
This challenge was part of the Bootcamp 33 NBO Andela.

## Author
Too Collins

## Documentation
https://documenter.getpostman.com/view/5601454/RWgxuujo

## Deployment
[Heroku](https://store-manager-app-api-heroku.herokuapp.com/api/v1/products)
