def solution(score):
    score=[x+y for x,y in score]
    rank={}
    for i,v in enumerate(sorted(score, reverse=1)):
        if v not in rank: rank[v]=i+1
    return [rank[v] for v in score]