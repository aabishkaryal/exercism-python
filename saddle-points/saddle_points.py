from typing import Dict, List

Matrix = List[List[int]]
ListIndex = Dict[str, int]


def column(matrix: Matrix, index: int) -> List[int]:
    return [row[index] for row in matrix]


def saddle_points(matrix: Matrix) -> List[ListIndex]:
    result = set()
    if (matrix and sum([len(row) for row in matrix]) / len(matrix) != len(matrix[0])):
        raise ValueError("irregular matrix")
    for i, row in enumerate(matrix):
        candidate = max(row)
        prev_index = 0
        for _ in range(row.count(candidate)):
            candidate_index = row.index(candidate, prev_index)
            if (min(column(matrix, candidate_index)) == candidate):
                result.add((i+1, candidate_index+1))
            prev_index = candidate_index+1
    return [{"row": r[0], "column": r[1]} for r in result]


print(saddle_points([[6, 7, 8], [5, 5, 5], [7, 5, 6]]))
