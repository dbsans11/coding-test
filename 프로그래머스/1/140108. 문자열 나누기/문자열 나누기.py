def solution(s):
    eq,diff,cur,res=0,0,s[0],0
    for c in s:
        if eq==diff: res,eq,diff,cur=res+1,0,0,c
        
        if c==cur: eq+=1
        else:diff+=1
    return res