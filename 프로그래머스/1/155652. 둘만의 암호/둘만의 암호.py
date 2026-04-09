def solution(s,skip,idx):
    alp='abcdefghijklmnopqrstuvwxyz'.translate(str.maketrans('','',skip))
    dic,l={v:i for i,v in enumerate(alp)},len(alp)
    return ''.join([alp[(dic[c]+idx)%l] for c in s])