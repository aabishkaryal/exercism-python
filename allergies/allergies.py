allergis = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats"
]


class Allergies:

    def __init__(self, score):
        self.score = score % 256
        self.allergies = []
        # bin(self.score)[2:].zfill(8)[::-1]
        # bin(self.score)[2:] -> Convert to binary and remove the first two character which is '0b'
        # zfill(8)[::-1] -> Add additional 0s in front if needed to make sure the the string is of length 8 and reverse the string
        # Combined each digit in this new binary can be converted to the list of allergies
        for index, v in enumerate(bin(self.score)[2:].zfill(8)[::-1]):
            if (int(v)):
                self.allergies.append(allergis[index])

    def allergic_to(self, item):
        return self.allergies.count(item) > 0

    @property
    def lst(self):
        return self.allergies


print(Allergies(64).allergic_to("cats"))
