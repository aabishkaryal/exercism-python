from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.rows: List[int][int] = [[int(v) for v in r.split()]
                                     for r in matrix_string.splitlines()]

    # Returns the row of Matrix at index. (Matrix is indexed from 1)
    def row(self, index: int) -> List[int]:
        return [x for x in self.rows[index-1]]

    # Returns the column of Matrix at index. (Matrix is indexed from 1)
    def column(self, index) -> List[int]:
        return [r[index-1] for r in self.rows]
