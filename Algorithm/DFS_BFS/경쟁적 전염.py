# https://www.acmicpc.net/problem/18405

# My Solution

# Key = 값이 0인 경우 상하좌우에 방문한 적이 없으면서 값이 0이 아닌 값 중 최소값을 삽입

n, k = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

s, index_x, index_y = map(int, input().split())

visited = [[False]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs (graph, x, y):
  virus = 1e9
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
      if graph[nx][ny]!=0 and not visited[nx][ny]:
        virus = min(virus, graph[nx][ny])
  graph[x][y] = virus if virus!=1e9 else 0
  visited[x][y] = True

for k in range(s):
  visited = [[False]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j]==0:
        dfs(graph,i,j)
  if graph[index_x-1][index_y-1]!=0:
    break
answer = graph[index_x-1][index_y-1]
print(answer)