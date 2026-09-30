# Course Management System

A small, dependency-free Python project for managing course mentors, students,
and enrollments. Its domain model demonstrates core object-oriented programming
principles while enforcing practical rules such as course capacity, duplicate
enrollment prevention, and seat release on cancellation.

## Features

- Abstract `User` base class with specialized `Student` and `Mentor` subclasses.
- Validated, encapsulated identity and course data exposed through properties.
- Polymorphic user roles and descriptions.
- `Course` and `Enrollment` entities with bidirectional relationships.
- Capacity limits, duplicate checks, enrollment completion, and cancellation.
- Static email validation and class-level unique user ID generation.
- Standard-library unit tests; no third-party packages required.

## Architecture and OOP concepts

| Class | Responsibility |
| --- | --- |
| `User` | Abstract base for shared identity, validation, generated IDs, and descriptions. |
| `Student` | Enrolls in courses and exposes its enrollments as a read-only tuple. |
| `Mentor` | Stores an area of expertise and its assigned courses. |
| `Course` | Holds course details and mentor, enforces capacity, and creates enrollments. |
| `Enrollment` | Represents a student's course registration and its lifecycle. |

- **Inheritance:** `Student` and `Mentor` inherit from `User`.
- **Encapsulation:** Internal fields are private-by-convention; properties validate
  input and collection properties return tuples rather than mutable internals.
- **Polymorphism:** `Student` and `Mentor` implement `role` and specialize
  `describe()`.
- **Abstraction:** `User` is an `ABC` with an abstract `role` property.
- **Instance methods:** `Student.enroll()`, `Course.enroll()`,
  `Enrollment.complete()`, and `Enrollment.cancel()` operate on object state.
- **`@staticmethod`:** `User.is_valid_email()` validates without needing an
  instance or class state.
- **`@classmethod`:** `User.generate_id()` uses the concrete subclass name and a
  shared counter to generate IDs.

## Requirements

- Python 3.10 or newer
- Git (only needed for the optional version-control workflow)

There are no external Python dependencies.

## Installation

Clone the repository, then enter this project folder:

```powershell
git clone https://github.com/tsaraju/gitlearn.git
cd gitlearn/minigithub
```

Optionally create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Usage

Run the included example from this folder:

```powershell
py main.py
```

Use the classes in another Python file in this folder:

```python
from course_management import Course, Mentor, Student

mentor = Mentor("Morgan Lee", "morgan@example.com", "Python")
course = Course(
    "PY101",
    "Python Foundations",
    "Learn Python and OOP.",
    mentor,
    capacity=25,
)
student = Student("Alex Kim", "alex@example.com")

enrollment = student.enroll(course)
print(course)
print(student.describe())
enrollment.complete()
```

Duplicate or over-capacity enrollments raise `DuplicateEnrollmentError` or
`FullCourseError`. Cancelling an active enrollment releases its seat:

```python
enrollment.cancel()
```

## Tests

Run the standard-library test suite from this folder:

```powershell
py -m unittest discover -s tests -v
```

## Git feature-branch and pull-request workflow

The project can be developed on a feature branch, reviewed, and merged through a
pull request:

```powershell
git switch -c feature/course-management-system
git add course_management main.py tests
git commit -m "Add OOP course management system"
git add README.md
git commit -m "Document course management system"
git push -u origin feature/course-management-system
```

Open a pull request from `feature/course-management-system` into `main` on
GitHub, review and merge it, then update the local branch:

```powershell
git switch main
git pull
```
