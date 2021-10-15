# https://www.acmicpc.net/problem/3190

# My Solution

def snake(n, apple, arrows):
  # 사과 위치, 시간에 따른 방향전환 리스트 생성
  vector = [[0, 1], [-1, 0], [0, -1], [1, 0]]
  # 앞, 뒷 좌표 초기화
  front = [0, 0]
  back = [0, 0]
  # 보드 초기화 - 1은 뱀이 차지하는 공간
  snake = [[0]*n for _ in range(n)]
  snake[0][0] = 1
  # 앞, 뒷 좌표 방향 변수와 시간 // x,y 는 시간
  x, y = 0, 0
  directionx, directiony = 0, 0
  # 게임 종료 시간
  answer = 0
  while True:
    # 시간 x를 확인해 방향전환 유무 확인, 존재하면 방향전환
    for arrow in arrows:
      if arrow[0] == x:
        if arrow[1] == 'L':
          directionx  = (directionx+1)%4
        elif arrow[1]=='D':
          directionx = (directionx-1)%4
    # 앞좌표 이동 후 x 증가
    front[0]+=vector[directionx][0]
    front[1]+=vector[directionx][1]
    x += 1
    # 벽에 막히면 시간 기록 후 나가기
    if front[0] < 0 or front[0] > n-1 or front[1] < 0 or front[1] > n-1:
      answer = x
      break
    # 몸통이랑 부딪히면 시간 기록 후 나가기
    elif snake[front[0]][front[1]]==1:
      answer = x
      break
    # 사과 없으면 뒷좌표 비우고 전진 후 y 증가
    if front not in apple:
      for arrow in arrows:
        if arrow[0] == y:
          if arrow[1] == 'L':
            directiony  = (directiony+1)%4
          elif arrow[1]=='D':
            directiony = (directiony-1)%4
      snake[back[0]][back[1]]=0
      back[0]+=vector[directiony][0]
      back[1]+=vector[directiony][1]
      y += 1
    # 앞좌표 1 채우기
    else:
      apple.remove(front)
    snake[front[0]][front[1]]=1
  return answer

n = int(input())
k = int(input())
apple = []
arrows = []
for _ in range(k):
  a, b = map(int, input().split())
  apple.append([a-1, b-1]) # 사과 위치(1행 1열 -> [0, 0])
l = int(input())
for _ in range(l):
  a, b = input().split()
  arrows.append([int(a), b]) # [시간, 방향전환 문자]]

print(snake(n, apple, arrows))