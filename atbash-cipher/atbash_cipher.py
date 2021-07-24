import string

translation = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1], string.punctuation + " ")


def encode(plain_text: str) -> str:
    cipher = list(plain_text.lower().translate(translation))
    for i in list(range(5, len(cipher), 5))[::-1]:
        cipher.insert(i, " ")
    return "".join(cipher)


def decode(ciphered_text: str) -> str:
    return ciphered_text.lower().translate(translation)
