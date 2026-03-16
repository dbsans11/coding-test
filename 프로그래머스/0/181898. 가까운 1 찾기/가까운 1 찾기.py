def solution(arr, idx):
    for i, v in enumerate(arr[idx:]):
        if v: return i+idx
    return -1