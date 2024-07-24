import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import Mock
from app.controllers import Controller
from app.schemas import StudentBase, Subject, Degree


class TestControllers:

    def test_create_student(self):
        mock_repo = Mock()
        controller = Controller(mock_repo)
        student_base = StudentBase(**{
            "name": "John",
            "email": "john@email.com",
            "address": "Some Address 123",
            "phone": 123456
        })
        mock_repo.add_student = Mock()

        controller.create_student(student_base)

        mock_repo.add_student.assert_called_once()

    def test_create_subject(self):
        mock_repo = Mock()
        controller = Controller(mock_repo)
        subject = Subject(**{
            "name": "Math",
            "degree_id": 123
        })
        mock_repo.add_subject = Mock()

        controller.create_subject(subject)

        mock_repo.add_subject.assert_called_once()

    def test_create_degree(self):
        mock_repo = Mock()
        controller = Controller(mock_repo)
        degree = Degree(**{
            "name": "Computer science",
        })
        mock_repo.add_degree = Mock()

        controller.create_degree(degree)

        mock_repo.add_degree.assert_called_once()