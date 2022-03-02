t = int(input())
maze = []
path = []
tempArray = []
count = 1
x = 0
y = 0

def wayFinder(maze, r, c, x, y, path, count):
    if x<0 or y<0 or x>c or y>r:
        return 0
    if count<path[y][x]:
        path[y][x] = count
    else:
        return 0
    if x == c and y == r:
        return 0
    if maze[y][x] == "-":
        if x == 0:
            wayFinder(maze, r, c, x+1, y, path, count+1)
        elif x == c:
            wayFinder(maze, r, c, x-1, y, path, count+1)
        else:
            wayFinder(maze, r, c, x+1, y, path, count+1)
            wayFinder(maze, r, c, x-1, y, path, count+1)
    elif maze[y][x] == "|":
        if y == 0:
            wayFinder(maze, r, c, x, y+1, path, count+1)
        elif y == r:
            wayFinder(maze, r, c, x, y-1, path, count+1)
        else:
            wayFinder(maze, r, c, x, y+1, path, count+1)
            wayFinder(maze, r, c, x, y-1, path, count+1)
    elif maze[y][x] == "+":
        if x == 0:
            wayFinder(maze, r, c, x+1, y, path, count+1)
        elif x == c:
            wayFinder(maze, r, c, x-1, y, path, count+1)
        else:
            wayFinder(maze, r, c, x+1, y, path, count+1)
            wayFinder(maze, r, c, x-1, y, path, count+1)

        if y == r:
            wayFinder(maze, r, c, x, y-1, path, count+1)
        elif y == 0:
            wayFinder(maze, r, c, x, y+1, path, count+1)
        else:
            wayFinder(maze, r, c, x, y+1, path, count+1)
            wayFinder(maze, r, c, x, y-1, path, count+1)

    if maze[y][x] == "*":
        return 0

for i in range(t):
    r = int(input())
    c = int(input())
    path = []
    for j in range(r):
        for i in range(c):
            tempArray.append(100000000)
        path.append(tempArray)
        tempArray = []
    for i in range(r):
        temp = input()
        for char in temp:
            tempArray.append(char)
        maze.append(tempArray)
        tempArray = []

    r -= 1
    c -= 1
    wayFinder(maze, r, c, x, y, path, count)
    if path[r][c] == 100000000:
        print(-1)
    elif maze[r][c] == "*":
        print(-1)
    else:
        print(path[r][c])
    path = []
    maze = []