import math
from turtle import *

def hearta(k):
    return 7 * math.sin(k) ** 3  

def heartb(k):
    return 6 * math.cos(k) - 2.5 * math.cos(2 * k) - 1 * math.cos(3 * k) - 0.5 * math.cos(4 * k)  

screen = Screen()
screen.setup(width=400, height=600) 

speed(0)
bgcolor("black")
color("#f73487")
width(2)

up()
goto(hearta(0) * 20, heartb(0) * 20)  
down()

for i in range(1, 6000):
    goto(hearta(i) * 20, heartb(i) * 20)  

goto(0, 0)
done()
