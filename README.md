# Store-Manager-Api
[![Build Status](https://travis-ci.com/TooColline/Store-Manager-Api.svg?branch=develop)](https://travis-ci.com/TooColline/Store-Manager-Api) [![Coverage Status](https://coveralls.io/repos/github/TooColline/Store-Manager-Api/badge.svg?branch=develop)](https://coveralls.io/github/TooColline/Store-Manager-Api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/d0ed3191e7c3ea7198c6/maintainability)](https://codeclimate.com/github/TooColline/Store-Manager-Api/maintainability)

## Project Overview
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. This repository contains the API Endpoints for the web application.

### Endpoints


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

## Credits
This challenge was part of the Bootcamp 33 NBO Andela.

## Author
Too Collins

## Documentation
https://documenter.getpostman.com/view/5601454/RWgwQam2

## Deployment
[Heroku](https://store-manager-app-api-heroku.herokuapp.com/api/v1/products)
