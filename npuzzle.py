GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Find blank position
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next states
def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


# BFS Algorithm
def solve_puzzle(start):
    queue = [start]      
    visited = []         

    while queue:
        current = queue.pop(0)   

        if current == GOAL:
            print("Solved!")
            return

        visited.append(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    print("No solution found")


# start state
start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]

solve_puzzle(start_state)