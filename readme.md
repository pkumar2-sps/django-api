## [Django Label API](https://github.com/prakashsharmacs24/django-api)
The "Django Label API" is a reference application created to show how

to develop Django based pdf label API(using Celery, Nginx, Postgresql and Redis) using the recommended best practices.


## Maintained by: [Prakash Kumar](https://github.com/prakashsharmacs24)



## Built With
* [Django](http://www.celeryproject.org/) - The web framework used
* [DRF](http://www.django-rest-framework.org/) - Django REST framework
* [Celery](http://www.celeryproject.org/) -  Distributed Task Queue
* [Gunicorn](http://www.gunicorn.org/) -  Application Server/Python WSGI HTTP Server


* [Nginx](http://www.nginx.com/) - Web Server(used as  reverse proxy)
* [Postgresql](https://postgresql.org/) - Relational Database
* [Redis](https://redis.io/) - NoSql Database(distributed and  in-memory key-value store db)



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
[![Deploy](https://hub.docker.com/public/images/logos/mini-logo.svg)](https://docs.docker.com/compose/django/)
```
Docker version 18.03.1-ce, build 9ee9f40
docker-compose version 1.21.1, build 7641a569,
```


How to use this image
------------

Run Application with a Docker/Docker-Compose
------------
This is the recommended way to run application. You can use the following docker compose template:
```yaml

version: '2'
services:
  nginx:
    image: nginx:latest
    container_name: nginx_container
    ports:
      - "7001:8000"
    volumes:
      - ./web:/src
      - ./config/nginx:/etc/nginx/conf.d
    depends_on:
      - web
  web:
    build: .
    container_name: django_container
    depends_on:
      - db
    volumes:
      - ./web:/src
    expose:
      - "8000"
    links:
      - redis
  db:
    image: postgres:latest
    container_name: postgres_container
  redis:
    image: redis:latest
    container_name: redis_container
    ports:
     - '6379:6379'

```


Execute this command to install the project:

1.  Builds the images define in the docker-compose.yml
```bash
docker-compose build
```

2.  Create your containers


```bash
docker-compose up -d
```
3.  Make  Migration


```bash
docker-compose run web python /src/manage.py makemigrations
docker-compose run web python /src/manage.py migrate
```
3.  Generate Label
We can confirm it works by navigating to http://127.0.0.1:7001/api/v1/reports/?limit=1 where you’ll see the pdf label as before.

3. Close Docker container
When you’re done, don’t forget to close down your Docker container.
```bash
docker-compose down
```


Useful Command
------------
- List Running container:
```bash
docker-compose ps
```
- View container log:
```bash
docker-compose logs -f web
```
- Stop containers:
```bash
docker-compose stop
```
- Remove containers:
```bash
 docker-compose rm -f
```
- Restart specific containers:
```bash
docker-compose restart web
```


# Contributing

We'd love for you to contribute to this container. You can request new features by creating an [issue](https://github.com/prakashsharmacs24/django-api/issues), or submit a [pull request](https://github.com/prakashsharmacs24/django-api/pulls) with your contribution.

# Issues

If you encountered a problem running this container, you can file an [issue](https://github.com/prakashsharmacs24/django-api/issues). For us to provide better support, be sure to include the following information in your issue:

- Host OS and version
- Docker version (`$ docker version`)
- Output of `$ docker info`
- Version of this container (`$ echo $BITNAMI_IMAGE_VERSION` inside the container)
- The command you used to run the container, and any relevant output you saw (masking any sensitive information)

# License

MIT License

Copyright (c) 2018 prakashkumar(<mailto:prakashsharmacs24@gmail.com>)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
