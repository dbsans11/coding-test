def solution(arr,k):
    return (t:=list(dict.fromkeys(arr)))[:k] +([-1]*(k-len(t)) if len(t)<k else [])