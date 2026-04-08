def solution(wa,bi):
    cnt=0
    while min(wa)<min(bi) or max(wa)<max(bi):
        if bi[0] > bi[1]: bi[0]//=2
        else: bi[1]//=2
        cnt+=1
    return cnt