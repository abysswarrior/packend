<p align="center">
  <img src="icon.png"><br/>

  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
  <img src="https://img.shields.io/badge/python-%3E=3.9-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/os-linux-blue?logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/web-Django-green?logo=django&logoColor=white"><br/>
  <img src= "https://img.shields.io/badge/deployment-heroku-purple?logo=heroku&logoColor=white">
  <img src="https://badges.frapsoft.com/os/v3/open-source.svg?v=103"><br/>
</p>

# About Packend
**Packend** is a free and open-source Website that gather latest python backend jobs in the Netherlands, made by the _Django_ framework.

# Live Demo

You can see the deployed version of project [here](http://packend.promethe.dev/) or [here](http://packend-promethe.fandogh.cloud/)

# Features

- [x] Based on **Django 4**
- [x] gather jobs with relocation package from **relocate.me**
- [x] gather job positions from **expatica.com**
- [ ] gather job positions from **tepstone.nl**
- [ ] **Search** mechanism for all resource
- [ ] Automatically send new job position to **email**
- [ ] A brief **History of the Netherlands**
- [ ] Useful **tips** & and **tricks** for expat
- [ ] Tips & Tricks about **health insurance**
- [ ] Introducing the most important website to find **jobs** in Netherlands
- [ ] information about the **best neighborhood** in the Netherlands for expat
- [ ] Introducing the best website fo **find home**
- [ ] List of **companies** that has permitted to offer **relocation package**
    
# Requirements

```markdown
- python version > 3.9
- django version 4
```

# Run Locally

**Step 1 :** create a new virtualenv and install requirements.
```shell
$ pip install -r requirements.txt
```

**Notice :** if you get psycopg2 `pg_config` error use this command
```shell
$ sudo apt-get install libpq-dev
```

**Step 2 :** run django and reach whole project in [http://localhost:8000/](http://localhost:8000/).
```shell
$ python manage.py runserver
```

# Deploy on Fandogh

[fandogh.cloud](https://www.fandogh.cloud/) is a fantastic PaaS that allows you to 
deploy project easily. You just need to make your project dockerized.

To deploy project follow these commands :

**Step 1 :** initiate the image
```shell
$ fandogh image init --name=packend
```

**Step 2 :** publish the image to fandogh registry
```shell
$ fandogh image publish --version v0.1 
```

**Step 3 :** deploy the image. Done!
```shell
$ fandogh service deploy --version v0.1 --name packend -p 8000 --hosts packend.promethe.dev
```

> To use `--host` option you should first verify your domain in fangogh  

# Why ?

I created this website, to gather everything that needs to know about The Netherlands.
if you are a backend developer (*especially in python stack*) and you decided to immigrate to the Netherlands I hope that would help.

# Contribution

Contributions are very welcome. I appreciate any PR or feedbacks to improve Packend.

# License

Made by ❤️ under [MIT](https://choosealicense.com/licenses/mit/) license.