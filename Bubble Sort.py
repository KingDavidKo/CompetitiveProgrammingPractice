N = int(input())
sort = []
temp1 = input().split(" ")
for i in range(N):
    sort.append(int(temp1[i]))

temp = 0
j = 0
print(*sort)
for j in range(N-1):
    for i in range(N-j-1):
        if sort[i] > sort[i+1]:
            temp = sort[1+i]
            sort[1+i] = sort[i]
            sort[i] = temp
            print(*sort)