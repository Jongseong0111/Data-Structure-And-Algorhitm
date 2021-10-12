# https://programmers.co.kr/learn/courses/30/lessons/60057

# My Solution

def solution(n):
    result = ''
    answer = 99999
    # 문자열 길이가 1개인 경우 
    if len(n) == 1:
        return 1
    for i in range(1, len(n)):
        index = i
        key = n[:i]
        string = ""
        num = 1
        while True:
            # 문자열 길이가 초과되는 경우
            if index + i > len(n) and index >= len(n):
                if num == 1:
                    string += key
                else:
                    string += str(num) + key
                string += n[index:]
                break
            # 반복 문자열이 같은 경우
            if key == n[index:(index+i)]:
                num += 1
            # 반복 문자열이 다른 경우 압축문자열에 추가
            else:
                if num == 1:
                    string += key
                else:
                    string += str(num) + key
                key = n[index:(index+i)]
                num = 1
            index += i
        answer = min(len(string), answer)
    return answer

# Other Solution - Use zip function

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])