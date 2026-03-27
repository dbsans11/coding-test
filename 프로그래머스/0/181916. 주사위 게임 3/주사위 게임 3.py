from collections import Counter
def solution(a,b,c,d):
    cnt = Counter([a,b,c,d]).most_common(4)
    if (n:=len(cnt))==1: return 1111*cnt[0][0]
    if n==2:
        if cnt[0][1]==3: return (10*cnt[0][0]+cnt[1][0])**2
        else: return (cnt[0][0]+cnt[1][0])*abs(cnt[0][0]-cnt[1][0])
    if n==3: return cnt[1][0] * cnt[2][0]
    else: return min(a,b,c,d)