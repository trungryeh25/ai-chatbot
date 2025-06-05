# Installation
## Using docker-compose
### Pre-requisites
Before proceeding, make sure you have the latest version of docker and docker-compose installed.

We recommend a version equal to or higher than the following.

```
$ docker --version
Docker version 28.1.1, build 4eba377
$ docker compose version
Docker Compose version v2.36.0-desktop.1
```

### Steps to deploy
Get the service up and running.
```
docker-compose up -d
```
or
```
docker-compose up -d -build
```
To access the admin panel, open http://8080/ in your favorite browser.