def solution(today, terms, privacies):
    today=list(map(int, today.split('.')))
    todays=today[0]*28*12 + today[1]*28 + today[2]
    
    terms_dict={}
    for term in terms:
        k, v = term.split()
        terms_dict[k] = int(v)*28
    
    res=[]
    for idx, pri in enumerate(privacies, start=1):
        date, term = pri.split()
        date = list(map(int,date.split('.')))
        days = date[0]*28*12 + date[1]*28 + date[2] + terms_dict[term] - 1
        if days < todays: res.append(idx)
    
    return res