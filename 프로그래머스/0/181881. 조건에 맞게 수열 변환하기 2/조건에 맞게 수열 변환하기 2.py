def solution(arr):
    cnt,temp,l = -1,[],len(arr)
    while temp!=arr:
        temp=arr[:]
        for i in range(l):
            if arr[i]>=50 and arr[i]%2==0: arr[i]//=2
            elif arr[i]<50 and arr[i]%2: arr[i]=arr[i]*2+1
        cnt+=1
    return cnt