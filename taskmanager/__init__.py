import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import env if it's there (local use, not on github)
if os.path.exists("env.py"):
    import env


# create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
# create an instance of the SQLAlchemy class and set to the instance of the Flask app
db = SQLAlchemy(app)

# this need app and db to be imported
from taskmanager import routes