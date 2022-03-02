T = int(input())

for i in range(T):
    a, b, c = map(int, input().split())
    if (a + b*2 + c*3)%2 == 1:
        print("NO")
    elif a < c:
        print("NO")
    elif (a-c)%2 == 0 and a > 0:
        print("YES")
    elif b%2 == 1:
        print("NO")
    else:
        print("YES")