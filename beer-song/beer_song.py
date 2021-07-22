from typing import List


def recite(start: int, take: int = 1) -> List[str]:
    result = []
    for i in range(take):
        if (start == 0):
            result.append(
                "No more bottles of beer on the wall, no more bottles of beer.")
            result.append(
                "Go to the store and buy some more, 99 bottles of beer on the wall.")
            continue
        if (start == 1):
            result.append(
                "{0} bottle of beer on the wall, {0} bottle of beer.".format(start))
        else:
            result.append(
                "{0} bottles of beer on the wall, {0} bottles of beer.".format(start))

        if (start == 2):
            result.append(
                "Take one down and pass it around, {0} bottle of beer on the wall.".format(start-1))
        elif (start == 1):
            result.append(
                "Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            result.append(
                "Take one down and pass it around, {0} bottles of beer on the wall.".format(start-1))
        if (i != take - 1):
            result.append("")
        start -= 1
    return result
