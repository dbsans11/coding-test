def solution(players, callings):
    ranks = {k:v for v, k in enumerate(players)}
    for call in callings:
        players[idx], players[idx-1] = (pre:=players[(idx:=ranks[call])-1]), players[idx]
        ranks[call], ranks[pre] = ranks[pre], ranks[call]
    return players
        