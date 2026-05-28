from flask import Flask, render_template, request

app = Flask(__name__)

employees = {
    "pavani": {
        "password": "1234",
        "details": {
            "Employee ID": "EMP101",
            "Department": "Testing",
            "Salary": "50000",
            "Location": "Bangalore"
        }
    }
}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/employee', methods=['POST'])
def employee():

    username = request.form['username']
    password = request.form['password']

    if username in employees and employees[username]["password"] == password:

        employee_details = employees[username]["details"]

        return render_template(
            "employee.html",
            username=username,
            details=employee_details
        )

    return "Invalid Username or Password"

if __name__ == '__main__':
    app.run(debug=True)