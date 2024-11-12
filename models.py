from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class Employees(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    department = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    phone_number = db.Column(db.String(15))
    hire_date = db.Column(db.Date)
    role = db.Column(db.String(50))
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))

class Payroll(db.Model):
    __tablename__ = 'payroll'
    payroll_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    base_salary = db.Column(db.Numeric)
    deductions = db.Column(db.Numeric)
    net_salary = db.Column(db.Numeric)
    pay_date = db.Column(db.Date)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    attendance_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete='CASCADE'))
    check_in = db.Column(db.DateTime)
    check_out = db.Column(db.DateTime)
    leave_type = db.Column(db.String())
    leave_duration = db.Column(db.Interval)
    attendance_date = db.Column(db.Date, nullable=False)

class Performance(db.Model):
    __tablename__ = 'performance'
    performance_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    review_date = db.Column(db.Date)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    performance_score = db.Column(db.Integer, db.CheckConstraint("performance_score BETWEEN 1 AND 5"))
    comments = db.Column(db.Text)

class Recruitment(db.Model):
    __tablename__ = 'recruitment'
    recruitment_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50))
    posted_date = db.Column(db.Date)
    application_deadline = db.Column(db.Date)
    status = db.Column(db.String(20), db.CheckConstraint("status IN ('Open', 'Closed', 'Filled')"))
    salary_offered = db.Column(db.Numeric)

class Applicants(db.Model):
    __tablename__ = 'applicants'
    applicant_id = db.Column(db.Integer, primary_key=True)
    recruitment_id = db.Column(db.Integer, db.ForeignKey('recruitment.recruitment_id', ondelete="CASCADE"))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    application_date = db.Column(db.Date)
    status = db.Column(db.String(20), db.CheckConstraint("status IN ('Pending', 'Interviewed', 'Rejected', 'Hired')"))

class Training(db.Model):
    __tablename__ = 'training'
    training_id = db.Column(db.Integer, primary_key=True)
    training_name = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    certification = db.Column(db.Boolean, default=False)

class EmployeeTraining(db.Model):
    __tablename__ = 'employee_training'
    employee_training_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    training_id = db.Column(db.Integer, db.ForeignKey('training.training_id', ondelete="CASCADE"))
    completion_date = db.Column(db.Date)
    status = db.Column(db.String(20), db.CheckConstraint("status IN ('Completed', 'In Progress', 'Not Started')"))

class Compliance(db.Model):
    __tablename__ = 'compliance'
    compliance_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    requirement = db.Column(db.String(100))
    status = db.Column(db.String(20), db.CheckConstraint("status IN ('pending', 'completed', 'Not Required')"))
    due_date = db.Column(db.Date)
    completion_date = db.Column(db.Date)

class Projects(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    client_name = db.Column(db.String(100))

class ProjectAssignment(db.Model):
    __tablename__ = "project_assignment"
    assignment_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id', ondelete="CASCADE"))
    role_in_project = db.Column(db.String(50))
    hours_worked = db.Column(db.Numeric, default=0)

class Expense(db.Model):
    __tablename__ = 'expenses'
    expense_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    expense_date = db.Column(db.Date)
    expense_type = db.Column(db.String(50))
    amount = db.Column(db.Numeric)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), db.CheckConstraint("status IN ('submitted', 'approved', 'rejected')"))
    approval_date = db.Column(db.Date)

class Document(db.Model):
    __tablename__ = 'documents'
    document_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id', ondelete="CASCADE"))
    document_type = db.Column(db.String(50))
    file_path = db.Column(db.String(50))
    upload_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)

