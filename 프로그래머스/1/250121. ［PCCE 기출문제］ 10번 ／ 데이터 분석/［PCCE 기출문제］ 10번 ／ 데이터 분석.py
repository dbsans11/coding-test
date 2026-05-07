def solution(data, ext, val_ext, sort_by):
    idx = {"code":0,"date":1,"maximum":2,"remain":3}
    ext,sort_by=idx[ext],idx[sort_by]
    return sorted([r for r in data if r[ext]<val_ext],key=lambda x:x[sort_by])