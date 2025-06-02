"""MEDIUM - Student class"""


# Solution 1
class Student:
    """Student"""

    def __init__(self, name: str) -> None:
        self.grades = []
        self.name = name

    def add_exam(self, grade) -> None:
        """Add exam to the student"""
        self.grades.append(grade)

    def get_mean(self) -> float:
        """Returns mean of students grades"""
        return sum(self.grades) / len(self.grades)


class School:
    """School"""

    def __init__(self, name: str) -> None:
        self.students = []
        self.name = name

    def add_student(self, student: Student) -> None:
        """Add student to the school"""
        self.students.append(student)

    def get_mean(self) -> float:
        """Returns mean of all students"""
        return sum(s.get_mean() for s in self.students) / len(self.students)

    def get_best_student(self) -> Student:
        """Returns best student"""
        return max(self.students, key=lambda s: s.get_mean())


class City:
    """City"""

    def __init__(self, name: str) -> None:
        self.school = []
        self.name = name

    def add_school(self, school: School) -> None:
        """Add school to the city"""
        self.school.append(school)

    def get_mean(self) -> float:
        """Get mean of all schools"""
        return sum(s.get_mean() for s in self.school) / len(self.school)

    def get_best_school(self) -> School:
        """Returns best school"""
        return max(self.school, key=lambda s: s.get_mean())

    def get_best_student(self) -> Student:
        """Returns best student"""
        return self.get_best_school().get_best_student()


if __name__ == "__main__":
    paris = City("paris")
    hkis = School("hkis")
    paris.add_school(hkis)
    for student_name, student_grades in (
        ("alice", (1, 2, 3)),
        ("bob", (2, 3, 4)),
        ("catherine", (3, 4, 5)),
        ("daniel", (4, 5, 6)),
    ):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)
