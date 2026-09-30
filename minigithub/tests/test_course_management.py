"""Tests for the course management domain model."""

import unittest
from abc import ABC

from course_management import (
    Course,
    CourseError,
    DuplicateEnrollmentError,
    EnrollmentStatus,
    FullCourseError,
    Mentor,
    Student,
    User,
)


class CourseManagementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mentor = Mentor("Morgan Lee", "MORGAN@example.com", "Python")
        self.course = Course(
            "PY101", "Python Foundations", "Learn Python.", self.mentor, capacity=1
        )
        self.student = Student("Alex Kim", "alex@example.com")

    def test_user_is_abstract_and_subclasses_override_role(self) -> None:
        self.assertTrue(issubclass(User, ABC))
        with self.assertRaises(TypeError):
            User("Casey", "casey@example.com")  # type: ignore[abstract]
        self.assertEqual(self.student.role, "Student")
        self.assertEqual(self.mentor.role, "Mentor")
        self.assertNotEqual(self.student.describe(), self.mentor.describe())

    def test_static_email_validation_and_class_generated_ids(self) -> None:
        self.assertTrue(User.is_valid_email("person@example.com"))
        self.assertFalse(User.is_valid_email("not-an-email"))
        self.assertTrue(self.student.student_id.startswith("student-"))
        self.assertTrue(self.mentor.mentor_id.startswith("mentor-"))

    def test_encapsulated_identity_validates_and_normalizes_values(self) -> None:
        student = Student("  Alex Kim ", "  ALEX@Example.com ")
        self.assertEqual(student.name, "Alex Kim")
        self.assertEqual(student.email, "alex@example.com")
        with self.assertRaises(ValueError):
            student.email = "invalid"
        with self.assertRaises(ValueError):
            student.name = " "

    def test_enrollment_links_student_course_and_completion(self) -> None:
        enrollment = self.student.enroll(self.course)
        self.assertIs(enrollment.student, self.student)
        self.assertIs(enrollment.course, self.course)
        self.assertEqual(enrollment.status, EnrollmentStatus.ACTIVE)
        self.assertEqual(self.course.enrolled_count, 1)
        self.assertEqual(len(self.student.enrollments), 1)

        enrollment.complete()
        self.assertEqual(enrollment.status, EnrollmentStatus.COMPLETED)
        with self.assertRaises(CourseError):
            enrollment.complete()

    def test_duplicate_and_full_course_enrollments_are_rejected(self) -> None:
        self.student.enroll(self.course)
        with self.assertRaises(DuplicateEnrollmentError):
            self.student.enroll(self.course)
        with self.assertRaises(FullCourseError):
            Student("Taylor", "taylor@example.com").enroll(self.course)

    def test_cancelling_releases_the_seat(self) -> None:
        enrollment = self.student.enroll(self.course)
        enrollment.cancel()
        self.assertEqual(enrollment.status, EnrollmentStatus.CANCELLED)
        self.assertEqual(self.course.available_seats, 1)
        self.assertEqual(self.student.enrollments, ())
        replacement = Student("Taylor", "taylor@example.com").enroll(self.course)
        self.assertEqual(replacement.status, EnrollmentStatus.ACTIVE)

    def test_course_and_mentor_expose_read_only_collections(self) -> None:
        course = Course("PY102", "Advanced Python", "More Python.", self.mentor)
        self.assertIn(course, self.mentor.courses)
        self.assertIsInstance(self.course.enrollments, tuple)
        self.assertIsInstance(self.mentor.courses, tuple)

    def test_invalid_course_details_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Course("", "Title", "Description", self.mentor)
        with self.assertRaises(ValueError):
            Course("ID", "Title", "Description", self.mentor, capacity=0)


if __name__ == "__main__":
    unittest.main()
