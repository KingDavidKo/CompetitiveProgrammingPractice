N = int(input())
a = int(N**0.5)+1
def prime(N,a):
    if N == 1:
        return 2
    if N == 2:
        return 2
    if N == 3:
        return 3
    if N%2 == 0:
        N += 1
    while True:
        for i in range(3,a):
            if N%i == 0:
                N+=2
                break
            if i == a-1:
                return N

print(prime(N,a))