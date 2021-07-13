def is_armstrong_number(number: int):
    val, number_original, n = 0, number, len(str(number))
    for d in str(number):
        val += (int(d) ** n)
    return val == number_original
