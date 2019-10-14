#name:Kathryn McCullough
#email: kathryn.mccullough1@marist.edu
#description: traffic light with functions (in order to compct code and reduce copying)




from graphics import *

#set width and length of screen
win = GraphWin('traffic_light',400,400)

#draw the light body> xy coordinates of left corner + length and width
def draw_light_body(x, y, l, w):
    rect= Rectangle (Point(x,y), Point(l,w))
    rect.setOutline("black")
    rect.setWidth(4)
    rect.setFill("white")
    rect.draw(win)
    
#draw the light lamps> xy(ab) coordinates of center + radius of circle+ color of light
def draw_lamp(a,b,radius,color):
    light=Circle (Point (a,b), radius)
    light.setFill(color)
    light.setOutline ("black")
    light.setWidth(3)
    light.draw(win)

#entire function with arguments> xy coordinates of left corner (ssame as body)
#don't need to end the previous functions but end the main function
def draw_traffic_light(x,y):
    draw_light_body(x, y, 90, 150)
    draw_lamp(60, 35, 20, "red")
    draw_lamp(60, 80, 20, "yellow")
    draw_lamp(60, 125, 20, "green")
    
draw_traffic_light(30, 10)
