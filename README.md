# Assignment

 Knowledge of Docker and how to build a microservice is required to complete these exercises. When completing tasks make sure to test work before submitting, it should work for us too. Part 1 requires some knowledge of Python but feel free to implement the rest in any other language.


## Exercises

### Part 1: Dockerize it

You're working with a development team that's completely new to Docker. They hand you a Python service ([Flask](http://flask.pocoo.org/)) called Hello `app/hello.py` and need you to help them Dockerize it. They have an incomplete `docker-compose.yml` file. The app will use `nginx` as a reverse proxy to access internal endpoints that should not be accessible from outside of Docker. The internal endpoints run on port `8080` but `nginx` will run on port `80`.

Tasks
1. Create a Dockerfile for Hello `app/hello.py`, it should run command `python -m flask run` on port `8080`.
2. Modify `docker-compose.yml` and `nginx/default.conf` so that `nginx` proxies requests  on port `80`.
3. Run `docker-compose up` and verify that the service is working as it should.

When complete you should be able to do the following:
```bash
$ curl localhost/
{'msg':'Hello, World!'}
$ curl localhost/baz
{'msg':'Hello, Baz!'}
```

### Part 2: Collect some metrics

Luckily the development team implemented a simple health check endpoint at `/health`. This returns the latency of the past request (random floating point number) and if the latency exceeds a certain threshold it marks the service unhealthy.

Metrics response example:
```bash
$ curl localhost/health
{'healthy':true,'latency':0.7978267010781679}
```

Create a sidecar container that will gather insights and perform health checks against the metrics endpoint of the Hello service. This service should be defined in the `docker-compose.yml` file. All logging should print to `stdout`. The sidecar should do the following:

1. Poll `/health` on Hello every minute (10 seconds)
2. Print the best, worst and average request latency of the past minute (60 seconds).
3. Print an alert message if `/health` returns a non 200 HTTP code or `healthy` is `False`.

### Part 3: Deploying 'Hello'

The development team is happy with the changes made to the project and now need to deploy it to production. Describe different ways this service could be deployed. How could it be deployed without any downtime?
