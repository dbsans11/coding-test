def solution(i,e,n,m):
    if i=="<": return (n<=m if e=="=" else n<m)*1
    else: return (n>=m if e=="=" else n>m)*1