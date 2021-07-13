import re


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if (hey_bob.isspace() or hey_bob == ""):
        return "Fine. Be that way!"
    elif (hey_bob == hey_bob.upper() and
          hey_bob[-1] == "?" and
          re.match(".*[a-zA-z].*", hey_bob)):
        return "Calm down, I know what I'm doing!"
    elif (hey_bob == hey_bob.upper() and
          re.match(".*[a-zA-z].*", hey_bob)):
        return "Whoa, chill out!"
    elif (hey_bob[-1] == "?"):
        return "Sure."
    else:
        return "Whatever."
