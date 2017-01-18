import flask
import flask_sqlalchemy

application = flask.Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"] = "mysql+cymysql://root:@127.0.0.1/metadata"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database = flask_sqlalchemy.SQLAlchemy(application)
