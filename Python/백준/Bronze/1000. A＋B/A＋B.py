# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
def sum_num(A, B):
    return(A + B)
    
A, B = map(int, input().split())
print(sum_num(A, B))