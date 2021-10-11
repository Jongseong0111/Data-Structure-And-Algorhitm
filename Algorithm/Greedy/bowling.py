# 이코테 2021 - Chapter 11 그리디 알고리즘 - 05 볼링공 고르기

from collections import Counter

# 볼링공 개수 n과 최대 무게 m
n, m = map(int, input().split())

# 각 볼링공의 무게 list
data = list(map(int, input().split()))

result = 0
counter = Counter(data)
# 첫 사람이 고르는 볼링공의 무게 value
for value in data:
  # 두번째 사람은 무게가 value가 아닌 볼링공을 고를 수 있음
  result += n - counter[value]

# (i, j), (j, i)와 같이 경우의 수가 두 번 계산되므로 반으로 출력
print(int(result/2))