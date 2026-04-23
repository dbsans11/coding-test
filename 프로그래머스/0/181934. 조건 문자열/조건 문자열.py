def solution(iq,eq,n,m):
    if iq=='<': return (n<=m)*1 if eq=='=' else (n<m)*1
    else: return (n>=m)*1 if eq=='=' else (n>m)*1