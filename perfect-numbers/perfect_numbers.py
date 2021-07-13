def classify(number):
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


def getFactors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors
