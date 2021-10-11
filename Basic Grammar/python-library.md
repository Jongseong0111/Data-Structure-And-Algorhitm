> 자주 사용되는 주요 라이브러리의 문법과 유의할 점에 대해 추가로 알아봅니다. 표준 라이브러리란 특정 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리입니다. Python 표준 Library는 [공식문서](https://docs.python.org/ko/3/library/index.html)에서 확인할 수 있습니다.

> **본문 내용은 `이것이 코딩 테스트다 with 파이썬` 도서를 참고하였습니다.**

## 내장 함수

> Python에는 별도 import 명령어 없이 바로 사용할 수 있는 Built-in 함수가 존재합니다. 대표적으로 `input()`, `print()`가 내장함수에 속하며, 나머지 유용한 내장함수를 알아보겠습니다.

### sum()

> List와 같은 Iterable 객체가 입력으로 주어진 경우 모든 원수의 합을 반환합니다.

```python
# sum()
result = sum([1,2,3])
print(result) # output: 6
```

### min(), max()

> Parameter가 2개 이상 들어왔을 때 가장 작은 값과 큰 값을 반환합니다.

```python
# min(), max()
list = [1,2,3,4,5]
print(min(list), max(list)) # output: 1 5
```

### eval()

> 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환합니다.

```python
# eval()
result = eval("(3+5)*7")
print(result) # output: 56
```

### sorted()

> Iterable 객체가 들어왔을 때 정렬된 결과를 반환합니다. Key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬 결과를 뒤집을 지 여부를 결정할 수 있습니다.

```python
# Tuple의 2번째 원소 기준으로 내림차순 정렬(lambda 사용)
list = [('a', 1), ('b', 3), ('c', 2)]
sorted(list, key = lambda x: x[1], reverse=True)
print(list) # output: [('b', 3), ('c', 2), ('a', 1)]
```

## Itertools

> Python에서 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리입니다. **순열과 조합**(Permutations, Combinations)를 다룰 경우 유용하게 사용됩니다.

```python
# permutations(순열) - r개의 Data를 뽑아 일렬로 나열하는 모든 경우를 제시
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 3개의 데이터를 나열하는 모든 경우의 수
print(result) # output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations(조합) - r개의 Data를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 제시
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개의 데이터를 뽑는 모든 경우의 수
print(result) # output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product - 중복을 허용하는 permutations
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개의 데이터를 뽑는 모든 순열(중복 허용)
print(result) # output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]


# combinations_with_replacement - 중복 원소를 허용하는 combinations
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 경우의 수(중복 허용)
print(result) # output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

```

## heapq

> Python에서는 Heap 기능을 위해 heapq 라이브러리를 제공합니다. heapq는 다양한 알고리즘에서 **우선순위 큐를 구현**하기 위해 사용됩니다. Python의 heap은 최소 heap으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣은 후 빼는 것 만으로도 **O(NlogN)의 시간복잡도**로 오름차순 정렬이 완료됩니다.

```python
# 최소 힙 구현
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 List에 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 2, 4, 8, 6])
print(result) # output: [1, 2, 3, 4, 5, 6, 7, 8]

# 최대 힙 구현(원소의 부호를 임시로 변경)

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 List에 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 2, 4, 8, 6])
print(result) # output: [8, 7, 6, 5, 4, 3, 2, 1]
```

## bisect

> Python에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리르 제공합니다. bisect 라이브러리는 **정렬된 배열에서 특정 원소를 찾을 때 매우 효과적**으로 사용됩니다.

- bisect_left(a, x) : 정렬된 순서를 유지하면서 List a에 Data x를 삽입할 가장 왼쪽 index를 찾는 Method
- bisect_right(a, x) : 정렬된 순서를 유지하면서 List a에 Data x를 삽입할 가장 오른쪽 index를 찾는 Method

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x)) # output: 2
print(bisect_right(a, x)) # output: 4

# 특정 범위에 속하는 원소의 개수 구하기
def count_by_range(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index

# 값이 4인 원소의 개수 출력
print(count_by_range(a, 4, 4) # output: 2

# 값이 [1, 4] 범위의 원소의 개수 출력
print(count_by_range(a, 1, 4) # output: 4
```

## collections

> Python의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리입니다. **deque와 counter** 클래스가 아주 유용하게 사용됩니다.

```python
# deque의 사용법
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) # data = deque([1, 2, 3, 4])
data.append(5)     # data = deque([1, 2, 3, 4, 5])
data.popleft()     # data = deque([2, 3, 4, 5])
data.pop()         # data = deque([2, 3, 4])
```

deque에서는 List와 다르게 Indexing, Slicing은 사용할 수 없지만 원소의 삽입이나 제거에서 **시간복잡도가 O(1)**이기 때문에 **Stack이나 Que 자료구조의 대용**으로 사용이 가능합니다. 예를 들어 Que 자료구조로 사용하고자 할때, 원소를 삽입할 경우는 `append()`를 사용하고 원소를 삭제할 경우 `popleft()`를 사용하면 먼저 들어온 원소가 항상 먼저 나가게 됩니다.(First in First Out)

```python
# counter의 사용법
from collections import Counter

# iterable 객체가 주어진 경우 해당 객체 내부의 원소별 등장 횟수를 세는 기능
counter = Counter(['red', 'blue', 'blue', 'green', 'blue', 'red'])
print(counter['blue']) # output: 3
```

## math

> math 라이브러리는 **자주 사용되는 수학적 기능을 포함**하고 있는 라이브러리입니다. 팩토리얼, 제곱근, 최대공약수 등을 계산하는 기능을 포함하여 수학적 계산을 요구하는 경우 효과적으로 사용이 가능합니다.

```python
import math

# Factorial
print(math.factorial(5)) # output: 120

# 제곱근 계산
print(math.sqrt(7)) # output: 2.6457513110645907

# 최대 공약수
print(math.gcd(21, 14)) # output: 7

# 원주율, 자연상수 e
print(math.pi, math.e) # output: 3.141592653589793 2.718281828459045
```
