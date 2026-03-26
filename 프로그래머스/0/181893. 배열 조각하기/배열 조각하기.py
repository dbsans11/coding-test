def solution(arr, qu):
    for i,q in enumerate(qu): arr = arr[q:] if i%2 else arr[:q+1]
    return arr