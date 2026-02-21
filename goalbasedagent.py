import random

class Vaccum:
    def __init__(self,roomsize=(10,10)):
        self.roomsize=roomsize
        rows,cols=self.roomsize
        self.grid = [[random.randint(0,1)for _ in range(cols)]for _ in range(rows)]
        self.current_position = (random.randrange(rows),random.randrange(cols))
        self.pastmove = []
    
    def display(self):
        print(" positon of vaccum cleaner" , self.current_position)
        for rows in self.grid:
            print(' '.join(map(str,rows)))
            print()
    
    def run(self):
        print("Initial Room State:")
        self.display()
    

    def move(self):
        r,c = self.current_position
        self.pastmove.append((r,c))
        if r+1 < len(self.grid) and self.grid[r+1][c] == 1 and (r+1,c) not in self.pastmove:
            new_r = r+1
            new_c = c
        elif r-1 >= 0 and self.grid[r-1][c] == 1 and (r-1,c) not in self.pastmove:
            new_r = r-1
            new_c = c
        elif c+1 < len(self.grid[0]) and self.grid[r][c+1] == 1 and (r,c+1) not in self.pastmove:
            new_r = r
            new_c = c+1
        elif c-1 >= 0 and self.grid[r][c-1] == 1 and (r,c-1) not in self.pastmove:
            new_r = r
            new_c = c-1
        else:
            new_r = r
            new_c = c
        self.current_position = (new_r,new_c)
        return self.current_position
    def clean(self):
        r,c=self.current_position
        if self.grid[r][c]==1:
            self.grid[r][c]=0
            print(f"Cleaned position: {self.current_position}")
agent = Vaccum()
agent.run()
for _ in range(20):
    agent.clean()
    agent.move()
agent.run()