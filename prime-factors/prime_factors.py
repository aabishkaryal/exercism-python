from typing import List


def factors(value: int) -> List[int]:
    factors = []
    candidate_factor = 2
    while value > 1:
        while value % candidate_factor == 0:
            factors.append(candidate_factor)
            value /= candidate_factor
        candidate_factor += 1
    return factors
