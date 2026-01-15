import sys
input = sys.stdin.readline

arr = input().strip()
res = set()
length = len(arr)

for i in range(1, length + 1):
    for j in range(length - i + 1):
        res.add(arr[j:j + i])
print(len(res))