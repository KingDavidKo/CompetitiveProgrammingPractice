import sys
input = sys.stdin.readline
direction = ''
instruction = input()
while instruction != '99999\n':
    add = int(instruction[0])+int(instruction[1])
    steps = str((instruction[2:5]))
    if add == 0:
        print(direction + steps)
    elif add%2==0:
        direction = 'right '
        print(direction + str(steps))
    else:
        direction = 'left '
        print(direction + str(steps))
    instruction = input()