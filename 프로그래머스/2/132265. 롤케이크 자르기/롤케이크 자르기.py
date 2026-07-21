def solution(topping):
    a1, a2 = set(), {}
    for tp in topping:
        if tp not in a2:
            a2[tp] = 1
        else:
            a2[tp] += 1
    
    cnt = 0
    for tp in topping:
        a1.add(tp)
        a2[tp] -= 1
        if a2[tp] == 0:
            a2.pop(tp)
        cnt += (len(a1)==len(a2))
    
    return cnt