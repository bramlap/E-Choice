## Setup of E-Choice game

1. Install all the modules in requirements.txt

2. Create a database and database user
In terminal run:

	sudo su - postgres

	psql

	CREATE DATABASE e_choice;

	CREATE USER e_choice_projectuser WITH PASSWORD '123qweasdzxc';

	ALTER ROLE e_choice_projectuser SET client_encoding TO 'utf8';

	ALTER ROLE e_choice_projectuser SET default_transaction_isolation TO 'read committed';

	ALTER ROLE e_choice_projectuser SET timezone TO 'UTC';

	GRANT ALL PRIVILEGES ON DATABASE e_choice TO e_choice_projectuser;

	\q

	exit (to exit terminal)

3. Create superuser 
In terminal:

	Go to E-Choice/E_Choice directory

	ls (to check is manage.py is present)

	python3 manage.py makemigrations

	python3 manage.py migrate

	python3 manage.py createsuperuser

		username: 	bramlap
		email:		bramlap@gmail.com
		password:	123qweasdzxc
		password(again):123qweasdzxc
	
4. Fill database (make sure django-extensions is installed)
In terminal:

	Go to E-Choice/E_Choice directory

	python3 manage.py runscript users

	python3 manage.py runscript modules

	python3 manage.py runscript vragen

5. Check
In terminal:

	python3 manage.py runserver

In browser, go to:

	http://127.0.0.1:8000/login

Login with:

	username:	bramlap
	password:	123qweasdzxc

DONE!


	
