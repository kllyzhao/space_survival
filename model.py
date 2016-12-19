import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
 
from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from prey      import Prey 
from special   import Special
from mobilesimulton import Mobile_Simulton
from simulton  import Simulton
 
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0 
clicked = ''
objects = set()
execute_one = False
 
 
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())
 
#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, clicked, objects, execute_one
    running = False
    cycle_count = 0 
    clicked = ''
    objects = set()
    execute_one = False 
 
 
#start running the simulation
def start ():
    global running
    running = True 
 
 
#stop running the simulation (freezing it)
def stop ():
    global running
    running = False
 
 
#tep just one update in the simulation
def step ():
    global running,execute_one
    running = True
    execute_one = True
    start()
    update_all()
    stop()     
 
 
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked
    clicked = kind 
     
 
#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global clicked
    global objects
    if clicked != "Remove":
        objects.add(eval(clicked + '(' + str(x) + ',' + str(y) + ')'))
    else:
        if clicked == "Remove":
            for item in objects.copy(): 
                if type(item) == Ball or type(item) == Floater:
                    if item.contains((x,y)):
                        objects.remove(item)
                if type(item) == Black_Hole or type(item) == Pulsator\
                or type(item) == Hunter or type(item) == Special: 
                    if item.contains2((x,y)):  
                        objects.remove(item)


#add simulton s to the simulation
def add(s):
    global objects
    objects.add(s)
 
# remove simulton s from the simulation    
def remove(s):
    global objects
    objects.remove(s)
 
#find/return a set of simultons that each satisfy predicate p    
def find(p):
    true_set = set()
    for ball in objects:
        if p(ball) == True: 
            true_set.add(ball)
    return true_set
 
#call update for every simulton in the simulation
def update_all():
    global cycle_count, objects
    objects_copy = set(objects)
    if running:
        cycle_count += 1
        for b in objects_copy:
            b.update(model) 
    
 
#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    try: 
        for o in controller.the_canvas.find_all():
            controller.the_canvas.delete(o)
    
        for b in objects:
            b.display(controller.the_canvas)        
        
    except AttributeError:
        reset()
     
    controller.the_progress.config(text=str(len(find(lambda x: isinstance(x, Prey))))+" balls / "+str(cycle_count)+" cycles")

    
            