from itertools import combinations
def solution(nums):
    e,r=[0,0]+[1]*2999,0
    for i in range(2,3001):
        if e[i]: e[i*i:3001:i]=[0]*len(range(i*i,3001,i))
    for v in combinations(nums,3): r+=e[sum(v)]
    return r