import heapq


n, m = map(int, input().split())
INF = int(1e9)
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

h = []

heapq.heappush(h, (0, start))

distance[start] = 0

while h:
  node = heapq.heappop(h)
  if distance[node[1]]<node[0]:
    continue
  
  for i in graph[node[1]]:
    cost = node[0]+i[1]
    if cost < distance[i[0]]:
      distance[i[0]]=cost
      heapq.heappush(h, (cost, i[0]))

for i in range(n+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])
