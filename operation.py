from connections import engine
from sqlalchemy.orm import sessionmaker
from models import SessionLocal, Student, StudentGPA, StudentHousing
import logging

# Configure logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class StudentOperations:
    @staticmethod
    def get_students():
        try:
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
        except Exception as e:
            logger.error(f"Error getting students: {e}")
            return []

    @staticmethod
    def add_student(name, major, graduates):
        try:
            session = SessionLocal()
            new_student = Student(name=name, major=major, graduates=graduates)
            session.add(new_student)
            session.commit()
            session.close()
        except Exception as e:
            logger.error(f"Error adding student: {e}")

    @staticmethod
    def get_student_gpa():
        try:
            session = SessionLocal()
            student_gpa = session.query(StudentGPA).all()
            gpa_list = [{"name": gpa.name, "gpa": gpa.gpa} for gpa in student_gpa]
            session.close()
            return gpa_list
        except Exception as e:
            logger.error(f"Error getting student GPA: {e}")
            return []

    @staticmethod
    def add_student_gpa(name, gpa):
        try:
            session = SessionLocal()
            new_gpa = StudentGPA(name=name, gpa=gpa)
            session.add(new_gpa)
            session.commit()
            session.close()



