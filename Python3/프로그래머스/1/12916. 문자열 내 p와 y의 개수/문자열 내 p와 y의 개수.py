def solution(s):
    p, y = 0, 0
    for i in range(len(s)):
        if s[i] in 'pP':
            p += 1
        elif s[i] in 'yY':
            y += 1
    if p != y:
        return False
    return True