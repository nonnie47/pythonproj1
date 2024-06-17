from models import SessionLocal, Student, StudentGPA, StudentHousing

def get_students():
    session = SessionLocal()
    students = session.query(Student).all()
    student_list = [
        {
            "name": student.name,
            "major": student.major,
            "graduates": student.graduates
        } for student in students
    ]
    session.close()
    return student_list

def add_student(name, major, graduates):
    session = SessionLocal()
    new_student = Student(name=name, major=major, graduates=graduates)
    session.add(new_student)
    session.commit()
    session.close()

def get_student_gpa():
    session = SessionLocal()
    student_gpa = session.query(StudentGPA).all()
    gpa_list = [{"name": gpa.name, "gpa": gpa.gpa} for gpa in student_gpa]
    session.close()
    return gpa_list

def add_student_gpa(name, gpa):
    session = SessionLocal()
    new_gpa = StudentGPA(name=name, gpa=gpa)
    session.add(new_gpa)
    session.commit()
    session.close()

def get_student_housing():
    session = SessionLocal()
    student_housing = session.query(StudentHousing).all()
    housing_list = [{"name": housing.name, "housing": housing.housing} for housing in student_housing]
    session.close()
    return housing_list

def add_student_housing(name, housing):
    session = SessionLocal()
    new_housing = StudentHousing(name=name, housing=housing)
    session.add(new_housing)
    session.commit()
    session.close()

