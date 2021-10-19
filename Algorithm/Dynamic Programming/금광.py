# 이코테 2021 - Ch.16 다이나믹 프로그램 Q.31

# My Solution

# 금광의 위치에서 왼쪽 위, 왼쪽, 왼쪽 아래에서 최대인 값을 더하면 각 위치에서 최대값이 된다.

t = int(input())

case = []
for k in range(t):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  testcase = []
  for i in range(n):
    sample=[]
    for j in range(m):
      sample.append(array[i*m+j])
    testcase.append(sample)
  case.append(testcase)

def gold(array):
  n = len(array)
  m = len(array[0])
  answer = 0
  for i in range(1, m):
    for j in range(n):
      if j==0:
        array[j][i] += max(array[j][i-1], array[j+1][i-1])
      elif j==n-1:
        array[j][i] += max(array[j][i-1], array[j-1][i-1])
      else:
        array[j][i] += max(array[j][i-1], array[j-1][i-1], array[j+1][i-1])
      if i==m-1:
        answer = max(answer, array[j][i])

  return answer

for i in range(t):
  print(gold(case[i]))
        
