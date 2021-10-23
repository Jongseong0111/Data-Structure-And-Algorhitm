# https://programmers.co.kr/learn/courses/30/lessons/42587

# My Solution

from collections import deque

def solution(priorities, location):
    result = [(priorities[i], i) for i in range(len(priorities))]

    queue = deque(result)
    queue2 = []

    index = 0
    while queue:
        a = queue.popleft()
        if not queue:
            queue2.append(a)
            break
        if a[0] >= max(queue)[0]:
            queue2.append(a)
        else:
            queue.append(a)

    for i in range(len(queue2)):
        if queue2[i][1]==location:
            answer = i+1
            break
    return answer

# Other Solution

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer