from flask import redirect, request, render_template

from model.models import Departments
from app import app, db


@app.route('/selectdepartments')
def select_departments():
    departments = Departments.query.order_by(Departments.date.desc()).all()
    return render_template("select-departments.html", departments=departments)


@app.route('/selectdepartments/<int:department_id>')
def select_detail(department_id):
    department = Departments.query.get(department_id)
    return render_template("select_detail.html", department=department)


@app.route('/create-departments', methods=['POST', 'GET'])
def create_departments():
    if request.method == "POST":
        department_name = request.form['department_name']
        manager_id = request.form['manager_id']
        location_id = request.form['location_id']

        department = Departments(department_name=department_name, manager_id=manager_id, location_id=location_id)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("create-departments.html")


@app.route('/selectdepartments/<int:department_id>/deletedepartments')
def select_delete_department(department_id):
    department = Departments.query.get_or_404(department_id)

    try:
        db.session.delete(department)
        db.session.commit()
        return redirect('/selectdepartments')
    except:
        return "При видаленні даних сталась помилка"


@app.route('/selectdepartments/<int:department_id>/updatedepartments', methods=['POST', 'GET'])
def update_departments(department_id):
    department = Departments.query.get(department_id)
    if request.method == "POST":
        department.department_name = request.form['department_name']
        department.manager_id = request.form['manager_id']
        department.location_id = request.form['location_id']

        try:
            db.session.commit()
            return redirect('/selectdepartments')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("update-departments.html", department=department)
