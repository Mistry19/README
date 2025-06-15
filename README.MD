# THIS IS THE MAIN TITLE

 ## Project overview
 what your project is about, features of your project
 and importance of project.
    1.
    2.
    3.

## Routes
Explain different end points

## Prerequisties
before installing dependancies activate virtual environment. run this command
```
cd server
python3 -m venv venv
source venv/bin/activate

```

To install backend dependancies run this code
```
pip install -r requirement.txt
```

To install frontend dependancies this code , run this command
```
cd client
npm install
```

## Set up database
run
```
flask db init
flask db migrate -m "Message"
flask db upgrade
```

Seed your database
```
python3 seed.py
```

## How to run app
to start the server run the following in the server directory
```
python3 app.py
```
to start the client run
```
npm start
```