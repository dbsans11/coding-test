def solution(c1, c2, g):
    i1,i2,l1,l2=0,0,len(c1),len(c2)
    for c in g:
        if i1<l1 and c1[i1]==c: i1+=1
        elif i2<l2 and c2[i2]==c: i2+=1
        else: return "No"
    return "Yes"