from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:19982804@localhost:3306/stepanproject_db'
db = SQLAlchemy(app)
db.init_app(app)


class Departments(db.Model):
    departmentID = db.Column(db.Integer, primary_key=True)
    departmentNAME = db.Column(db.String(200), nullable=False)
    managerID = db.Column(db.Integer, nullable=False)
    locationID = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<departments {self.id}>"


class Employees(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column (db.String(200), nullable=False)
    phone_number = db.Column (db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    departmentID = db.Column(db.Integer, db.ForeignKey('departmentID'))

    def __repr__(self):
        return f"<employees {self.id}>"

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/create-departments', methods=['POST', 'GET'])
def create_departments():
    if request.method == "POST":
        departmentNAME = request.form['departmentNAME']
        managerID = request.form['managerID']
        locationID = request.form['locationID']

        department = Departments(departmentNAME=departmentNAME, managerID=managerID, locationID=locationID)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/')
        except:
            return "При заповненні виникла помилка"

    else:
        return render_template("create-departments.html")



if __name__ == "__main__":
    app.run(debug=True)