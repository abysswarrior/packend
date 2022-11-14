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

You can see the deployed version of project [here](https://packend.herokuapp.com/)

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

# License

[MIT](https://choosealicense.com/licenses/mit/)