# https://programmers.co.kr/learn/courses/30/lessons/12973

# My Solution

from collections import deque

def solution(s):
    a = []
    for i in s:
        if not a:
            a.append(i)
            continue
        if a[-1]==i:
            a.pop()
        else:
            a.append(i)
    
    return 1 if not a else 0