# 이코테 2021 - Ch.15 이진탐색 Q.28

# My Solution

# 가운데 값과 인덱스를 비교

n = int(input())

num = list(map(int, input().split()))

def point(array, start, end):
  if start>end:
    return -1
  mid = (start+end)//2
  if array[mid]==mid:
    return mid
  if array[mid] > mid:
    return point(array, start, mid-1)
  if array[mid] < mid:
    return point(array, mid+1, end)

print(point(num, 0, n-1))
