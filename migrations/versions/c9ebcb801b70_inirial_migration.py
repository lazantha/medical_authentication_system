"""inirial migration

Revision ID: c9ebcb801b70
Revises: 
Create Date: 2023-10-27 14:23:29.853156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9ebcb801b70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('attempts',
    sa.Column('att_id', sa.Integer(), nullable=False),
    sa.Column('attempt', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('att_id')
    )
    op.create_table('closing_dates_list',
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('closing_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('date_id')
    )
    op.create_table('departments',
    sa.Column('dep_id', sa.Integer(), nullable=False),
    sa.Column('dep_code', sa.String(length=10), nullable=True),
    sa.Column('department_list', sa.String(length=100), nullable=True),
    sa.Column('calling_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('dep_id')
    )
    op.create_table('medical_types',
    sa.Column('medi_type_id', sa.Integer(), nullable=False),
    sa.Column('medi_type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('medi_type_id')
    )
    op.create_table('student_types',
    sa.Column('studen_type_id', sa.Integer(), nullable=False),
    sa.Column('student_type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('studen_type_id')
    )
    op.create_table('syllabuses',
    sa.Column('syllabus_id', sa.Integer(), nullable=False),
    sa.Column('syllabus_type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('syllabus_id')
    )
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('student_type_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('index_number', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=300), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.Column('id_card', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.dep_id'], ),
    sa.ForeignKeyConstraint(['student_type_id'], ['student_types.studen_type_id'], ),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('subject_name', sa.String(length=50), nullable=True),
    sa.Column('subject_code', sa.String(length=20), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('semester', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.dep_id'], ),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('super_admins',
    sa.Column('super_admin_id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=300), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.dep_id'], ),
    sa.PrimaryKeyConstraint('super_admin_id')
    )
    op.create_table('exams',
    sa.Column('exm_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('syllabus_id', sa.Integer(), nullable=True),
    sa.Column('super_admin_id', sa.Integer(), nullable=True),
    sa.Column('held_date', sa.Date(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('location', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.ForeignKeyConstraint(['super_admin_id'], ['super_admins.super_admin_id'], ),
    sa.ForeignKeyConstraint(['syllabus_id'], ['syllabuses.syllabus_id'], ),
    sa.PrimaryKeyConstraint('exm_id')
    )
    op.create_table('medical_informations',
    sa.Column('med_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('med_type_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('att_id', sa.Integer(), nullable=True),
    sa.Column('exam_date', sa.Date(), nullable=True),
    sa.Column('exam_location', sa.String(length=10), nullable=True),
    sa.Column('issued_date', sa.Date(), nullable=True),
    sa.Column('from_date', sa.Date(), nullable=True),
    sa.Column('to_date', sa.Date(), nullable=True),
    sa.Column('doc_name', sa.String(length=50), nullable=True),
    sa.Column('hospital', sa.String(length=50), nullable=True),
    sa.Column('medical_sheet', sa.String(length=300), nullable=True),
    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
    sa.Column('is_authenticated', sa.Boolean(), nullable=True),
    sa.Column('recorded_time', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['att_id'], ['attempts.att_id'], ),
    sa.ForeignKeyConstraint(['med_type_id'], ['medical_types.medi_type_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.PrimaryKeyConstraint('med_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical_informations')
    op.drop_table('exams')
    op.drop_table('super_admins')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('syllabuses')
    op.drop_table('student_types')
    op.drop_table('medical_types')
    op.drop_table('departments')
    op.drop_table('closing_dates_list')
    op.drop_table('attempts')
    op.drop_table('admins')
    # ### end Alembic commands ###