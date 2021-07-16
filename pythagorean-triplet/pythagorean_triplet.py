from typing import List
from math import ceil, gcd


def triplets_with_sum(sum: int) -> List[List[int]]:
    '''
    Generate all possible Pythagorean Triplets that add up to the given sum.
    '''
    triplets = []
    half_sum = sum / 2
    m_limit = ceil(half_sum ** 0.5)
    for m in range(2, m_limit):
        if half_sum % m == 0:
            sm = half_sum / m
            while sm % 2 == 0:
                sm /= 2
            k = m+2 if m % 2 == 1 else m+1
            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = half_sum / (k*m)
                    n = k - m
                    a = int(d * (m*m - n*n))
                    b = int(2 * d * m * n)
                    c = int(d * (m*m+n*n))
                    candidate = sorted([a, b, c])
                    if candidate not in triplets:
                        triplets.append(candidate)
                k += 2
    return triplets
