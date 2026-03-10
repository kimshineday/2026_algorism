find = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(6):
        answer.append(chess[i] - find[i])
print(*answer)