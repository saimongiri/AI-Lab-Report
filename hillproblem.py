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

def hill_climbing(start):
    current = start

    while True:
        h_current = heuristic(current)

        if current == GOAL:
            print("Solved!")
            return

        neigh = neighbors(current)
        best = min(neigh, key=heuristic)
        h_best = heuristic(best)

        if h_best >= h_current:
            print("Stopped (Local Optimum)")
            return

        current = best


start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

hill_climbing(start)