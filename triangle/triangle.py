from typing import List


def equilateral(sides: List[int]):
    return sides[0] == sides[1] == sides[2] != 0


def isosceles(sides: List[int]):
    return (2*max(sides) < sum(sides) and  # Triangle inequality
            (sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]))  # Two sides equal


def scalene(sides: List[int]):
    return (2*max(sides) < sum(sides) and  # Triangle inequality
            sides[0] != sides[1] != sides[2])  # Scalene test
