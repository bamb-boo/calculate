import time as t
import math
from math import sin, cos, tan, pi
list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "sin", "cos", "tan", "pi", "equals"]
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evaluate=""
choices=[]
done=False
velocity= 14.008 # set it to 14.69081 later
time=0
y=0
x=0
dt=0.1
seconddone=False

while done==False:
    angle=float(input("enter the angle "))
    vx=math.cos(math.radians(angle))*velocity
    vy=math.sin(math.radians(angle))*velocity

    distance=((velocity**2)*math.sin(2*angle))/9.81
    if 0 <= math.degrees(angle)< 1.3:
        choice=0
    else:
        choice=list[math.floor(distance)-1]
    print(choice)

    choices.append(choice)
        
    while seconddone==False:
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
        
        print("\n|  |",  end="")
        for i in range(22):
            print(" |_|", end="")
        print("\n|__|")
        if y<0 and time > dt:
            seconddone=True
        else:
            print("\033[H", end="")
            t.sleep(0.2)
    if choice=="equals":
        done=True

brackets=0
for i in range(len(choices)-1):
    value=choices[i]
    if value in ["+", "-", "*", "/"]:
        if brackets>0:
            evaluate=evaluate + ")"
            brackets-=1
        evaluate=evaluate+str(value)
    elif value in ["sin", "cos", "tan"]:
        evaluate=evaluate+str(value)+"("
        brackets+=1
    else:
        evaluate=evaluate+str(value)

evaluate=evaluate+(")"*brackets)
evaluate=evaluate.replace("sin", "*sin").replace("cos", "*cos").replace("tan", "*tan").replace("pi", "*pi")
evaluate=evaluate.replace("+*", "+").replace("-*", "-").replace("**", "*").replace("/*", "/") #check if other things need to be replaced

print(evaluate)

answer=eval(evaluate)
print(answer)




'''things to do next
add a cannonball-like animation (maybe terminal maybe tkinter) to show ball being launched at angle and following the path through air and falling into "buckets"
'''


'''
30
12
20
7
17
33
3
45
'''

