from connections import engine
from flask import Flask, jsonify, request
from operation import add_student, get_students, add_student_gpa, get_student_gpa, add_student_housing, get_student_housing

app = Flask(__name__)

@app.route('/api/students', methods=['GET'])
def api_get_students():
    students = get_students()
    return jsonify(students)

@app.route('/api/students', methods=['POST'])
def api_add_student():
    data = request.get_json()
    add_student(data['name'], data['major'], data['graduates'])
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/api/studentgpa', methods=['GET'])
def api_get_student_gpa():
    gpa_list = get_student_gpa()
    return jsonify(gpa_list)

@app.route('/api/studentgpa', methods=['POST'])
def api_add_student_gpa():
    data = request.get_json()
    add_student_gpa(data['name'], data['gpa'])
    return jsonify({"message": "Student GPA added successfully"}), 201

@app.route('/api/studenthousing', methods=['GET'])
def api_get_student_housing():
    housing_list = get_student_housing()
    return jsonify(housing_list)

@app.route('/api/studenthousing', methods=['POST'])
def api_add_student_housing():
    data = request.get_json()
    add_student_housing(data['name'], data['housing'])
    return jsonify({"message": "Student housing added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

