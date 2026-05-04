from collections import Counter
def solution(X, Y):
    X,Y,r=Counter(X),Counter(Y),''
    for k in X.keys()&Y.keys():
        r+=(k*min(X[k],Y[k]))
    return ''.join(sorted(r,reverse=1)) if r.strip('0') else '0' if r else '-1'