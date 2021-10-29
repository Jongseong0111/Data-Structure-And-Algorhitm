# https://programmers.co.kr/learn/courses/30/lessons/81302

# My Solution - depth 2 만큼 확인

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(place, x, y):
    n = len(place)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n:
            if place[nx][ny]== "P":
                return False
            elif place[nx][ny]=="O":
                for j in range(4):
                    if j != (i+2)%4:
                        mx = nx + dx[j]
                        my = ny + dy[j]
                        if 0 <= mx < n and 0 <= my < n:
                            if place[mx][my]=="P":
                                return False
    return True
  
def solution(places):
    answer = []
    n = len(places)
    for place in places:
        result = 1
        for i in range(n):
            for j in range(n):
                if place[i][j]=='P':
                    if not check(place, i, j):
                        result = 0
        answer.append(result)

    return answer

# Other Solution

import numpy as np

def isvalid(p):
    q = []

    p = np.array([list(x) for x in p])
    for y, x in zip(*np.where(p == 'P')):
        q.append((y, x, y, x, 0))    # (y, x, 시작'P'y, 시작'P'x, 거리)

    while q:
        y, x, sy, sx, d = q.pop(0)

        if d < 2:
            for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
                if -1 < ny < 5 and -1 < nx < 5 and (ny, nx) != (sy, sx):
                    if p[ny, nx] == 'P': return 0
                    elif p[ny, nx] == 'O': q.append((ny, nx, sy, sx, d+1))

    return 1

def solution(places):
    return [isvalid(p) for p in places]
