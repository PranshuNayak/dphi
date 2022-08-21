# Set up
* Make sure you are in the root directory `dphi` which contains other folders like `account` or `course`
* Create a virtual environment: ` python -m virtualenv .venv`
* Activate the virtual environment: `Scripts/activate`
* Install the dependencies: `pip install -r requirements.txt`
* Make migrations: `python manage.py makemigrations`
* Migrate the DB: `python manage.py migrate` and `python manage.py migrate --run-syncdb`
* Load the initial data
    1. `python manage.py loaddata user_data`
    2. `python manage.py loaddata course_data`
    3. `python manage.py loaddata course_registration`
* Run the server `python manage.py runserver`

# Admin Panel
* Username `admin` password `1234`

# Login for already present users
* Usernames = pranshunayak, john, viratkohli , Password = ilovedjango

# Authorisation
You need sent jwt token for accessing protected routes
For creating new users
* `auth/users` for sigup
* `auth/jwt/create` for login (save the refresh and access token as they will be used to access protected endpoints)
* `auth/jwt/refresh` for refreshing token
