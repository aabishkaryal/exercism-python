from functools import reduce


def largest_product(series: str, n: int) -> int:
    '''
    Returns the largest product in series of n consecutive digits
    '''
    if n > len(series):
        raise ValueError('n cannot be greater than the length of series')
    if n < 0:
        raise ValueError('n cannot be less than 0')
    if n == 0:
        return 1
    series = [int(i) for i in series]
    largest = 0
    for i in range(len(series) - n+1):
        product = reduce(lambda x, y: x * y, series[i:i+n])
        if product > largest:
            largest = product
    return largest
