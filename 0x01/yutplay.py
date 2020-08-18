for i in range(3):
    a,b,c,d = map(int, input().split())
    res = a + b + c + d
    if res ==3:
        print("A")
    elif res ==2:
        print("B")
    elif res == 1:
        print("C")
    elif res == 4:
        print("E")
    else:
        print("D")