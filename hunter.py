# A Hunter is both a Mobile_Simulton and a Pulsator: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.

from simulton import Simulton
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    distance_bounds = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self._speed = 5
        self.angle = self.randomize_angle()

    
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
          
        # Growing the pulsator 
        prey_set = model.find(lambda x: isinstance(x,Prey))
        for item in prey_set:
            if self.contains(item) == True: 
                delete_list.append(item)
                self.set_dimension(width+1,height+1)
        for ball in delete_list: 
            model.remove(ball)
         
        if self._count == self.max_count:
            self.set_dimension(width-1,height-1)
            self._count = 0
        if width == 0 and height == 0 : 
            model.remove(self)
   
             

            
            
