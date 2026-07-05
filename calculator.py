import time as t
import math
from math import sin, cos, tan, pi
list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "sin", "cos", "tan", "pi", "equals"]
simple_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "s", "c", "t", "π", "="]
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evaluate=""
choices=[]
done=False
velocity= 14.008 # set it to 14.69081 later
dt=0.1

while done==False:
    time=0
    y=0
    x=0
    seconddone=False
    angle=float(input("enter the angle "))
    angle=math.radians(angle)
    vx=math.cos(angle)*velocity
    vy=math.sin(angle)*velocity

    distance=((velocity**2)*math.sin(2*angle))/9.81
    if 0 <= math.degrees(angle)< 1.3:
        choice=0
    else:
        choice=list[math.floor(distance)-1]
    print(choice)

    choices.append(choice)
        
    while seconddone==False:
        print("\033[3J\033[2J\033[H", end="")
        x=vx*time
        y=vy*time - 0.5*9.81*time**2
        intx=round(x*4)
        inty=int(y*2)
        time=time+dt
        final = (y<0 and time>dt)
        for j in range(12):
            for i in range(136):
                if not final and i == intx and (11-j) == inty:
                    print("*", end="")
                else:
                    if i == 135:
                        print(" ")
                    else:
                        print(" ", end="")

        print("|  |", end="")
        for i in range(1, 81):
            if i%4==1:
                print(" ", end="")
            elif i%4==2:
                print("|", end="")
            elif i%4==3:
                print(" ", end="")
            elif i%4==0:
                print("|", end="")
        
        print("\n|  |",  end="")
        if final:
            target=math.floor(distance)-1
        else:
            target=intx//4

        for i in range(20):
            if final and i==target:
                print(" |*|", end="")
            else:
                print(" |_|", end="")


        print("\n|__|", end="")

        for i in range(len(simple_list)-1):
            print(f"  {simple_list[i]} ",  end="")

        print(" = ")


        if final:
            seconddone = True
        else:
            t.sleep(0.1)



    if choice=="equals":
        done=True
    else:
        seconddone=False

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

