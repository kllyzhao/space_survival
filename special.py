
# My special class is behaves like a hunter but with these specific differences: 
# - The special object starts off pink 
# - With every prey it catches, its speed will increase
# - Once it has caught 10 prey objects, it will turn invisible 
# - After it catches 8 more prey objects, it will flash between 
# being invisible and a different color from a set 


from hunter import Hunter 
from prey import Prey
from math import atan2
import random
 
class Special(Hunter):
    prey_count = 0 
    color = "indian red"
    outline = "indian red"
    # Fall themed colors
    color_list = ["IndianRed1","IndianRed2", "IndianRed3","IndianRed4",\
                  "tan1","tan2","tan4",\
                  "firebrick1","firebrick2","firebrick3", "firebrick4",\
                  "brown1","brown2","brown3","brown4",\
                  "salmon1","salmon2","salmon3","salmon4",\
                  "LightSalmon2", "LightSalmon3", "LightSalmon4",\
                  "coral1","coral2","coral3","coral4",\
                  "tomato2","tomato3","tomato4"]

    def __init(self,x,y):
        Hunter.__init__(x,y)
        
    def update(self,model):
        self.move()
        dist_dict = {}
        dist_list = []
        prey_set = model.find(lambda x: isinstance(x,Prey))

        for ball in prey_set: 
            dist_between = self.distance(ball.get_location())
            if dist_between <= self.distance_bounds:
                dist_dict[dist_between] = ball
                for key,value in dist_dict.items(): 
                    dist_list.append(key)
                least_dist = min(dist_list)
                ball = dist_dict[least_dist]
                x = ball.get_location()
                y = self.get_location()
                angle = atan2(x[1]-y[1],x[0]-y[0])
                self.set_angle(angle)
                
        delete_list = []
        dimension_tuple = self.get_dimension()
        width = dimension_tuple[0]
        height = dimension_tuple[1]
           
        self._count += 1
          
        # Growing the special 
        prey_set = model.find(lambda x: isinstance(x,Prey))
        for item in prey_set:
            if self.contains(item) == True: 
                self.prey_count += 1
                delete_list.append(item)
                self.set_dimension(width+0.5,height+0.5)
                self.set_speed(self._speed +1)
                
        if self.prey_count >= 10:
            self.color = "white"
            self.outline = "white"
            if self.prey_count >= 18 and self.prey_count % 2 == 0: 
                self.color = random.choice(self.color_list)
                self.outline = self.color 
        for ball in delete_list: 
            model.remove(ball)
         
        if self._count == self.max_count:
            self.set_dimension(width-0.5,height-0.5)
            self.set_speed(self._speed -1)
            if self._speed <= 5: 
                self._speed = 5
            self._count = 0
        if width == 0 and height == 0 : 
            model.remove(self)
   
    def display(self,canvas):
        width,height = self.get_dimension()
        canvas.create_oval(self._x-width/2, self._y-height/2,\
                           self._x+width/2, self._y+height/2,\
                           fill = self.color, outline = self.outline)

            
