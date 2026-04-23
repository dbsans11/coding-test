from collections import Counter
def solution(a):
    cnt=Counter(a).most_common(2)
    if len(cnt)>1 and cnt[0][1]==cnt[1][1]: return -1
    return cnt[0][0]