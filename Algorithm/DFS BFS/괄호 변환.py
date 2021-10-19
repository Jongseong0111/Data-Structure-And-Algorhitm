# https://programmers.co.kr/learn/courses/30/lessons/60058

# My Solution

def solution(p):
    string = p
    print(string)
    if string=='':
      return ''
    if string[0]=='(':
        a, b = 1, 0
    elif string[0]==')':
        a, b = 0, 1
    index = 1
    while a!=b:
        if string[index]=='(':
            a+=1
        elif string[index]==')':
            b+=1
        index+=1
    u = string[:index]
    v = string[index:]
    if u[0]=='(':
        return u + solution(v)
    elif u[0]==')':
        c = ''
        if len(u)>2:
            for i in u[1:-1]:
                if i=='(':
                    c+=')'
                else:
                    c+='('
        return '('+solution(v)+')'+c