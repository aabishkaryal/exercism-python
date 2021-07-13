import re


def is_valid(isbn: str) -> bool:
    if re.search(r"^\d-?\d{3}-?\d{5}-?[\dX]$", isbn):
        isbn = isbn.replace("-", "")[::-1]
        return sum([convert(c) * i for i, c in enumerate(isbn, start=1)]) % 11 == 0
    return False


def convert(x: str) -> int:
    return 10 if x == "X" else int(x)
