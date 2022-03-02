N = int(input())
a = []
cost = 0
temp = 0

for i in range(N):
    temp = int(input())
    cost += temp
    a.append(temp)

a.sort(reverse = True)

for i in range(int(N/3)):
    cost -= a[2+i*3]

print(cost)