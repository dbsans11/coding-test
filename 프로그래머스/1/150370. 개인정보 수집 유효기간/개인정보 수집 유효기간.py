def solution(today, terms, privacies):
    today,terms_dict,res=list(map(int,today.split('.'))),{},[]
    for t in terms:
        k,v=t.split()
        terms_dict[k]=int(v)
    
    for i,p in enumerate(privacies,start=1):
        date,term=p.split()
        date=list(map(int,date.split('.')))
        date[1]+=terms_dict[term]
        date[2]-=1
        
        if date[2]<1: 
            date[1]-=1
            date[2]=28
        
        if date[1]>12:
            temp,date[1]=divmod(date[1],12)
            date[0]+=temp
        
        if date[1]<1:
            date[1]=12
            date[0]-=1
        
        if date<today: res.append(i)
    
    return res