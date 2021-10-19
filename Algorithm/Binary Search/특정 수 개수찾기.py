# 이코테 2021 - Ch.15 이진탐색 Q.27

# My Solution

# 특정 수의 가장 왼쪽 인덱스와 오른쪽 인덱스를 따로 구현

n, x = map(int, input().split())

num = list(map(int, input().split()))

def first(array, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  if num[mid]==target and mid==0:
    return 0
  if num[mid] == target and mid!=0:
    if num[mid-1] == num[mid]:
      return first(array, target, start, mid-1)
    else:
      return mid
  if num[mid] > target:
    return first(array, target, start, mid-1)
  if num[mid] < target:
    return first(array, target, mid+1, end)

def right(array, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  if num[mid]==target and mid==n-1:
    return n-1
  if num[mid] == target and mid!=n-1:
    if num[mid+1] == num[mid]:
      return right(array, target, mid+1, end)
    else:
      return mid
  if num[mid] > target:
    return right(array, target, start, mid-1)
  if num[mid] < target:
    return right(array, target, mid+1, end)

def count_x(array, x):
  n = len(array)
  first_index = first(num, x, 0, n-1)

  if first_index==None:
    return -1
  right_index = right(num, x, 0, n-1)

  answer = right_index+1-first_index
  return answer

print(count_x(num, x))
