def solution(today, terms, privacies):
    def date_to_int(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y*28*12 + m*28 + d
    
    answer = []
    today = date_to_int(today)
    
    term_dict = {}
    for term in terms:
        k, v = term.split()
        term_dict[k] = int(v)*28
    
    for i, pri in enumerate(privacies, start=1):
        date, term = pri.split()
        date = date_to_int(date) + term_dict[term]
        
        if today >= date:
            answer.append(i)
    
    return answer