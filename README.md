# RPG-forum-CMS
A python driven tool to help manage and generate, manage and balance content for roleplaying forums.

Project progress is being tracked on trello: https://trello.com/b/IYiTGI7F/python-rpg-cms-for-forums

# How to generate docs
Run genDoc.sh on a linux machine. Windows right now deos not have an easy to use file and will have to inspect genDoc.sh to see what settings need to be used for what commands.

# How to setup everything
1) Create a virtual env
2) Active virtual env
3) pull code from github
4) pip install -r requirements.txt
5) Create a config.ini in the /config folder (copy paste the example will work, we recommend tweaking the settting to your enviroment though but it can run with just the defaults)
6) "export FLASK_APP=core/main.py" while in the top level directory of the application
7) flask db init
8) flask db migrate -m "DB Init"
9) flask db upgrade
10) flask run

Now it should run wihtout trouble

# Links and references
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
https://danidee10.github.io/2016/11/20/flask-by-example-8.html
https://flask-admin.readthedocs.io/en/latest/
https://pythonhosted.org/Flask-Security/index.html
https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
https://pusher.com/tutorials/chat-flask-vue-part-1
https://danidee10.github.io/2016/12/12/flask-by-example-10.html
