def solution(wal):
    r,c=[],[]
    for row_idx,row in enumerate(wal):
        for col_idx,col in enumerate(row):
            if col=='#':
                r.extend([row_idx, row_idx+1])
                c.extend([col_idx, col_idx+1])
    return [min(r),min(c),max(r),max(c)]
            