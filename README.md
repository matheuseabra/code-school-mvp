# CodingApp

<!-- [![Build Status](https://travis-ci.org/matheuseabra/docker-flask-react.svg?branch=master)](https://travis-ci.org/matheuseabra/docker-flask-react) -->

A educational coding app built using Flask, React and Docker using the micro-services architecture.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker

### Install

Launch services by running:

```
docker-compose up

```

## Running the tests

```
docker-compose exec users python manage.py test

```

## Built With

* [Flask](https://flask.palletsprojects.com) - The web framework used
* [React](https://reactjs.org/) - UI library to build the frontend
* [Docker](https://www.docker.com/) - Used to containerize the app
* [Ngnix](https://www.nginx.com/) - Reverse Proxy used to foward incoming requests

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
