from connections import engine
from flask import Flask, jsonify, request
from operation import StudentOperations

app = Flask(__name__)

@app.route('/api/students', methods=['GET'])
def api_get_students():
    try:
        students = StudentOperations.get_students()
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students', methods=['POST'])
def api_add_student():
    try:
        data = request.get_json()
        StudentOperations.add_student(data['name'], data['major'], data['graduates'])
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/studentgpa', methods=['GET'])
def api_get_student_gpa():
    try:
        gpa_list = StudentOperations.get_student_gpa()
        return jsonify(gpa_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/studentgpa', methods=['POST'])
def api_add_student_gpa():
    try:
        data = request.get_json()
        StudentOperations.add_student_gpa(data['name'], data['gpa'])
        return jsonify({"message": "Student GPA added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/studenthousing', methods=['GET'])
def api_get_student_housing():
    try:
        housing_list = StudentOperations.get_student_housing()
        return jsonify(housing_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/studenthousing', methods=['POST'])
def api_add_student_housing():
    try:
        data = request.get_json()
        StudentOperations.add_student_housing(data['name'], data['hall'])
        return jsonify({"message": "Student housing added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



