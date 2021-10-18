# 선택 정렬 - 가장 작은 데이터를 맨 앞으로 가져오는 것을 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i],array[min_index]

print(array)

# 삽입 정렬 - 특정 데이터를 적절 위치에 삽입

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): # i 부터 1까지 감소하며 반복
    if array[j] < array[j-1]: # 자기보다 크면 위치 변경
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작으면 멈춤
      break
  
print(array)

# 퀵 정렬 - pivot 기준으로 왼쪽은 나보다 작고 오른쪽은 나보다 큰 것들 모음

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):

  if len(array)<=1:
    return array
  pivot = array[0]
  tail = array[1:]

  left = [x for x in tail if x<=pivot]
  right = [x for x in tail if x>pivot]
  return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(array))

# 계수 정렬 - 데이터 최대값으로 리스트를 초기화한 후 모두 삽입(간편)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]*(max(array)+1) # 최대값+1 로 리스트 선언

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=" ")