J = int(input())
A = int(input())
sizes = []
request = []
success = 0

for i in range(J):
    sizes.append(input())

for i in range(A):
    for i in input().split():
        request.append(i)

for i in range(A):
    if sizes[int(request[2*i+1])-1] <= request[2*i]:
        sizes[int(request[2*i+1])-1] = "Z"
        success += 1

print(success)