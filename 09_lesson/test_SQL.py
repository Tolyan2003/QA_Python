from SQL import student, db
from sqlalchemy import insert, update, delete, select, and_
import pytest
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def setup_db():
    Session = sessionmaker(bind=db)
    session = Session()

    yield session

    session.close()


def test_add_student(setup_db):
    new_student = {
        "user_id": 5544,
        "level": "Pre-Intermediate",
        "education_form": "group",
        "subject_id": 2
    }
    result = setup_db.execute(insert(student).values(new_student))
    setup_db.commit()
    assert result.rowcount == 1


def test_update_student(setup_db):
    existing_student = {
        "user_id": 5544,
        "level": "Pre-Intermediate",
        "education_form": "group",
        "subject_id": 2
    }
    setup_db.execute(update(student).where(student.c.user_id == existing_student['user_id']).values(level="Elementary"))
    setup_db.commit()

    updated_student = setup_db.execute(
        student.select().where(student.c.user_id == existing_student['user_id'])).fetchone()
    assert updated_student.level == "Elementary"


def test_delete_student(setup_db):
    student_to_delete = {
        "user_id": 5544,
        "level": "Elementary",
        "education_form": "personal",
        "subject_id": 2
    }

    setup_db.execute(delete(student).where(student.c.user_id == student_to_delete['user_id']))
    setup_db.commit()

    deleted_student = setup_db.execute(student.select().where(student.c.user_id == student_to_delete['user_id'])).fetchone()
    assert deleted_student is None


def test_select_1_row_with_two_filters(setup_db):
    sql_statement = select(student).where(and_(student.c.user_id < 10000, student.c.level == 'Beginner'))
    result = setup_db.execute(sql_statement)
    for row in result:
        print(row)
