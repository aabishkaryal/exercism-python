check_dict = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}


def convert(number):
    result = ""
    for k in check_dict:
        if number % k == 0:
            result += check_dict[k]
    return result or str(number)


print(convert(105))
