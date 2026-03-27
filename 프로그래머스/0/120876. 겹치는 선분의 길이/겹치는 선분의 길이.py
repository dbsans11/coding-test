def solution(lines):
    sets = [set(range(min(v), max(v))) for v in lines]
    return len(sets[0]&sets[1] | sets[1]&sets[2] | sets[2]&sets[0])