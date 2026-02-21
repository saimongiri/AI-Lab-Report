GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def heuristic(state):
    d = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                d += abs(i-x) + abs(j-y)
    return d

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_zero(state)
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    result = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<3 and 0<=ny<3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)
    return result

def solve(start):
    open_list = [(start, 0)]   # (state, g)
    closed = []

    while open_list:
        # choose state with minimum f = g + h
        current, g = min(open_list, key=lambda x: x[1] + heuristic(x[0]))
        open_list.remove((current, g))

        if current == GOAL:
            print("Solved!")
            return

        closed.append(current)

        for n in neighbors(current):
            if n not in closed:
                open_list.append((n, g+1))

    print("No solution")

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

solve(start)