def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        repeat = my_string[i] * n
        answer += repeat
    return answer