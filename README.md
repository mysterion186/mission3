# Mission 3 - Section 7
This a project is a mission from the [section 7](https://www.section7.dev/projects/mission3).   
The aim is to create a Flashcard application. I'll use the template I created [Django Boilerplate](https://github.com/mysterion186/django-boilerplate).  
I'll this project as an example of how you can reuse this template as your own.
You'll be able to find a thread on my work [here](https://x.com/kowsik186/status/1728719396829384817?s=20). 

## Installation
### Basic installation
For installing this project you can run the following command:

Install python module:
```pip3 install -r requirements.txt``` (run this command in a virtual env if you have one)  
Install node modules:
```cd frontend && npm install```

### Docker
You can now use Docker to run this project. 
The command to use is the following:   
```docker-compose up --build```.  
The first time running the project, you'll have to make migrations with the following commands:  
```docker-compose exec api sh```  
Then:  
```python3 manage.py makemigrations && python3 manage.py migrate```

## Features
There are some of the current features:
-  Basic Custom User (check the *MyUser* model in `accounts/models`)
    - account creation
    - login
    - update password
    - generate a one time link for resetting password (the email will be prompted on the terminal).
    - reset password (click the link on the email)  

- Social User
    - Google
- Unit testing  
- Docker  
- PostgreSQL  


## Usage

To run the project as is, follow these steps: 
-  rename the `.env.sample` into a `.env` file (with the correct values for your project).
-  run the following commands
    -  ```python3 manage.py runserver```
    -  ```npm run dev```
