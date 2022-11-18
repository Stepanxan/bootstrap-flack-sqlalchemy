from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///blog.db'
db = SQLAlchemy(app)


class Departments(db.Model):
    departmentID = db.Column(db.Integer, primary_key=True)
    departmentNAME = db.Column(db.String(200), nullable=False)
    managerID = db.Column(db.Integer, nullable=False)
    locationID = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Departments %r>' % self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)