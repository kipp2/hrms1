from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

def get_db_connection():
	return psycopg2.connect(
		dbname="hRmSpayroll",
		user="ray",
		password="rayray",
		host="localhost"
	)

@app.route('/add_employee', methods=['GET'])
def add_employee_form():
	return render_template('add_employee.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
	name = request.form['name']
	role_id = request.form['role_id']
	salary = request.form['salary']
	off_days = request.form['off_days']

	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO Employees (name, role_id, salary, off_days) VALUES (%s, %s, %s, %s) ", 
		(name, role_id, salary, off_days)
	)
	conn.commit()
	cursor.close()
	conn.close()
	return redirect(url_for('employees'))
	
@app.route('/employees')
def employees():
    return "coming soon "

if __name__ == "__main__":
	app.run(debug=True)

