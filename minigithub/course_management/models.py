"""Core entities and business rules for the course management system."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from enum import Enum
from itertools import count
from typing import ClassVar


class CourseError(Exception):
    """Base exception for course management rule violations."""


class DuplicateEnrollmentError(CourseError):
    """Raised when a student is already enrolled in a course."""


class FullCourseError(CourseError):
    """Raised when a course has reached its enrollment limit."""


class EnrollmentStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class User(ABC):
    """An abstract user with validated, encapsulated identity details."""

    _id_counter: ClassVar[count] = count(1)

    def __init__(self, name: str, email: str, user_id: str | None = None) -> None:
        self.name = name
        self.email = email
        self._user_id = user_id or self.generate_id()

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Return whether an email has a basic local@domain form."""
        local, separator, domain = email.strip().partition("@")
        return bool(separator and local and "." in domain and not domain.startswith("."))

    @classmethod
    def generate_id(cls) -> str:
        """Create a unique identifier prefixed with the concrete user type."""
        return f"{cls.__name__.lower()}-{next(User._id_counter):04d}"

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Name cannot be empty.")
        self._name = cleaned

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        cleaned = value.strip().lower()
        if not self.is_valid_email(cleaned):
            raise ValueError(f"Invalid email address: {value!r}")
        self._email = cleaned

    @property
    @abstractmethod
    def role(self) -> str:
        """Return the concrete user's role."""

    def describe(self) -> str:
        """Return a concise description; subclasses specialize this method."""
        return f"{self.role}: {self.name} ({self.email})"


class Student(User):
    """A learner who can enroll in courses."""

    def __init__(
        self, name: str, email: str, student_id: str | None = None
    ) -> None:
        super().__init__(name, email, student_id)
        self._enrollments: dict[str, Enrollment] = {}

    @property
    def role(self) -> str:
        return "Student"

    @property
    def student_id(self) -> str:
        return self.user_id

    @property
    def enrollments(self) -> tuple[Enrollment, ...]:
        return tuple(self._enrollments.values())

    def enroll(self, course: Course) -> Enrollment:
        """Enroll this student in a course, respecting course rules."""
        return course.enroll(self)

    def _add_enrollment(self, enrollment: Enrollment) -> None:
        self._enrollments[enrollment.course.course_id] = enrollment

    def _remove_enrollment(self, course_id: str) -> None:
        self._enrollments.pop(course_id, None)

    def describe(self) -> str:
        return f"{super().describe()} | Enrolled courses: {len(self.enrollments)}"


class Mentor(User):
    """An instructor who can be assigned to courses."""

    def __init__(
        self,
        name: str,
        email: str,
        expertise: str,
        mentor_id: str | None = None,
    ) -> None:
        super().__init__(name, email, mentor_id)
        self.expertise = expertise
        self._courses: dict[str, Course] = {}

    @property
    def role(self) -> str:
        return "Mentor"

    @property
    def mentor_id(self) -> str:
        return self.user_id

    @property
    def courses(self) -> tuple[Course, ...]:
        return tuple(self._courses.values())

    @property
    def expertise(self) -> str:
        return self._expertise

    @expertise.setter
    def expertise(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Expertise cannot be empty.")
        self._expertise = cleaned

    def _add_course(self, course: Course) -> None:
        self._courses[course.course_id] = course

    def describe(self) -> str:
        return (
            f"{super().describe()} | Expertise: {self.expertise} "
            f"| Courses: {len(self.courses)}"
        )


class Course:
    """A course with a mentor, capacity limit, and managed enrollments."""

    def __init__(
        self,
        course_id: str,
        title: str,
        description: str,
        mentor: Mentor,
        capacity: int = 30,
    ) -> None:
        cleaned_id = course_id.strip()
        cleaned_title = title.strip()
        if not cleaned_id:
            raise ValueError("Course ID cannot be empty.")
        if not cleaned_title:
            raise ValueError("Course title cannot be empty.")
        if not description.strip():
            raise ValueError("Course description cannot be empty.")
        if capacity < 1:
            raise ValueError("Course capacity must be at least 1.")
        self._course_id = cleaned_id
        self._title = cleaned_title
        self._description = description.strip()
        self._mentor = mentor
        self._capacity = capacity
        self._enrollments: dict[str, Enrollment] = {}
        mentor._add_course(self)

    @property
    def course_id(self) -> str:
        return self._course_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def mentor(self) -> Mentor:
        return self._mentor

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def enrollments(self) -> tuple[Enrollment, ...]:
        return tuple(self._enrollments.values())

    @property
    def enrolled_count(self) -> int:
        return len(self._enrollments)

    @property
    def available_seats(self) -> int:
        return self.capacity - self.enrolled_count

    def enroll(self, student: Student) -> Enrollment:
        """Enroll a student if the course has space and no duplicate."""
        if student.student_id in self._enrollments:
            raise DuplicateEnrollmentError(
                f"{student.name} is already enrolled in {self.title}."
            )
        if self.available_seats == 0:
            raise FullCourseError(f"{self.title} has reached its capacity.")
        enrollment = Enrollment(student, self)
        self._enrollments[student.student_id] = enrollment
        student._add_enrollment(enrollment)
        return enrollment

    def _remove_enrollment(self, student_id: str) -> None:
        self._enrollments.pop(student_id, None)

    def __str__(self) -> str:
        return (
            f"{self.title} ({self.course_id}) - mentor: {self.mentor.name}, "
            f"seats: {self.available_seats}/{self.capacity}"
        )


class Enrollment:
    """The association between one student and one course."""

    def __init__(self, student: Student, course: Course) -> None:
        self._student = student
        self._course = course
        self._status = EnrollmentStatus.ACTIVE
        self._enrolled_at = datetime.now(timezone.utc)

    @property
    def student(self) -> Student:
        return self._student

    @property
    def course(self) -> Course:
        return self._course

    @property
    def status(self) -> EnrollmentStatus:
        return self._status

    @property
    def enrolled_at(self) -> datetime:
        return self._enrolled_at

    def complete(self) -> None:
        """Mark an active enrollment as completed."""
        self._require_active()
        self._status = EnrollmentStatus.COMPLETED

    def cancel(self) -> None:
        """Cancel an active enrollment and release the course seat."""
        self._require_active()
        self._status = EnrollmentStatus.CANCELLED
        self.course._remove_enrollment(self.student.student_id)
        self.student._remove_enrollment(self.course.course_id)

    def _require_active(self) -> None:
        if self.status is not EnrollmentStatus.ACTIVE:
            raise CourseError(
                f"Cannot change an enrollment with status {self.status.value!r}."
            )
