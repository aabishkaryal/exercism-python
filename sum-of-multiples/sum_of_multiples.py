from typing import List, Set


def sum_of_multiples(limit: int, factors: List[int]) -> int:
    multiples: Set[int] = set()
    for f in factors:
        if f == 0:
            continue
        n = int(limit / f)
        for i in range(1, n if limit % f == 0 else n+1):
            multiples.add(f*i)
    return sum(multiples)
