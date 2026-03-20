import math
def solution(numer1, denom1, numer2, denom2):
    if denom1 == denom2:
        gcd = math.gcd(numer1 + numer2, denom1)
        return (numer1 + numer2) // gcd, denom1 // gcd
    else:
        answer_numer = numer1 * denom2 + numer2 * denom1
        answer_denom = denom1 * denom2
        gcd = math.gcd(answer_numer, answer_denom)
        return answer_numer // gcd, answer_denom // gcd