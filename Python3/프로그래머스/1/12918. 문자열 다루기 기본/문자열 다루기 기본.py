def solution(s):
    if len(s) not in (4, 6): # len(s) != 4 and len(s) != 6
        return False
    else:
        for i in range(len(s)):
            if s[i] not in '1234567890':
                return False
        return True
