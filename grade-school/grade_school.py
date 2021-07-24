from typing import List

from dataclasses import dataclass


class School:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, grade: int) -> None:
        """
        Add student to the school at grade
        """

        print(self.students)
        new_student = Student(name, grade)
        for i, s in enumerate(self.students):
            if new_student < s:
                self.students.insert(i, new_student)
                return
        self.students.append(new_student)

    def roster(self) -> List[str]:
        """
        Returns the roster sorted primarily by grade then alphabetically
        """
        return [student.name for student in self.students]

    def grade(self, grade_number: int) -> List[str]:
        """
        Returns the student in grade_number sorted alphabetically.
        """
        return [student.name for student in self.students if student.grade == grade_number]


@dataclass(frozen=True)
class Student:
    name: str
    grade: int

    def __lt__(self, other) -> bool:
        if self.grade == other.grade:
            if min(self.name, other.name) == self.name:
                return True
            return False
        else:
            if self.grade< other.grade:
                return True
            return False

    def __gt__(self, other) -> bool:
        return self != other and not self < other

    def __ne__(self, other) -> bool:
        return not self == other

    def __eq__(self, other) -> bool:
        return other.grade == self.grade and other.name == self.name

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __ge__(self, other) -> bool:
        return self > other or self == other


school = School()
school.add_student(name="Peter", grade=2)
school.add_student(name="Anna", grade=1)
school.add_student(name="Barb", grade=1)
school.add_student(name="Zoe", grade=2)
school.add_student(name="Alex", grade=2)
school.add_student(name="Jim", grade=3)
school.add_student(name="Charlie", grade=1)
expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
print(school.roster())
print(expected)
