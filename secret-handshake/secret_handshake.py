from typing import List

secret = ["wink", "double blink", "close your eyes", "jump"]


def commands(number: int) -> List[str]:
    binary = bin(number)[2:]
    secret_handshake = []
    for i, b in enumerate(binary[:-5:-1]):
        if bool(int(b)):
            secret_handshake.append(secret[i])

    if len(binary) >= 5 and binary[4] == '1':
        secret_handshake.reverse()

    return secret_handshake
