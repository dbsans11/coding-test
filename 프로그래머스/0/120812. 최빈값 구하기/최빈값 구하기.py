from collections import Counter
def solution(a):
    cnt = Counter(a).most_common(2)
    return -1 if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0]