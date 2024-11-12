from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import db, Employees, Payroll, Attendance, Performance, Recruitment, Applicants, Training, EmployeeTraining, Compliance, Projects, ProjectAssignment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ray:123456@localhost/hrmspayroll'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

#add employee
@app.route('/employee/add', methods=['GET', 'POST'])
def add_employee():
	if request.method == 'POST':
		name = request.form['name']
		department = request.form['department']
		position = request.form['position']
		#newemployee route
		new_employee = Employees(name=name, department=department, position=position)
		db.session.add(new_employee)
		db.session.commit()
		return redirect(url_for('get_employees'))
	return render_template('add_employee.html')

#edit existing employee
@app.route('/employee/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
	employee = Employees.query.get_or_404(id)
	if request.method == 'POST':
		employee.name = request.form['name']
		employee.department = request.form['department']
		employee.position = request.form['position']
		db.session.commit()
		return redirect(url_for('get_employees'))
	return render_template('edit_employee.html', employee=employee)

#delete an employee
@app.route('/employee/delete/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
	employee = Employee.query.get_or_404(id)
	db.session.delete(employee)
	db.session.commit()
	return redirect(url_for('got_employee'))

#view employee payroll
@app.route('/employee/<int:id>/payroll')
def view_payroll(id):
	payroll= Payroll.query.filter_by(employee_id=id).all()
	return render_template('payroll.html', payroll=payroll)

#view employee attendance
@app.route('/employee/<int:id>/attendance')
def view_attendance(id):
	attendance = Attendance.query.filter_by(employee_id).all()
	return render_template('attendance.html', attendance=attendance)

#perfomance_reviews of an employment 
@app.route('/employee/<int:id>/perfomance')
def view_perfomance(id):
	perfomance = Perfomance.query.filter_by(employee_id=id).all()
	return render_template('perfomance.html', perfomance=perfomance)

#employ training review
@app.route('/employee/<int:id>/training')
def view_training(id):
	training = EmployeeTraining.query.filter_by(employee_id=id).all()
	return render_template('training.html', training=training)

#all project routes
@app.route('/projects')
def get_projects():
	projects = Projects.query.all()
	return render_template('[projects.html', projects=projects)

#assign project to an employee
@app.route('/project/assign/<int:project_id>', methods=['GET', 'POST'])
def assign_project(project_id):
	if request.method == 'POST':
		employee_id = request.form['employee_id']
		role = request.form['employee_id']
		hours_worked = request.form[hours_worked]
		assignment = ProjectAssignment(employee_id=employee_id,project_id=project_id, role_in_project=role, hours_worked=hours_worked)
		db.session.add(assignment)
		db.session.commit()
		return redirect(url_for('gets_projects'))
	return render_template('assign_project.html', project_id=project_id)

#review project details and assigned employees
@app.route('/project/<int:project_id>')
def project_details(project_id):
	project = Projects.query.get_or_404(project_id)
	assignment = ProjectAssignment.query.filter_by(project_id=project_id).all()
	return render_template('projects_details.html', project=project, assignments=assignments)

#Json raw data API food
@app.route('/api/employee/<int:id>')
def api_get_employee(id):
	employee = Employees.query.get_or_404(id)
	return jsonify({
		'id' : employee.employee_id,
		'name' : employee.name, 
		'department' : employee.department,
		'position' : employee.position
	})

#Error_Handling
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)

