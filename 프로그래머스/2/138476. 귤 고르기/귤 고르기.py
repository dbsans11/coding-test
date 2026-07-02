from collections import Counter
def solution(k, tangerine):
    cnt = Counter(tangerine).most_common()
    arr = []
    for n, c in cnt:
        arr.extend([n]*c)
    return len(set(arr[:k]))