N = int(input())
answers = []
count = 0
for i in range(2*N):
    answers.append(input())

for i in range(N):
    if answers[i] == answers[i+N]:
        count += 1

print(count)
