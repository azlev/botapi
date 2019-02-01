This project uses python3 with Django in a default docker-compose environment

https://docs.docker.com/compose/django/

# Running

To run you need docker and docker-compose in your environment

```
docker-compose build
docker-compose up -d
docker-compose exec botapi ./manage.py migrate
```

The botapi will run in http://localhost:8000

# Implementation

To do this assigment, I choose:

* Application layer: python3 + Django + Django REST
* Database: PostgreSQL
* Development Environment: docker-compose

## Application Layer

* python3 is my language "du jour", so it was natural to me
* Django 2.1: the easier way to implement routing and model logic
* Django REST framework: REST has a lot of tiny details, so it's better to use a framework


## Database

PostgreSQL is a very advanced relational database that I'm used to.

## Development Environment

docker-compose nowaday is the best way to port a project from one env to another

# Scaling

Scale the application is not very complex, since there is no state session in this API. We can use Load Balancers using a round robin algorithm.

The "bots" resource is not big and I don't expect more than 10000 different bots. So It's not hard to create one master and N hot standbys to scale reads.

The "messages" resource is the main bottleneck. We can split those rows to multiple databases using some shard technique, using some function like getconnection(conversationId) -> connection.

There are some custom PostgreSQL extensions that help to split the live data.

# Fault Tolerance

In application layer, a smart load balancer can route to just healthy applications.

In database layer, native master/standby replication can do the job, with some orchestration software like [Patroni](https://github.com/zalando/patroni) can do the job.

# Rational

One thing that I spend some time was modeling the messages model in a way that I can mantain some relation integrity. But the bot ID could be in one of "from" and "to". To solve this, I created in the model internal fields called "bot", "direction" and "client". So, before save, I find if the bot is the "from" or "to", save the information inside "direction". The opposite process takes place when we retrieve data from database.

This implementation took more time than I expected, but I still think that the effort was not wasted.

One problem arose in the "from" field. "from" is a reserved word in python, and it took a lot of time to workaround it.


# Technical Debts

It's expected that only OLTP data will live in this env. Any deleted resource can be archived in another place using triggers in the database

Tests must be improved a lot.

To comply with LGPD (Lei Geral de Proteção aos Dados), it's a good idea to put a reverse proxy on top of this application or the frontend.

