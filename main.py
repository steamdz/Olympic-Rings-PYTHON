#AYMEN DEV 
#Olympic Rings-شعار الالمبياد

from turtle import *

speed(1)
setup(600, 500)
pensize(8)

# Black Ring
pencolor("black")
circle(70)

# Blue Ring
penup()
goto(-180, 0)
pendown()
pencolor("blue")
circle(70)

# Red Ring
penup()
goto(180, 0)
pendown()
pencolor("red")
circle(70)

# Yellow Ring
penup()
goto(-88, -80)
pendown()
pencolor("yellow")
circle(70)

# Green Ring
penup()
goto(88, -80)
pendown()
pencolor("green")
circle(70)

mainloop()
