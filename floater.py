# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    def __init__(self,x,y):
        self._radius = 5
        Prey.__init__(self,x, y, 2 * self._radius,\
                      2 * self._radius, 0 ,5)
        self.randomize_angle()
        
    def update(self,model):
        speed_deviation = random.uniform(-0.5,0.5)
        angle_deviation = random.uniform(-0.5,0.5)
        if random.randint(1,10) <= 3:
            total_angle = self.get_angle() + angle_deviation 
            self.set_angle(total_angle)
            total_speed = self.get_speed() + speed_deviation
            if total_speed >= 3 and total_speed <= 7:
                self.set_speed(total_speed)
            self.move()
        
    def display(self,canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius,\
                           self._x + self._radius, self._y + self._radius,\
                           fill = 'red')
        