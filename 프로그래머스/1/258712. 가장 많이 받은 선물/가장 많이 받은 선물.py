from itertools import combinations

def solution(friends, gifts):
    friend_map, gift_rate, res = {k:{} for k in friends}, {k:0 for k in friends}, {k:0 for k in friends}
    for gift in gifts:
        A, B = gift.split()
        friend_map[A][B] = friend_map[A].get(B, 0) + 1
        gift_rate[A]+=1
        gift_rate[B]-=1
    
    for A, B in combinations(friends,2):
        if (a:=friend_map[A].get(B,0))!=(b:=friend_map[B].get(A,0)):
            res[A if a>b else B]+=1
        else:
            if gift_rate[A]!=gift_rate[B]:
                res[A if gift_rate[A] > gift_rate[B] else B]+=1
    
    return max(res.values())
            
    