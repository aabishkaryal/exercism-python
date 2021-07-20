positions = ["", "", "thousand", "million", "billion", "trillion"]

single_digit_num_to_words = {'0': '', '1': 'one', '2': 'two', '3': 'three',
                             '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', }

teen_numbers = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
                }

tens = {'1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty',
        '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}


def say(number: int) -> str:
    if (number < 0 or number > 999999999999):
        raise ValueError("number out of range. -1 < number < 999999999999")
    if (number == 0):
        return "zero"
    n = str(number)[::-1]
    digits_position = []
    for i in range(0, len(n), 3):
        digits = n[i:i+3][::-1]
        digits_position.insert(0, digits)
    in_word = ""
    num_positions = len(digits_position)
    for i, digits in enumerate(digits_position):
        digit_in_word = say3digit(digits)
        if (digit_in_word == ''):
            continue
        in_word += "{} {} ".format(say3digit(digits),
                                   positions[num_positions - i])
    return in_word.strip()


def say3digit(number: str) -> str:
    if (0 > int(number) > 999):
        raise ValueError("number out of range. -1 < number < 1000")
    if (len(number) == 1):
        return single_digit_num_to_words[number]
    elif (len(number) == 2):
        return double_digit_num_to_words(number)
    return three_digit_num_to_words(number)


def double_digit_num_to_words(number: str) -> str:
    if (len(number) != 2):
        raise ValueError("only double digit numbers accepted.")
    if (number[0] == '0'):
        return single_digit_num_to_words[number[1]]
    n = int(number)
    if (n > 10 and n < 20):
        return teen_numbers[number]
    return (tens[number[0]] + "-" + single_digit_num_to_words[number[1]]) if number[1] != '0' else tens[number[0]]


def three_digit_num_to_words(number: str) -> str:
    if (len(number) != 3):
        raise ValueError("only three digit numbers accepted.")
    if (number[0] == '0'):
        return double_digit_num_to_words(number[1:])
    return single_digit_num_to_words[number[0]] + " hundred " + double_digit_num_to_words(number[1:])
