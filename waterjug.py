class waterjug:
    
    def __init__(self,xcapacity,ycapacity):
        xcapacity=self.xcapacity
        ycapacity=self.ycapacity
    
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
                display(x,y,step)
            elif y == self.ycapacity :
                y=0
                step=step+1
                print("Empty Y")
                display(x,y,step)
            else:
                temp = min(self.ycapacity-y,x)
                y=y+temp
                x=x-temp
                step=step+1
                print("pour in X in Y")
                display(x,y,step)
            return step
        
        def display(self,a,b,s):
            print("\t"+a+"\t"+b+"\t"+step)
            print()

n = int(input("Enter the liters(GOAL) of water required to be filled in Vessel 1:"))
xcap=int(input("Enter the capacity of the first vessel:"))
ycap=int(input("Enter the capacity of the second vessel:"))
agent = waterjug(xcap,ycap)
steps = agent.successor(n)
print("Steps required:"+steps)