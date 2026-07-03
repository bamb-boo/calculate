import time
import math

angle=45
velocity=14.008
vx=math.cos(math.radians(angle))
vy=math.sin(math.radians(angle))
time=0
y=0
x=0
dt=0.1
done=False

print("\033[2J", end="")

while done==False:
    x=x+vx*time
    y=y+vy*time - 0.5*9.81*time**2
    if y==0:
        done=True

print("\033[H", end="")

empty=[]
for i in range(12):
    row=[]
    for j in range(136):
        row.append(" ")
    empty.append(row)

col=x*4+4
rows=11-y*2




print("  *")
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

