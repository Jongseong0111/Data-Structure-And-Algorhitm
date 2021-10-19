# https://www.acmicpc.net/problem/1715

# My Solution

# 우선순위 큐를 사용하여 시간복잡도 최소화

import heapq
import sys

n = int(input())
card = []
for _ in range(n):
  j = sys.stdin.readline().rstrip()
  heapq.heappush(card, int(j))
answer = 0
while card:
  a = heapq.heappop(card)
  if not card:
    break
  b = heapq.heappop(card)

  answer += a+b
  heapq.heappush(card, a+b)

print(answer)