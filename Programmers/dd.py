# https://programmers.co.kr/learn/courses/30/lessons/85002

# My Solution 

def solution(weights, head2head):
  result = []
  answer = []

  for i in range(len(weights)):
    win_less = 0
    win_more = 0
    lose = 0
    fight = False
    win_rate = 0
    for j in range(len(weights)):
      if head2head[i][j]=='W':
        fight = True
        if weights[j]>weights[i]:
          win_more += 1
        else: 
          win_less +=1
      elif head2head[i][j]=='L':
        fight = True
        lose +=1
    if fight:
      win_rate = (win_less+win_more)/(win_less+win_more+lose)
    result.append([win_rate, win_more, weights[i], i])

  for i in range(len(result)):
    for j in range(i, 0, -1):
      if result[j][0] > result[j-1][0]:
        result[j], result[j-1] = result[j-1], result[j]
      elif result[j][0] == result[j-1][0]:
        if result[j][1] > result[j-1][1]:
          result[j], result[j-1] = result[j-1], result[j]
        elif result[j][1] == result[j-1][1]:
          if result[j][2] > result[j-1][2]:
            result[j], result[j-1] = result[j-1], result[j]
          elif result[j][2] == result[j-1][2]:
            if result[j][2] < result[j-1][2]:
              result[j], result[j-1] = result[j-1], result[j]
            else: 
              break
          else:
            break
        else:
          break
      else:
        break
  [answer.append(i[3]+1) for i in result]
  return answer

# Other Solution - Sort()

def solution(weights, head2head):
    result = []
    l = len(weights)
    # 한 번에 정렬해서 풀어봅시다!
    ans = [[0 for _ in range(4)] for _ in range(l)] # 승률, 무거운복서 이긴횟수, 자기 몸무게, 번호(음수로)
    for i in range(l):
        ans[i][2] = weights[i]
        ans[i][3] = -(i+1)
        cnt = 0 # 판수
        for j in range(l):
            if head2head[i][j] == 'W':
                ans[i][0] += 1 # 일단 이김
                cnt += 1
                if weights[i] < weights[j]:
                    ans[i][1] += 1 # 무거운 복서 이김
            elif head2head[i][j] == 'L':
                cnt += 1 # 판수만 늘려준다
        if cnt == 0:
            ans[i][0] = 0
        else:
            ans[i][0] /= cnt
    ans.sort(reverse=True) # 역순으로 정렬하면 모든 조건이 한 번에 정렬된다

    for i in range(l):
        result.append(-ans[i][3])
    return result

# Other Solution - lambda Expression
def solution(weights, head2head):
    person = []
    for i, head in enumerate(head2head):
        person.append(
            (
                head.count("W") / (len(head) - head.count("N")) if head.count("N") != len(head) else 0,
                sum(1 for j, h in enumerate(head) if h == "W" and weights[i] < weights[j]),
                weights[i],
                i + 1
            )
        )
    return list(list(zip(*sorted(person, key=lambda x: (-x[0], -x[1], -x[2], x[3]))))[3])