def solution(s):
    ar = list(map(int, s.split()))
    return f'{min(ar)} {max(ar)}'