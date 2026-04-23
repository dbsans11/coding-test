def solution(ms, pa):
    cnt=0
    for i in range(len(ms)-(l:=len(pa))+1):
        cnt += ms[i:i+l]==pa
    return cnt