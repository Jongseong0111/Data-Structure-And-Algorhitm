# https://www.acmicpc.net/problem/14501

# My Solution

n = int(input())

schedule = [0]
for i in range(n):
  te, pe = map(int, input().split())
  schedule.append([te,pe])

result = [0]*(n+2)
m = n
max_value = 0

while m>=1:
  [t,p] = schedule[m]
  if m + t <= n+1:
    if t == 1:
      result[m] = result[m+1]+p
    else:
      for i in range(1,t):
        result[m] =  max(result[m+t]+p, max_value)
        max_value = result[m]
  else:
    result[m]=max_value
  m-=1

print(max_value)