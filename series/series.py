def slices(series: str, length: int):
    if len(series) < length:
        raise ValueError("length cannot be greater than length of string")
    if length <= 0:
        raise ValueError("length must be greater than 0")
    return [series[i:i+length] for i in range(len(series)-length+1)]
