def support(state, block):
    s = []
    while block != "Table":
        s.append(block)
        block = state[block]
    return s

def heuristic(state, goal):
    score = 0
    for block in state:
        if support(state, block) == support(goal, block):
            score += len(support(state, block))
        else:
            score -= len(support(state, block))
    return score


state = {'A': 'B', 'B': 'Table', 'C': 'Table'}
goal  = {'A': 'B', 'B': 'C', 'C': 'Table'}

print("Heuristic value:", heuristic(state, goal))