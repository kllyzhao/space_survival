# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
 
class Black_Hole(Simulton):
    def __init__(self,x,y):
        self._radius = 10
        Simulton.__init__(self,x, y, 2 * self._radius,\
                      2 * self._radius)
                
    def update(self,model):
        delete_list = []
        prey_set = model.find(lambda x: isinstance(x,Prey))
        for item in prey_set:
            if self.contains(item) == True: 
                delete_list.append(item)
        for ball in delete_list: 
            model.remove(ball)
        return prey_set    
    
    def display(self,canvas):
        width,height = self.get_dimension()
        canvas.create_oval(self._x-width/2, self._y-height/2,\
                           self._x+width/2, self._y+height/2,\
                           fill = 'black')

    def contains(self,xy):
        width,height = self.get_dimension()
        if self.distance(xy.get_location()) <= width/2:
            return True 
        
    def contains2(self,xy):
        width,height = self.get_dimension()
        if self.distance(xy) <= width/2:
            return True 
            
        
        
        
        
        
        
        
        