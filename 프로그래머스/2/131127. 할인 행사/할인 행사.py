from collections import Counter

def solution(want, number, discount):
    dict = {w:n for w, n in zip(want, number)}
    cnt = 0
    for i in range(len(discount)-9):
        cnt += dict == Counter(discount[i:i+10])
    return cnt