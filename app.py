from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DB_STRING = 'mysql://root:root@127.0.0.1:3306/sqlalc'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import User
