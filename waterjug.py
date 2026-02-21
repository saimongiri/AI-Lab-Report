class Waterjug:
    def __init__(self,intial_state,goal_state):
        self.intial_state= intial_state
        jug_A, jug_B = self.intial_state

    def goalTest(current_state,goal_state):
        if current_state == goal_state :
            return 1
        else:
            return 0
    def production(self):
        if self.current_position and self.jug_A<4 : # This is to fill water in Jug A
            self.current_position = (4,self.jug_B)
        elif self.current_position and self.jug_B<3: # This is to fill water in Jug B
            self.current_position = (self.jug_A,3)
        elif self.current_position and self.jug_A == 4:
            self