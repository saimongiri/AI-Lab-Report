class waterjug:
    
    def __init__(self,xcapacity,ycapacity):
        self.xcapacity=xcapacity
        self.ycapacity=ycapacity
    
    def min(self,d,f):
        if d<f:
            return d
        else:
            return f
    
    def successor(self,n):
        x=0
        y=0
        step=0
        print("\tVessel A \t Vessel B \t Steps")
        print()
        while x!=n:
            if x==0:
                x=self.xcapacity
                step=step+1
                print("Fill x")
                self.display(x,y,step)
            elif y == self.ycapacity :
                y=0
                step=step+1
                print("Empty Y")
                self.display(x,y,step)
            else:
                temp = self.min(self.ycapacity-y,x)
                y=y+temp
                x=x-temp
                step=step+1
                print("pour in X in Y")
                self.display(x,y,step)
        return step
        
    def display(self,a,b,step):
            print("\t"+str(a)+"\t"+str(b)+"\t"+str(step))
            print()

n = int(input("Enter the liters(GOAL) of water required to be filled in Vessel 1:"))
xcap=int(input("Enter the capacity of the first vessel:"))
ycap=int(input("Enter the capacity of the second vessel:"))
agent = waterjug(xcapacity=xcap,ycapacity=ycap)
steps = agent.successor(n)
print("Steps required:",steps)
