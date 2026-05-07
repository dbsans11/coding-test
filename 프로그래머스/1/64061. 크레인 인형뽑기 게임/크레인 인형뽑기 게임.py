def solution(board, moves):
    board,st,n = [[v for v in row if v] for row in zip(*board[::-1])],[],0
    for m in moves:
        if board[m-1]:
            t=board[m-1].pop()
            if not st or st[-1]!=t: st.append(t)
            else:
                st.pop()
                n+=2
    return n