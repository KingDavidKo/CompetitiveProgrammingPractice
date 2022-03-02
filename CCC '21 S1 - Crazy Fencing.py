N = int(input())
height = input().split()
width = input().split()
area = 0

for i in range(N):
    area += (int(height[i])+int(height[i+1]))*0.5*int(width[i])

print(area)