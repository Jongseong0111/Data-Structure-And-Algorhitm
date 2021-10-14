# https://programmers.co.kr/learn/courses/30/lessons/60059

# My Solution

# 1. 자물쇠를 가운데에 위치하여 3x3 Matrix 구현
# 2. Key를 [0, 0]부터 이동하며 새 배열의 원소와 합
# 3. 자물쇠 위치의 모든 값이 1이면 True, 아니면 False
# 4. 자물쇠를 90도 돌려 4가지 경우에 대해 시행

def rotate(key):
    key_after = [[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            key_after[j][len(key)-1-i] = key[i][j]
    print(key_after)
    return key_after

def check(box):
    box_length = len(box)//3
    for i in range(box_length, box_length*2):
        for j in range(box_length, box_length*2):
            if box[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    box = [[0]*m*3 for _ in range(3*m)]
    
    for i in range(m):
        for j in range(m):
            box[i+m][j+m] = lock[i][j]
    
    for rota in range(4):
        key = rotate(key)
        for i in range(m*2):
            for j in range(m*2):
                for k in range(n):
                    for l in range(n):
                        box[i+k][j+l] += key[k][l]
                if check(box)==True:
                    return True
                for k in range(n):
                    for l in range(n):
                        box[i+k][j+l] -= key[k][l]
                        
    return False