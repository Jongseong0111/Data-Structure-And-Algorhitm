# 이코테 2021 - Chapter 05 DFS/BFS - 미로탈출
# BFS

from collections import deque

graph = []
n, m = map(int, input().split())
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 1
x, y = 0, 0
queue = deque([(x, y)])
while queue:
  (x,y) = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <0 or nx > n-1 or ny < 0 or ny > m-1:
      continue
    if graph[nx][ny]==1:
      queue.append((nx, ny))
      graph[nx][ny] = graph[x][y]+1

print(graph[n-1][m-1])