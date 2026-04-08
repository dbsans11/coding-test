def solution(k,m,score):
    score.sort(reverse=1)
    profit,idx,ln=0,0,len(score)
    while idx+m<=ln: 
        profit+=min(score[idx:idx+m])*m
        idx+=m
    return profit