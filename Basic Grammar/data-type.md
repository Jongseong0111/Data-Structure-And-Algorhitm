> Python은 문법이 간결하면서도 다루기 쉬운 언어로 알고리즘을 구현할 때도 다른 언어(C/C++/Java)에 비해서 코드가 짧은 편입니다. 이곳에서는 코딩 테스트에서 중요한 Python 문법 위주로 다루었습니다.

알고리즘 풀이를 포함한 모든 프로그래밍은 결국 데이터를 다루므로, **자료형에 대한 이해는 근본적으로 매우 중요**하다고 할 수 있습니다. 파이썬의 자료형은 다른 언어에서 사용되는 기본 자료형을 제공할 뿐 아니라 Dictionary, Set 등 강력한 기능을 제공하는 자료형을 내장하고 있어 매우 편리합니다.

> **본문 내용은 `이것이 코딩 테스트다 with 파이썬` 도서를 참고하였습니다.**

## 수 자료형

### 정수형(Integer)

> 정수를 다루는 자료형으로 양의 정수, 음의 정수, 0이 있습니다. 

```python
a = 1000 # 양의 정수
print(a) # output: 1000

a = -7 # 음의 정수
print(a) # output: -7
```

### 실수형(Real Number)

> **소수점 아래의 데이터**를 포함하는 수 자료형으로, 변수에 **소수점을 붙인 수를 대입하면 실수형 변수**로 처리합니다. 소수부가 0이거나 정수부가 0인 소수는 0을 생략하고 작성할 수 있습니다. 

```python
# 양의 실수
a = 157.93
print(a) # output: 157.93

# 음의 실수
a = -83.2
print(a) # output: -83.2

# 소수부 0 생략
a = 5.
print(a) # output: 5.0

# 10억의 지수 표현 방식
a = 1e9
print(a) # output: 1000000000.0

# 752.5
a = 75.25e1
print(a) # output: 752.5
```
#### round()

현대 컴퓨터 시스템은 수 데이터를 처리할 경우 2진수를 이용하기 때문에 **실수 정보를 정확히 표현하는 데 한계**를 가집니다. 예를 들어 2진수 체계에서 0.9를 정확히 표현할 방법이 없습니다. 따라서 **소수점 값을 정확히 비교하는 작업이 필요하다면 round() 함수를 이용**할 수 있습니다.

```python
a = 0.3 + 0.6
print(a) # output: 0.89999999999
print(a==0.9) # output: False

a = 0.3 + 0.6
# round(a,4) // a는 실수형 데이터, 4는 (반올림 위치 -1)(5번째 자리에서 반올림)
print(round(a, 4)) # output: 0.9
```

### 수 자료형의 연산

> **사칙연산(+, -, X, /)를 사용해 계산**합니다. 추가적으로 몫(//)과 나머지(%) 연산자를 사용합니다. 나누기(/) 연산자는 기본적으로 실수형으로 결과를 처리하기 때문에 주의해주어야 합니다.

```python
a = 7
b = 3
print(a / b)  # output: 2.3333333333
print(a % b)  # output: 1
print(a // b) # output: 2
print(a ** b) # output: 343
```

## List 자료형

> List는 **여러 개의 데이터를 연속적으로 처리**하기 위해 사용합니다. append(), remove() 등의 메소드를 지원합니다.

### List 생성

```python
a = [1, 2, 3, 4, 5]

print(a) # output: [1, 2, 3, 4, 5]

# Index 4로 접근
print(a[4]) # output: 5

# 빈 리스트 선언
a = list() or []
print(a) # output: []

# 크기가 N인 리스트 초기화
n = 5
a = [0] * n
print(a) # output: [0, 0, 0, 0, 0]
```

### List Indexing & Slicing

> Index를 입력하여 List의 특정 원소에 접근하는 것을 Indexing, 연속적 위치의 원소를 가져오는 것을 Slicing이라 합니다. 

```python
a = [1, 2, 3, 4, 5]

# 뒤에서 첫 번째 원소 출력
print(a[-1]) # output: 9

# 세 번째 원소 변경
a[2] = 7
print(a) # output: [1, 2, 7, 4, 5]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4]) # output: [2, 7, 4]
```

### List Comprehension

> List Comprehension은 **리스트를 초기화하는 방법** 중 하나입니다. 대괄호([ ])안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있으며, 2차원 리스트를 초기화할 경우 효과적으로 사용됩니다.

```python
# 0부터 10까지 홀수만 포함하는 List
array = [i for i in range(10) if i % 2 == 1]
print(array) # output: [1, 3, 5, 7, 9]

# n x m 크기의 2차원 리스트 
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array) # output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# n x m 크기의 2차원 리스트(잘못된 방법)
# 내부적으로 리스트가 동일 객체에 대한 레퍼런스로 인식
array = [[0] * m] * n
array[1][1] = 5
print(array) # output: [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
```
### List Method

| Method  | 설명 | Big O Notation |
|:----------|:----------|:----------|
| append() |List에 원소를 하나 삽입합니다. | O(1) |
| sort() |기본 정렬 기능으로, 오름차순으로 정렬합니다. | O(NlogN) |
| reverse() |List 원소의 순서를 뒤집어놓습니다. | O(N) |
| insert() |특정 index에 원소를 삽입할 때 사용합니다. | O(N)|
| count(특정값) |List에서 특정 값을 가지는 데이터 개수를 셉니다. | O(N) |
| remove() |특정 값을 갖는 원소를 하나 제거합니다. | O(N) |

```python
a = [1, 4, 3]

# 원소 삽입
a.append(2)
print(a) # output: [1, 4, 3, 2]

# 오름차순 정렬
a.sort()
print(a) # output: [1, 2, 3, 4]

# 내림차순 정렬
a.sort(reverse=True)
print(a) # output: [4, 3, 2, 1]

# 원소 뒤집기
a.reverse()
print(a) # output: [1, 2, 3, 4]

# 특정 index에 date 추가
a.insert(2, 4)
print(a) # output: [1, 2, 4, 3, 4]

# 특정 값 데이터 개수
print(a.count(4)) # output: 2

# 특정 값 데이터 제거
a.remove(1)
print(a) # output: [2, 4, 3, 4]
```
> `insert()`의 시간복잡도는 O(N)이고 `append()`의 시간복잡도는 O(1)이기 때문에 `insert()`를 자주 사용하는 것은 좋지 않습니다. 마찬가지로 `reverse()`의 시간복잡도도 O(N)이기 때문에 모든 값을 제거하고자 한다면 다음과 같은 방법을 사용합니다.

```python
# 특정 값의 원소를 모두 제거하는 효율적인 방법

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# 3, 5로 remove()를 사용하는 것이 아니라 remove_set에 포함되지 않은 값을 저장
result = [i for i in a if i not in remove_set]
print(result) # output: [1, 2, 4]
```

## 문자열 자료형

### 문자열 초기화

> 문자열 변수의 초기화는 큰 따옴표(")나 작은 따옴표(')를 사용하고, 백슬래시(\)를 사용해 문자열 내부에 큰 따옴표나 작음 따옴표를 사용합니다.

```python
string = "Hello World"
print(string) # output: Hello World

string = "Say \"Hello World\""
print(string) # output: Say "Hello World"
```

### 문자열 연산
> 문자열 변수에 덧셈이나 곱셉으로 처리합니다. 파이썬의 문자열은 내부적으로 **리스트와 같이 처리**되어, 여러 개의 문자가 합쳐진 리스트라고 볼 수 있습니다. 따라서 문자열도 Indexing과 Slicing이 가능합니다.

```python
# 문자열 덧셈
a = "Hello"
b = "World"
print(a + " " + b) # output: Hello World

# 문자열 곱셈
a = "String"
print(a*3) # output: StringStringString

# Slicing
a = "ABCDEF"
print(a[2:4]) # output: CD

