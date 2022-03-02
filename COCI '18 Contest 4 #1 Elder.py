owner = input()
N = int(input())
winners = []
losers = []
count = 1
for i in range(N):
    duel = input().split()
    winners.append(duel[0])
    losers.append(duel[1])
visited = set()
visited.add(owner)
for i in range(N):
    if owner == losers[i]:
        owner = winners[i]
    if owner not in visited:
        count += 1
        visited.add(owner)

print(owner)
print(count)