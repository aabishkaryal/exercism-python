import string
import random

alphabets = list(string.ascii_uppercase)


class Robot:
    def __init__(self):
        random.seed()
        self.name = random.choice(
            alphabets) + random.choice(alphabets) + "{:0>3}".format(random.randrange(0, 1000))

    def reset(self):
        random.seed()
        self.name = random.choice(
            alphabets) + random.choice(alphabets) + "{:0>3}".format(random.randrange(0, 1000))
