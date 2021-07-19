from typing import List
from collections import defaultdict


class Garden:
    def __init__(self, diagram: str,
                 students: List[str] = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                                        "Ginney", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.rows = [[self.convert(plant) for plant in list(row)]
                     for row in diagram.splitlines()]
        self.students = sorted(students)

    def plants(self, student: str) -> List[str]:
        i = self.students.index(student)
        result: List[str] = []
        for row in self.rows:
            result.extend(row[2*i:2*i+2])
        return result

    def convert(self, p: str) -> str:
        if p == "G":
            return "Grass"
        elif p == "C":
            return "Clover"
        elif p == "R":
            return "Radishes"
        elif p == "V":
            return "Violets"
