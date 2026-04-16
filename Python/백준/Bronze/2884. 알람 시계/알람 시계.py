H, M = map(int, input().split())
early = 45
if M < early:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = (60+M) - early
else:
    M -= early
print(f'{H} {M}')