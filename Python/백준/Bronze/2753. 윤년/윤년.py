leap = int(input())

if leap % 400 == 0:
    print(1)
elif leap % 100 != 0:
    if leap % 4 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)