from typing import Dict, List
from collections import defaultdict

# Convert plant first letter to full plant name
plants = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    def __init__(self, diagram: str,
                 students: List[str] = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                                        "Ginney", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        # Split diagram to proper row with full plant name
        self.rows = [[plants[p] for p in list(row)]
                     for row in diagram.splitlines()]
        # Sort the students alphabetically
        self.students = sorted(students)

        # Determine which student is responsible for which plant and store in dictionary.
        self.student_plants: Dict[str, List[str]] = {}
        for student in self.students:
            self.student_plants[student] = self.__getPlants(student)

    def __getPlants(self, student: str) -> List[str]:
        '''
        Returns the plants for which the student is responsible for taking care of.
        '''
        i = self.students.index(student)
        result: List[str] = []
        for row in self.rows:
            result.extend(row[2*i:2*i+2])
        return result

    def plants(self, student: str) -> List[str]:
        '''
        Returns the plants for which the student is responsible for taking care of.
        '''
        return self.student_plants[student]
