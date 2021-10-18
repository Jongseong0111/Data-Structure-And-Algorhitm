# https://programmers.co.kr/learn/courses/30/lessons/42889

# My Solution

def solution(N, stages):
    answer = []

    a = [0]*(N+2)
    for i in stages:
        a[i]+=1

    users = len(stages)
    score = []
    for i in range(1,N+1):
        if users == 0:
            score.append((0,i))
        else:
            score.append((-(a[i]/users), i))
            users-=a[i]

    score.sort()
    for i in score:
        answer.append(i[1])

    return answer