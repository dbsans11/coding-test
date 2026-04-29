def solution(km, tg):
    cnt={}
    for k in km:
        for i,c in enumerate(k):
            if c in cnt: cnt[c]=min(cnt[c],i+1)
            else: cnt[c]=i+1
    
    res=[]
    for t in tg:
        r=0
        for c in t:
            if c not in cnt:
                r=-1
                break
            else: r+= cnt[c]
        res.append(r)
    
    return res