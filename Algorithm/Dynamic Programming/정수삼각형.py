# https://www.acmicpc.net/problem/2110

# My Solution

# 현재 위치의 위, 왼쪽위 중 최대값을 더한다.

n = int(input())

triangle = []
for i in range(n):
  num = list(map(int, input().split()))
  triangle.append(num)

for i in range(1, n):
  for j in range(i+1):
    if j==0:
      triangle[i][j] += triangle[i-1][j]
    elif j==i:
      triangle[i][j] += triangle[i-1][j-1]
    else:
      triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
print(max(triangle[n-1]))
    