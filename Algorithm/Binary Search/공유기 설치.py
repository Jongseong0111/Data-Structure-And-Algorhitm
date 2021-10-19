# https://www.acmicpc.net/problem/2110

# My Solution

# 공유가 시이 거리를 이진탐색으로 좁혀서 구현

n, m = map(int, input().split())

num = []

for _ in range(n):
  j = int(input())
  num.append(j)

num.sort()

result = 0
start = 1
end = num[n-1]-num[0]

while start<=end:
  count = 1
  mid = (start+end)//2

  value = num[0]
  for i in range(1, len(num)):
    if num[i]>=value+mid:
      value = num[i]
      count += 1
  
  if count >= m:
    start = mid+1
    result = mid
  else:
    end = mid-1

print(result)