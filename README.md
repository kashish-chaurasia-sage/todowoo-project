Todo Woo - Django 3.0
==========================================================
Life is fun. But life is also busy. There's a million different things you could be doing. But what matters is what you do. I created Todo Woo to help you make sense of all of your opportunities and live that life that matters most to you. Your new organized life awaits.

A website where a user can sign up for an account, and fully manage a todo list with the ability to create, edit, and delete. Built using Django,bootsrap 4, python,sql,javascript, html/css, SCSS, github actions, and many other useful technologies.

Features
--------
* Supports multiple user accounts.
* Add, delete, update or mark complete your daily tasks.
* Prioritize to tasks.
* Simple and straight forward digital way to track you daily tasks and prioritize it.

Learnt while building up this project
--------------------------------------------------
How to:

- Work with the authentication system (sign up, login, logout)
- Create virtual environments
- Establish model relationships
- Require login for certain pages
- Create a CRUD application (Create, Read, Update, Delete)
- Queries and filters
- Handling Errors


Getting Started
---------------
Install dependencies:

```bash
$ virtualenv MRS
$ source MRS/bin/activate
$ pip3 install -r requirements.txt
```

Clone the repository:

```bash
$ git clone https://gitlab.com/kashish10/todowoo-project.git
```

Go inside the folder :

```bash
$ cd todowoo-project
```

Create super-user for your DB admin :

```bash
$ python manage.py createsuperuser
```

Make DB migrations :

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

Run server :

```bash
$ python manage.py runserver
```

Go-to Localhost : [localhost](http://127.0.0.1:8000/)

You can see that the todowoo project is up, you can now modify the contents accordingly. All the static file or images are in static folder.

Contributing
------------
Contributions are actively encouraged. Please review the code. If you find a bug, or any improvement please [email me](kashish.chaurasia10@gmail.com), submit a pull request or submit an issue.


