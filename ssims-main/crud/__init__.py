from flask import Flask
from flaskext.mysql import MySQL

application = Flask(__name__)

my_sql = MySQL()
application.config["SECRET_KEY"] = "weh"
application.config["SECRET_KEY"] = "secret_key"
application.config["MYSQL_DATABASE_HOST"] = "localhost"
application.config["MYSQL_DATABASE_USER"] = "root"
application.config["MYSQL_DATABASE_PASSWORD"] = "root0305"
application.config["MYSQL_DATABASE_DB"] = "flask"

my_sql.init_app(application)

from crud import routes
