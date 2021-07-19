from typing import Set


def classify(number: int) -> str:
    if number > 0:
        factors = getFactors(number)
        s = sum(factors)
        if s == number:
            return "perfect"
        elif s > number:
            return "abundant"
        else:
            return "deficient"
    else:
        raise ValueError("positive integer required")


def getFactors(n: int) -> Set[int]:
    if n <= 1:
        return []
    factors = {1, }
    limit = int(n ** 0.5)+1
    for i in range(2, limit):
        if n % i == 0:
            factors.add(i)
            factors.add(n/i)
    return factors
