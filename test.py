import time as t
import math

angle=45
velocity=14.008
vx=math.cos(math.radians(angle))*velocity
vy=math.sin(math.radians(angle))*velocity
time=0
y=0
x=0
dt=0.1
done=False

while done==False:
    print("\033[2J\033[H", end="")
    x=vx*time
    y=vy*time - 0.5*9.81*time**2
    intx=int(x)
    inty=int(y)
    time=time+dt
    for j in range(12):
        for i in range(136):
            if i == intx and (11-j) == inty:
                print("*", end="")
            else:
                if i == 135:
                    print(" ")
                else:
                    print(" ",  end="")

    print("|  |", end="")
    for i in range(1, 89):
        if i%4==1:
            print(" ", end="")
        elif i%4==2:
            print("|", end="")
        elif i%4==3:
            print("_", end="")
        elif i%4==0:
            print("|", end="")
    
    print("\n|__|")
    if y<0 and time > dt:
        done=True
    else:
        print("\033[H", end="")
        t.sleep(0.2)


