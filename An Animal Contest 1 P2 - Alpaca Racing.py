import sys
import math
input = sys.stdin.readline

def function():
    N, D, K, X = map(int, input().split(" "))
    speed = []
    for i in range(N):
        speed.append(int(input()))
    P = int(input())
    count = 0
    percentage = (100-X)/100


    for i in range(len(speed)):
        while P <= speed[i]:
            speed[i] = math.floor(speed[i]*percentage)
            count += 1
            if count > K:
                print("NO")
                return 0
    print("YES")
function()