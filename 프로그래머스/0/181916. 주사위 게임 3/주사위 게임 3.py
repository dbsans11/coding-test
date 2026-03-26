def solution(a,b,c,d):
    dset=set((a,b,c,d))
    if (l:=len(dset)) == 1: return 1111*a
    if l==4: return min(a,b,c,d)
    cnt, dset = {k:(a,b,c,d).count(k) for k in dset}, list(dset)
    if l==2:
        if max(cnt.values())==3:
            if cnt[dset[0]]==3: return (10*dset[0]+dset[1])**2
            else: return (10*dset[1]+dset[0])**2
        else: return (dset[0]+dset[1]) * abs(dset[0]-dset[1])
    else: 
        q,r = [k for k,v in cnt.items() if v==1]
        return q*r