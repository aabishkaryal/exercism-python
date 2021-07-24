from collections import deque

bracket_pairs = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_paired(input_string: str) -> bool:
    stack = deque()
    for bracket in input_string:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        if bracket in bracket_pairs.keys() and (len(stack) == 0 or stack.pop() != bracket_pairs[bracket]):
            return False
    if len(stack) == 0:
        return True
    return False
