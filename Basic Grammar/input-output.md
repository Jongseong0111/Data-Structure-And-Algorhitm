> Python은 문법이 간결하면서도 다루기 쉬운 언어로 알고리즘을 구현할 때도 다른 언어(C/C++/Java)에 비해서 코드가 짧은 편입니다. 이곳에서는 코딩 테스트에서 중요한 Python 문법 위주로 다루었습니다.

알고리즘 문제 풀이의 첫 단계는 데이터를 입력받는 것입니다. 알고리즘을 수행할 수 있는 로직을 작성했다 해도 데이터의 입력이 적절하지 않다면 잘못된 결과를 출력할 것입니다.

> **본문 내용은 `이것이 코딩 테스트다 with 파이썬` 도서를 참고하였습니다.**

## Python 입출력

> Python에서 데이터를 입력받을 때 `input()`을 사용합니다. `input()`은 한 줄의 문자열을 입력받도록 해주고, 정수형으로 변환하기 위해 `int()` 함수를 사용해야 합니다.

```python
# 데이터의 개수 입력
n = int(input()) # input: 5
print(n) # output: 5

# 2개의 데이터를 공백으로 구분하여 입력
n, m = input().split() # input: 데이터 공백
print(n, m) # output: 데이터 공백

# 2개의 데이터를 공백으로 구분하여 정수형으로 변환
n, m = map(int, input().split()) # input: 5 7
print(n, m) # output: 5 7

# 각 데이터를 공백으로 구분하여 List로 입력
data = list(map(int, input().split())) # input: 5 6 7 8
data.sort(reverse=True)
print(data) # output: [8, 7, 6, 5]
```

> 입력의 개수가 많은 경우 단순 `input()` 함수를 그대로 사용하지 않고 Python의 sys 라이브러리를 사용합니다.

```python
import sys

# 문자열을 한 줄 입력받기
data = sys.stdin.readline().rstrip() # input: Hello World
print(data) # output: Hello World
# rstrip() 함수를 호출하여 줄 바꿈 공백 문자를 제거합니다.
```
