days = int(input())
prices = sorted([int(x) for x in input().split()])
prices = [str(x) for x in prices]
order = ''
action = ''
if days == 1:
    print(prices[0])
    print("E")
else:
    for i in range(days//2):
        order += prices[i] + " " + prices[days-i-1] + " "
        action += "BS"
    if days%2 == 1:
        order += prices[days//2]
        action += "E"
    else:
        order = order[:-1]
    print(order)
    print(action)