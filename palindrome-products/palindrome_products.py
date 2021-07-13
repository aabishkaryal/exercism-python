from typing import List
from unittest.main import main


class Product:
    def __init__(self, factor1=None, factor2=None) -> None:
        self.factors = None if (factor1 and factor2) == None else [
            factor1, factor2]
        self.product = None if (
            factor1 and factor2) == None else factor1 * factor2


def isPalindrome(n: int) -> bool:
    return str(n) == str(n)[:: -1]


def largest(min_factor: int, max_factor: int) -> int:
    if (min_factor > max_factor):
        raise ValueError("min is greater than max")
    products = set()
    max_products = []
    for i in range(max_factor, min_factor-1, -1):
        for j in range(i, min_factor-1, -1):
            p = Product(i, j)
            if (p in products):
                continue
            if (len(max_products) > 0):
                if (p.product < max_products[0].product):
                    break
                if (p.product == max_products[0].product):
                    max_products.append(p)
                elif (p.product > max_products[0].product and
                      isPalindrome(p.product)):
                    max_products = [p]
            else:
                if (isPalindrome(p.product)):
                    max_products = [p]
    return (max_products[0].product if len(max_products) > 0 else None,
            [p.factors for p in max_products])


def smallest(min_factor: int, max_factor: int) -> int:
    if (min_factor > max_factor):
        raise ValueError("min is greater than max")
    products = set()
    min_products = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            p = Product(i, j)
            if (p in products):
                continue
            if (len(min_products) > 0):
                if (p.product > min_products[0].product):
                    break
                if (p.product == min_products[0].product):
                    min_products.append(p)
                elif (p.product < min_products[0].product and
                      isPalindrome(p.product)):
                    min_products = [p]
            else:
                if (isPalindrome(p.product)):
                    min_products = [p]
    return (min_products[0].product if len(min_products) > 0 else None,
            [p.factors for p in min_products])
