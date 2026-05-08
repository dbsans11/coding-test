def solution(wal):
    r=[51,51,-1,-1]
    for row_idx,row in enumerate(wal):
        for col_idx,col in enumerate(row):
            if col=='#': r=[min(r[0],row_idx),min(r[1],col_idx),max(r[2],row_idx+1),max(r[3],col_idx+1)]
    return r
            