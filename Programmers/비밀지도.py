# https://programmers.co.kr/learn/courses/30/lessons/17681

# My Solution

def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        e = ''
        string = ''
        for c, d in zip(bin(2**n+a)[3:], bin(2**n+b)[3:]):
            e+=str(int(c)|int(d))
        for i in e:
            string += ' #'[int(i)] 
        answer.append(string)
        print(answer)
    return answer

# Other Solution

def solution(n, *maps):
    return [line(n, a | b) for a, b in zip(*maps)]

def line(n, x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])