
from typing import List


def primes(limit: int) -> List[int]:
    '''
    primes uses the sieve of eratosthenes to find all the primes less than the limit
    '''
    limit += 1
    nums = {x: True for x in range(2, limit)}
    for i in range(2, limit):
        if nums[i]:
            for j in range(i * i, limit, i):
                nums[j] = False
    return [x for x in nums if nums[x]]
