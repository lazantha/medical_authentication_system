from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# all tables


class Admins(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(60))
    password = db.Column(db.String(300))

class Attempts(db.Model):
    att_id = db.Column(db.Integer, primary_key=True)
    attempt = db.Column(db.Integer)

class Departments(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True)
    dep_code = db.Column(db.String(10))
    department = db.Column(db.String(100))
    calling_name = db.Column(db.String(50))
    students = db.relationship('Students', backref='departments')
    subjects = db.relationship('Subjects', backref='departments')
    super_admin_list = db.relationship('SuperAdmins', backref='departments')

class Exams(db.Model):
    exm_id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    syllabus_id = db.Column(db.Integer, db.ForeignKey('syllabuses.syllabus_id'))
    super_admin_id = db.Column(db.Integer, db.ForeignKey('super_admins.super_admin_id'))
    held_date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    location = db.Column(db.String(10))

class MedicalInformations(db.Model):
    med_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    med_type_id = db.Column(db.Integer, db.ForeignKey('medical_types.medi_type_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    att_id = db.Column(db.Integer, db.ForeignKey('attempts.att_id'))
    exam_date= db.Column(db.Date)
    exam_location= db.Column(db.String(10))
    issued_date = db.Column(db.Date)
    from_date = db.Column(db.Date)
    to_date = db.Column(db.Date)
    doc_name = db.Column(db.String(50))
    hospital = db.Column(db.String(50))
    medical_sheet = db.Column(db.String(300))
    is_confirmed=db.Column(db.Boolean)
    is_authenticated=db.Column(db.Boolean)

    recorded_time = db.Column(db.Time)

class MedicalTypes(db.Model):
    medi_type_id = db.Column(db.Integer, primary_key=True)
    medi_type = db.Column(db.String(10))
    medical_informations = db.relationship('MedicalInformations', backref='medical_type')


class Students(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.dep_id'))
    student_type_id = db.Column(db.Integer, db.ForeignKey('student_types.studen_type_id'))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    index_number = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(300))
    password = db.Column(db.String(300))
    id_card = db.Column(db.String(300))
    medical_informations = db.relationship('MedicalInformations', backref='Students')
    student_type = db.relationship('StudentTypes', backref='Students')

class StudentTypes(db.Model):
    studen_type_id = db.Column(db.Integer, primary_key=True)
    student_type = db.Column(db.String(10))
    students = db.relationship('Students', backref='StudentTypes')

class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.dep_id'))
    exams = db.relationship('Exams', backref='subject')
    medical_informations = db.relationship('MedicalInformations', backref='subject')
    subject_name = db.Column(db.String(50))
    subject_code = db.Column(db.String(20))
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)

class SuperAdmins(db.Model):
    super_admin_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.dep_id'))
    department = db.relationship('Departments', backref='SuperAdmins')
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(300))
    password = db.Column(db.String(300))
    exams = db.relationship('Exams', backref='super_admin')

class Syllabuses(db.Model):
    syllabus_id = db.Column(db.Integer, primary_key=True)
    syllabus_type = db.Column(db.String(10))
    exams = db.relationship('Exams', backref='syllabus')

class ClosingDatesList(db.Model):
    date_id = db.Column(db.Integer, primary_key=True)
    closing_date = db.Column(db.Date)



