# https://www.acmicpc.net/problem/10825

# My Solution

# Tuple의 sort는 index 순서대로 적용됩니다.

n = int(input())
score = []
for i in range(n):
  a, b, c, d = input().split()
  score.append((-int(b), int(c), -int(d), a))
score.sort()

for i in range(n):
  print(score[i][3])