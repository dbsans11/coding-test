def solution(s,d):
    s=sorted(s)
    return 1 if any(s==sorted(c) for c in d) else 2