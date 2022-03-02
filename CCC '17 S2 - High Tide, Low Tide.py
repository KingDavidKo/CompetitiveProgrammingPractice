import math

N = int(input())
tide = list(map(int,input().split()))
tide.sort()
lowtide = tide[:math.ceil(N/2)]
hightide = tide[math.ceil(N/2):]
measurments = []

for i in range(int(N/2)):
    measurments.append(lowtide[math.ceil(N/2-i-1)])
    measurments.append(hightide[i])

if N%2 == 1:
    measurments.append(lowtide[0])

print(*measurments)