from cs1graphics import *

class Heart() :
    def __init__(self, x, y):
        heart = Layer()
        
        leftell = Ellipse(10,9,Point(x,y))
        leftell.setFillColor('red')
        leftell.setBorderWidth(0)
        #leftcir.setDepth(10)
        heart.add(leftell)
        
        rightell = Ellipse(10,9,Point(x+10,y))
        rightell.setFillColor('red')
        rightell.setBorderWidth(0)
        #rightcir.setDepth(10)
        heart.add(rightell)
        
        bottom = Polygon(Point(0,0),Point(20,0),Point(10,10))
        bottom.moveTo(x-5, y+1)
        bottom.setFillColor('red')
        bottom.setBorderWidth(0)
        #bottom.setDepth(10)
        heart.add(bottom)
        
        self.layer = heart
        

class Robot_shape():
    def __init__(self,x,y) :
        robot = Layer()

        head = Polygon(Point(0,0),Point(25,0),Point(25,20),Point(0,20))
        head.setFillColor((84,105,128))
        head.setBorderWidth(0)
        robot.add(head)

        eye1 = Rectangle(4,4,Point(6,9))
        eye1.setFillColor('yellow')
        eye1.setBorderWidth(0)
        robot.add(eye1)

        eye2 = Rectangle(4,4,Point(19,9))
        eye2.setFillColor('yellow')
        eye2.setBorderWidth(0)
        robot.add(eye2)

        body = Polygon(Point(3,20),Point(22,20),Point(22,30),Point(3,30))
        body.setFillColor((84,105,128))
        body.setBorderWidth(0)
        robot.add(body)

        arm1 = Polygon(Point(2,20),Point(7,20),Point(7,27),Point(2,27))
        arm1.setFillColor((120,145,173))
        arm1.setBorderWidth(0)
        robot.add(arm1)

        arm2 = Polygon(Point(19,20),Point(24,20),Point(24,27),Point(19,27))
        arm2.setFillColor((120,145,173))
        arm2.setBorderWidth(0)
        robot.add(arm2)

        leg1 = Polygon(Point(6,30),Point(11,30),Point(11,35),Point(6,35))
        leg1.setFillColor((120,145,173))
        leg1.setBorderWidth(0)
        robot.add(leg1)

        leg2 = Polygon(Point(14,30),Point(19,30),Point(19,35),Point(14,35))
        leg2.setFillColor((120,145,173))
        leg2.setBorderWidth(0)
        robot.add(leg2)
        
        self.layer = robot
        self.layer.moveTo(x,y)
        
                
class Bomb() :
    def __init__(self) :
        bomb = Layer()
        
        body = Circle(14)
        body.setFillColor((35,35,35))
        body.setBorderWidth(0)
        body.setDepth(10)
        bomb.add(body)

        shiny = Circle(4)
        shiny.setFillColor('white')
        shiny.setBorderWidth(0)
        shiny.setDepth(5)
        shiny.move(-5,-3)
        bomb.add(shiny)
        
        spark = Polygon(Point(2,2), Point(5,3), Point(7,1), Point(8,4),Point(11,4),Point(8,6),Point(8,9),Point(6,7), Point(3,8),Point(4,6))
        spark.setFillColor('red')
        spark.setBorderWidth(0)
        spark.move(-3,-23)
        spark.setDepth(10)
        spark.scale(1.8)
        bomb.add(spark)
        
        self.layer = bomb

class Item() :
    def __init__(self) : 
        item = Layer()
        
        body = Circle(8)
        body.setFillColor('yellow')
        body.setBorderWidth(0)
        body.setDepth(15)
        item.add(body)
        
        small = Circle(5)
        small.setFillColor((255,201,14))
        small.setBorderWidth(0)
        small.setDepth(13)
        item.add(small)
        
        self.layer = item
        