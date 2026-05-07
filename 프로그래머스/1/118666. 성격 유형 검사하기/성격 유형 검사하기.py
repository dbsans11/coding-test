def solution(survey, choices):
    d1,d2,r={'RT':(0,1),'TR':(0,-1),'CF':(1,1),'FC':(1,-1),'JM':(2,1),'MJ':(2,-1),'AN':(3,1),'NA':(3,-1)},[3,2,1,0,-1,-2,-3],[0,0,0,0]
    for s,c in zip(survey,choices):
        ti,tp=d1[s]
        r[ti]+=d2[c-1]*tp
    return ''.join([c[(v<0)*1] for v,c in zip(r,['RT','CF','JM','AN'])])
    