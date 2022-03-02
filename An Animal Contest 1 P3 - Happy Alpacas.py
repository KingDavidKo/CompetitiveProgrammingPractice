result = ''
N, X = map(int, input().split(" "))

if (N-X)%2 == 0:

    for i in range(X):
        result += "0"
    for i in range(N-X):
        if i%2 == 0:
            result += "1"
        else:
            result += "0"
    print(" ".join(result))
else:
    print("-1")