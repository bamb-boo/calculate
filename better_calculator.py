import time as t
import math
from math import sin, cos, tan, pi
import ast
import operator as op
num_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "sin", "cos", "tan", "pi", "equals"]
simple_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "s", "c", "t", "π", "="]
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evaluate=""
choices=[]
done=False
velocity= 14.008 # set it to 14.69081 later
dt=0.1

def evall(expression):
    operator={
        ast.Add:op.add,
        ast.Sub:op.sub,
        ast.Mult:op.mul,
        ast.Div:op.truediv,
        ast.USub:op.neg
    }

    var={
        "pi":math.pi,
        "sin":math.sin,
        "cos":math.cos,
        "tan":math.tan
    }

    def actualeval(thing):
        if isinstance(thing, ast.Constant):
            return thing.value
        
        if isinstance(thing, ast.Name):
            return var[thing.id]
        
        if isinstance(thing, ast.BinOp):
            return operator[type(thing.op)](actualeval(thing.left), actualeval(thing.right))

        if isinstance(thing, ast.UnaryOp):
            return operator[type(thing.op)](actualeval(thing.operand))

        if isinstance(thing, ast.Call):
            arg=actualeval(thing.args[0])
            return var[thing.func.id](arg)
        
    tree=ast.parse(expression, mode="eval")
    return actualeval(tree.body)

while done==False:
    time=0
    y=0
    x=0
    seconddone=False
    places=[]
    angle=float(input("enter the angle "))
    angle=math.radians(angle)
    vx=math.cos(angle)*velocity
    vy=math.sin(angle)*velocity

    distance=((velocity**2)*math.sin(2*angle))/9.81
    if 0 <= math.degrees(angle)< 1.3:
        choice=0
    else:
        choice=num_list[math.floor(distance)-1]
    print(choice)

    choices.append(choice)
        
    while seconddone==False:
        print("\033[3J\033[2J\033[H", end="")
        x=vx*time 
        y=vy*time - 0.5*9.81*time**2
        intx=round(x*4)
        inty=int(y*2)
        final = (y<0 and time>0)
        place=[intx, inty]
        places.append(place)

        frames=[]
        for j in range(12):
            row=""
            for i in range(136):
                if not final and i == intx and (11-j)==inty:
                    row=row+"*"
                else:
                    row=row+" "
            frames.append(row)

        divide = "|  |"
        for i in range(20):
            divide=divide+" | |"
        frames.append(divide)

        hole="|  |"
        if final:
            target=math.floor(distance)-1
        else:
            target=intx//4

        for i in range(20):
            if final and i==target:
                hole=hole+" |*|"
            else:
                hole=hole+" |_|"
        frames.append(hole)
        value="|__| "
        for i in range(len(simple_list)-1):
            value=value+f" {simple_list[i]}  "
        value=value+" ="
        frames.append(value)

        print("\n".join(frames))

        if final:
            seconddone = True
        else:
            time=time+dt
            t.sleep(0.1)

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

temp=""
for i, char in enumerate(evaluate):
    if i>0 and char.isalpha() and (evaluate[i-1].isdigit() or evaluate[i-1]==")"):
        temp=temp+"*"
    temp=temp+char
evaluate=temp
evaluate=evaluate.replace("+*", "+").replace("-*", "-").replace("**", "*").replace("/*", "/") #check if other things need to be replaced

print(evaluate)

answer=evall(evaluate)
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

