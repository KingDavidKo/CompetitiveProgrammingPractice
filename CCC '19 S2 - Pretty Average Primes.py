T = int(input())
import math
N = 0
def isPrime(a):
    for i in range(2, math.floor(a**0.5)+1):
        if a%i == 0:
            return False
    return True

for i in range(T):
    N = int(input())
    if N%2 == 0:
        a = N + 1
        b = N - 1
    else:
        a = N
        b = N
    while b >= 3:
        if isPrime(a) and isPrime(b):
            print(str(b) + " " + str(a))
            break
        a += 2
        b -= 2