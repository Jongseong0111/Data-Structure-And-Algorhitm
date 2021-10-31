# https://programmers.co.kr/learn/courses/30/lessons/72411

# My Solution

from itertools import combinations

def solution(orders, course):
    answer = []
    # Course에 담겨있는 숫자만큼 조합을 담기 위해 result 생성
    result = [{} for _ in range(len(course))]
    c = set()
    for order in orders:
        a = sorted(list(order))
        for i in range(len(course)):
            b = set(combinations(a, course[i]))
            for j in b:
                if j in c:
                    result[i][j] +=1
                else:
                    result[i][j] = 1
                    c.add(j)

    for i in range(len(result)):
        # 숫자마다 조합 중 2개 이상의 가장 많이 나온 조합을 문자열 형태로 answer에 추가
        [answer.append(''.join(k)) for k,v in result[i].items() if max(result[i].values()) == v and v>=2] 

    answer.sort()
    return answer

# Other Solution

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]