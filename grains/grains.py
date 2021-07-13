def square(number):
    if number <= 0:
        raise ValueError("number cannot be less than or equal to 0")
    if number > 64:
        raise ValueError("number cannot be greater than 64")
    return 2 ** (number-1)


def total():
    return sum([square(i) for i in range(1, 65)])
