def distance(strand_a: str, strand_b: str) -> int:
    if (strand_a != strand_b and (strand_b == "" or strand_a == "")):
        raise ValueError("Empty strands")
    if (len(strand_a) != len(strand_b)):
        raise ValueError("Unequal length strands")
    return len([x for i, x in enumerate(strand_a) if strand_a[i] != strand_b[i]])
