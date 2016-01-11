from cs1graphics import *
from time import *
import random
import math

from shape import *

width = 300
height = 400
paper = Canvas(width, height)
paper.setBackgroundColor((192,166,255))

end_flag = 0

class idle(EventHandler) : 
    def __init__(self,setting,robot,bombs,items):
        EventHandler.__init__(self)
        self.robot = robot
        self.bombs = bombs
        self.setting = setting
        self.items = items
        self.clock = 0
                
    def handle(self,event):
        self.clock += 1
        
        # move bombs
        for i in range(len(self.bombs.container)) :
            for j in range(len(self.bombs.container[i])) :
                self.bombs.container[i][j].layer.move(0,20)
                self.bombs.position[i][j][1] += 20

        # add new bombs as time goes
        if self.clock % 6 == 0 :
            self.bombs.add_row()
        
        # add new item 
        if self.clock % 80 == 0 :
            self.items.add()
        self.check_item_collision()
        
        # check collision
        self.check_collision()

        # remove bombs beyond the canvas
        if (len(self.bombs.position[0]) != 0 and self.bombs.position[0][0][1] > 390) or (len(self.bombs.position[0]) == 0 and len(self.bombs.position) > 0) :
            self.bombs.remove_firstin()

        # Implementation Here
        if self.clock % 10 == 0 :
            self.setting.score_up(10)
            
        # check life and finish game
        if self.setting.life == 0 : 
            global end_flag
            end_flag = 1
            
            alarm.stop()
            self.robot.turn_off()            
            self.setting.exit_game()
            
    # Implementation Here
    def check_collision(self) :
        # check first row
        for i in range(len(self.bombs.container[0])):
            rob_x = self.robot.x 
            rob_y = self.robot.y
            ob_x = self.bombs.position[0][i][0]
            ob_y = self.bombs.position[0][i][1]
            dist = math.sqrt(math.pow(rob_x - ob_x, 2) + math.pow(rob_y - ob_y, 2))
            if dist < 14 + self.robot.bound:
                self.bombs.remove_one_obs(0,i)
                # Implementation Here
                self.setting.lose_life()
                break
    
    def check_item_collision(self) :
        for i in range(len(self.items.container)) :
            rob_x = self.robot.x 
            it_x = self.items.position[i]
            dist = abs(rob_x - it_x)
            if dist < 4 + self.robot.bound:
                self.items.remove(i)
                self.setting.score_up(50)
                break            
            
class Bombs() :
    def __init__(self):
        self.position = []
        self.container = []
        self.add_row()
    
    def add_row(self) :
        temp1 = []
        temp2 = []
        for i in range(2) :
            temp1.append([float(random.randint(0,20))/float(20)*float(width),0]) # (x,y)
            b = Bomb()
            b.layer.move(temp1[i][0], temp1[i][1])
            paper.add(b.layer)
            temp2.append(b)
                    
        self.position.append(temp1)
        self.container.append(temp2)

    def remove_firstin(self) :
        for i in range(len(self.container[0])) :
            tmp = self.container[0][i].layer
            paper.remove(self.container[0][i].layer)
            del tmp
            
        self.container.remove(self.container[0])
        self.position.remove(self.position[0])
        
    def remove_one_obs(self, i,j) :
        tmp = self.container[i][j]        
        paper.remove(self.container[i][j].layer)
        del tmp
        
        self.container[i].remove(self.container[i][j])
        self.position[i].remove(self.position[i][j])
        

class Robot :
    def __init__(self):
        self.x = 150
        self.y = 363
        self.bound = 15
        self.half_w = 12
        self.turn_on = 1
        
        r = Robot_shape(self.x-12,self.y-17)
        self.shape = r
        paper.add(self.shape.layer)
    
    def move_left(self) :
        if self.turn_on and self.x - self.half_w >= 0 :
            self.shape.layer.move(-10,0)
            self.x -= 10

    def move_right(self) :
        if self.turn_on and self.x + self.half_w <= 300 :
            self.shape.layer.move(10,0)
            self.x += 10
        
    def jump(self) :
        self.shape.layer.move(0,-20)
        sleep(0.2)
        self.shape.layer.move(0,20)
    
    def turn_off(self) : 
        self.turn_on = 0

class GameSetting() :
    def __init__(self):
        self.bound = 380

        ground = Rectangle(300,20)
        ground.setFillColor((57,88,178))
        ground.setBorderWidth(0)
        ground.move(150,390)
        paper.add(ground)

        score_text = Text('0', 20, Point(150,100))
        score_text.setFontColor('white')
        paper.add(score_text)
            
        self.ground = ground
        self.score = 0
        self.score_text = score_text        
        self.life = 3
        self.life_shape = []
        for i in range(self.life) :
            h = Heart(10+i*30, 10)
            paper.add(h.layer)
            self.life_shape.append(h)
    
    def score_up(self, up) : 
        self.score += up
        self.score_text.setMessage(str(self.score))

    def lose_life(self) :
        self.life -= 1
        paper.remove(self.life_shape[self.life].layer)
        
    def exit_game(self) : 
        over = Text("GAME OVER", 25, Point(150,180))
        over.setFontColor((255,0,115))
        your_score = Text("Your Score : " + str(self.score), 20, Point(150, 210))
        your_score.setFontColor('white')
        msg = Text("Press s key to close game", 10, Point(150, 230))
        msg.setFontColor('white')

        paper.add(over)
        paper.add(your_score)
        paper.add(msg)

class Items() :
    def __init__(self):
        self.position = []
        self.container = []
        self.add()
    
    def add(self):
        item = Item()
        pos = float(random.randint(0,20))/float(20)*float(width)
        item.layer.move(pos, 370)
        paper.add(item.layer)
        
        self.container.append(item)
        self.position.append(pos)  

    def remove(self, i):
        if len(self.container) != 0 :
            paper.remove(self.container[i].layer)
            
            pos = self.position[i]
            tmp = self.container[i]        
            self.container.remove(self.container[i])
            self.position.remove(self.position[i])
            del tmp

            msg = Text("+50", 10, Point(pos+20,360))
            msg.setFontColor('white')
            paper.add(msg)
            sleep(0.5)
            paper.remove(msg)


robot = Robot()
bombs = Bombs()
setting = GameSetting()
items = Items()

alarm = Timer(0.1,True)
idle_func = idle(setting, robot, bombs, items)
alarm.addHandler(idle_func)
alarm.start()

while True : 
    e = paper.wait()
    d = e.getDescription()
        
    if d == 'keyboard':
        k = e.getKey()
        if k == 'a':
            robot.move_left()
        elif k == 'd':
            robot.move_right()
        elif k == 'w' :
            robot.jump()

        if end_flag == 1 and k == 's' :
            paper.close()
            break

