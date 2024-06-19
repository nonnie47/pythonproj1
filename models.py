from connections import engine
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.engine import URL


Base= declarative_base();

class Student(Base):
    __tablename__ = "students"

    name = Column(String, primary_key=True, index=True)
    major = Column(String, index=True)
    graduates = Column(Integer)

    gpa = relationship("StudentGPA", back_populates="student", uselist=False)
    hall = relationship("StudentHousing", back_populates="student")


class StudentGPA(Base):
    __tablename__ = "studentgpa"

    name = Column(String, ForeignKey("students.name"), primary_key=True)
    gpa = Column(Integer)

    student = relationship("Student", back_populates="gpa")


class StudentHousing(Base):
    __tablename__ = "studenthousing"

    name = Column(String, ForeignKey("students.name"), primary_key=True)
    hall = Column(String)

    student = relationship("Student", back_populates="hall")


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
