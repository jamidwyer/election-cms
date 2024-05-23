# election cms

Goal: Election data API.

Current status: empty state, event, and candidate REST endpoints. Probably will get a job before this goes anywhere useful. Please feel free to run with this code/idea yourself!

## Requirements
Python 3
Docker
AWS cli

## Setup
`git clone`
`cd elections`

## Develop (no Docker)

```
python3 -m venv venv
. venv/bin/activatepython3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install --upgrade pip
python3 manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Develop (Docker)

```
docker build -t elections .
docker run -p 8000:8000 elections
```

Visit: http://0.0.0.0:8000/

## Deploy

- change tag in dockerrun.aws.json
- docker build -t elections .
- docker tag elections:latest <your dockerhub username>/elections:<new tag>
- docker push <your dockerhub username>/elections:<new tag>
- eb deploy

## Demo

Feel free to check it out here: http://elections-dev.us-west-2.elasticbeanstalk.com/. The data's sqlite, so it's gonna get wiped a lot until I decide how to persist it. 

## Roadmap

### MVP
- github
- make something that uses the api to see what fields i need to add/change
- handle data correctly. shouldn't be sqlite on whatever server it's on.
- contributor verification

### Important
- smaller geographic areas than states
- automate deploy
- think about ways it will be misused by people with deep pockets; prevent those
- better docs

### Maybe
- eks instead of eb?

## Thanks

This blog post: https://dev.to/ki3ani/deploying-your-first-dockerized-django-rest-api-on-aws-elastic-beanstalk-a-comprehensive-guide-2m77

