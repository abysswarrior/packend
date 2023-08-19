<p align="center">
  <img src="icon.png"><br/>

  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"><br/>
  <img src="https://badges.frapsoft.com/os/v3/open-source.svg?v=103"><br/>
</p>

# About Packend
**Packend** is a free and open-source Website that gather latest python backend jobs in the Netherlands, made by the _Django_ framework.

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
- [ ] **Dockerize** project
- [ ] Store crawled data in **database**
- [ ] Automate jobs crawling by **celery beat**
    
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

# Screenshots

### Home Page

![home](screenshot/home.png)

### Relocate.me

![relocateme](screenshot/relocateme.png)

### Expatica

![expatica](screenshot/expatica.png)

# Why ?

I created this website, to gather everything that needs to know about The Netherlands.
if you are a backend developer (*especially in python stack*) and you decided to immigrate to the Netherlands I hope that would help.

# Contribution

Contributions are very welcome. I appreciate any PR or feedbacks to improve Packend.

# License

Made by ❤️ under [MIT](https://choosealicense.com/licenses/mit/) license.