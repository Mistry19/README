from flask import Flask
from flask_migrate import Migrate
from models import db, User

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://my_database_1np3_user:q0cJBD10HS2c6Vs8BYJ1Z2ERKMdqplBv@dpg-d15vd97diees73ei8bn0-a.oregon-postgres.render.com/user_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
migrate =Migrate(app,db)

@app.route('/')
def home():
    return "API running"

