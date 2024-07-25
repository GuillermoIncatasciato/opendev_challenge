import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import Mock
from app.services import Service
from app.schemas import StudentBase, Subject, Degree


class TestServices:
    def test_create_student(self):
        mock_dao = Mock()
        service = Service(mock_dao)
        student_base = StudentBase(
            **{
                "name": "John",
                "email": "john@email.com",
                "address": "Some Address 123",
                "phone": 123456,
            }
        )
        mock_dao.add_student = Mock()

        service.create_student(student_base)

        mock_dao.add_student.assert_called_once()

    def test_create_subject(self):
        mock_dao = Mock()
        service = Service(mock_dao)
        subject = Subject(**{"name": "Math", "degree_id": 123})
        mock_dao.add_subject = Mock()

        service.create_subject(subject)

        mock_dao.add_subject.assert_called_once()

    def test_create_degree(self):
        mock_dao = Mock()
        service = Service(mock_dao)
        degree = Degree(
            **{
                "name": "Computer science",
            }
        )
        mock_dao.add_degree = Mock()

        service.create_degree(degree)

        mock_dao.add_degree.assert_called_once()
