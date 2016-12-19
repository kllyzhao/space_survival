# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey


class Pulsator(Black_Hole):
    max_count = 30
    def __init__(self,x,y):
        self._count = 0 
        self._radius = 10 
        Black_Hole.__init__(self,x,y)
        
    def update(self,model):
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
  
            