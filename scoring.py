def score(time, memory, correct):
    if not correct:
        return 0
    return max(0, 1000 - (time * 1e6))
