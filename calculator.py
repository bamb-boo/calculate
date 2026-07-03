import math
from math import sin, cos, tan, pi
list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "*", "/", ".", "sin", "cos", "tan", "pi", "equals"]
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evaluate=""
choices=[]
done=False
velocity= 14.008 # set it to 14.69081 later

while done==False:
    angle=float(input("enter the angle "))
    angle=math.radians(angle)
    distance=((velocity**2)*math.sin(2*angle))/9.81
    if 0 <= math.degrees(angle)< 1.3:
        choice=0
    else:
        choice=list[math.floor(distance)-1]
    print(choice)
    choices.append(choice)
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


ordinary differential equation-
dy/dt and dx/dt
horizontal = previous position + velocity_x*time
vertical = previous position + velocity_y*time - 0.5*9.81*time^2

velocty_x and velocity_y using sin and cos of angle and velocity (line 8)
                                         
          *                               
         * *                               
        *   *                              
       *     *                             
      *       *                            
----|     |\  */\   /\   /\   /\   /\   /
    |     | \_/  \_/  \_/  \_/  \_/  \_/ 
    |     |
    |     |
    ______


                                         
                                          
                                           
            *                                    
         *     *                            
       *         *                          
----|     |\   /\   /\   /\   /\   /\   /
    |     | \_/  \_/  \_/  \_/  \_/  \_/ 
    |     |
    |     |
    ______
