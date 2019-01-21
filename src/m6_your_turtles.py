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
simba.pen=rg.Pen('pink', 15)

size=120

for k in range(7):
    simba.draw_circle(size)

    simba.pen_up()
    simba.right(90)
    simba.forward(50)
    simba.right(90)
    simba.forward(100)

    simba.pen_down()
    size = size - 15

window.tracer(100)

nala = rg.SimpleTurtle('square')
nala.pen = rg.Pen('violet', 15)

for k in range(50):
    nala.draw_regular_polygon(8,k)

    nala.pen_up()
    nala.forward(k)
    nala.left(90)
    nala.forward(k)
    nala.right(50)
    nala.forward(k)
    nala.left(90)
    nala.forward(50)
    nala.pen_down()

window.close_on_mouse_click()






##################################################
