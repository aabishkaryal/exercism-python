def latest(scores: list):
    return scores[-1]


def personal_best(scores: list):
    return sorted(scores)[-1]


def personal_top_three(scores: list):
    return sorted(scores, reverse=True)[:3]
