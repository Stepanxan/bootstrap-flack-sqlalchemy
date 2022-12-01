from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:19982804@localhost:3306/stepanproject_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


with app.app_context():
     db.create_all()

with app.app_context():
    from routes.main import *
    from routes.departments import *
    from routes.employees import *


if __name__ == "__main__":
    app.run(debug=True)