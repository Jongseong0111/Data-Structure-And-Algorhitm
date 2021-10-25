# https://programmers.co.kr/learn/courses/30/lessons/49191

# My Solution

def solution(n, results):
    # index를 번호로 가진 선수에 대해 그 선수가 이긴 선수들의 set, 진 선수들의 set을 초기화
    board = [[set(), set()] for _ in range(n+1)]

    # 경기결과가 들어올 때 마다 선수들의 이기고 진 정보를 업데이트 (모든 선수에 대해)
    for result in results:
        # result = [4,3]인 경우
        # 4번이 이긴 선수 목록에 3번을 추가
        board[result[0]][0].add(result[1])
        # 4번이 이긴 선수 목록에 3번이 이긴 선수 목록을 추가 (3번이 이긴 선수라면 4번이 이길 수 있으므로)
        board[result[0]][0] = board[result[0]][0] | board[result[1]][0]
        # 4번이 진 선수들의 목록에 3번과 3번이 이긴 선수목록을 새롭게 추가 (4번에게 이긴 선수라면 3번도 이기므로)
        for i in list(board[result[0]][1]):
            board[i][0].add(result[1])
            board[i][0] = board[i][0] | board[result[1]][0]

        # 마찬가지로 3번이 진 선수 목록에 4번을 추가
        board[result[1]][1].add(result[0])
        # 3번이 진 선수 목록에 4번을 이긴 선수 목록 추가 (4번에게 이긴 선수라면 3번도 이기므로)
        board[result[1]][1] = board[result[1]][1] | board[result[0]][1]
        # 3번이 이긴 선수들의 목록에 4번과 4번을 이긴 선수를 업데이트 (3번에게 진 선수라면 4번에게도 지므로)
        for i in list(board[result[1]][0]):
            board[i][1].add(result[0])
            board[i][1] = board[i][1] | board[result[0]][1]
            
    answer = 0
    # 순위를 알기 위해서 자신이 이기고 진 선수들의 합이 n-1 이어야 한다.
    for i in range(n+1):
        if len(board[i][0]) + len(board[i][1]) == n-1:
            answer+=1

    return answer