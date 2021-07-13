def steps(n: int, current_steps: int = 0) -> int:
    if n <= 0:
        raise ValueError("number cannot be less or equal to zero")
    if n == 1:
        return current_steps
    return steps(n/2 if n % 2 == 0 else 3*n+1, current_steps+1)
