import re


class PhoneNumber:
    def __init__(self, number: str):

        number = re.sub(r"[.|(|)|\-|+| ]", "", number)
        number = re.sub(r"^1", "", number)
        if re.fullmatch(r"[2-9]\d{2}[2-9]\d{6}", number):
            self.number = number
            self.area_code = number[:3]
        else:
            raise ValueError("invalid number")

    def pretty(self):
        return "({})-{}-{}".format(self.number[:3], self.number[3:6], self.number[6:])
