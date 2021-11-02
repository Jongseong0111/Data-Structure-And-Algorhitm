# https://programmers.co.kr/learn/courses/30/lessons/43238

# My Solution

def solution(n, times):
    y = n*max(times)
    x = 0
    answer = 0
    while True:
        sum = 0
        mid = (x+y)//2
        for time in times:
            sum += mid//time
        if sum >= n:
            y = mid
        else:
            x = mid+1
        if x==y:
            answer = x
            break
    return answer