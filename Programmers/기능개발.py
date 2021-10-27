# https://programmers.co.kr/learn/courses/30/lessons/42586

# My Solution

def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        if (100-progress)%speed == 0:
            days.append((100-progress)//speed)
        else:
            days.append(((100-progress)//speed)+1)
    standard = days[0]
    num = 1
    answer = []
    for i in range(1, len(days)):
        if standard >=  days[i]:
            num+=1
        else:
            standard = days[i]
            answer.append(num)
            num = 1
    answer.append(num) 
            
    return answer