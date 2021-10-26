# https://programmers.co.kr/learn/courses/30/lessons/42626

# My Solution

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
        
    answer = 0
    while scoville:
        a = heapq.heappop(scoville)
        if a > k:
            break
        if scoville:
            b = heapq.heappop(scoville)
        else:
            return -1

        c = a+2*b
        heapq.heappush(scoville, c)
        answer+=1

    return answer