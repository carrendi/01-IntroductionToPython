"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Danna Carreno.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
import rosegraphics as rg

window= rg.TurtleWindow()
window.delay(10)

simba = rg.SimpleTurtle('turtle')
simba.speed = 2

size=120


simba.pen.pen_up
simba.draw_circle(size)
simba.forward(2)

simba.pen_down()
size=size-5

sunflower=rg.SimpleTurtle()
sunflower.pen =rg.Pen('yellow', 30)

sunflower.forward(100)
sunflower.right(90)
sunflower.forward(100)
sunflower.right(90)
sunflower.forward(100)
sunflower.right(90)
sunflower.forward(100)

sunflower.draw_circle(36)
sunflower.right(10)
sunflower.left(36)
sunflower.left(45)
sunflower.forward(20)

sunflower.right(90)
sunflower.forward(100)
sunflower.left(90)
sunflower.forward(100)
sunflower.right(90)
sunflower.forward(50)
sunflower.left(90)
sunflower.forward(150)
sunflower.right(90)
sunflower.forward(50)
sunflower.right(90)
sunflower.left(100)
##################################################
