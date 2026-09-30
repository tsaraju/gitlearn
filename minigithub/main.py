"""Run a short demonstration of the course management system."""

from course_management import Course, Mentor, Student


def main() -> None:
    mentor = Mentor("Morgan Lee", "morgan@example.com", "Python programming")
    course = Course(
        "PY101",
        "Python Foundations",
        "Learn core Python and object-oriented programming.",
        mentor,
        capacity=2,
    )
    student = Student("Alex Kim", "alex@example.com")

    enrollment = student.enroll(course)
    print(course)
    print(student.describe())
    print(mentor.describe())
    print(f"Enrollment status: {enrollment.status.value}")


if __name__ == "__main__":
    main()
