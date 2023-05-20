import sandbox
import time
import random

#Project Description
"""This project simulates the movement of several particles
and their interactions with other particles and the box
bounding them."""


#Create canvas (525 x 600)
canvas = sandbox.createCanvas()
#Variables
rad = 10 #Radius of particles
rng = 3  #Range for collision detection. Between 3-5 is effective; smaller values will allow te program to run faster.
amount = 15  #Number of particles
x_bound = 525 - rad
y_bound = 600 - rad
friction_force = 11/10  #Magnitude of force used to slow particles

#Create box
x1 = 175
x2 = 350
y1 = 200
y2 = 400
def draw_lines():
  canvas.line((x1, y1), (x2, y1))
  canvas.line((x1, y1), (x1, y2))
  canvas.line((x1, y2), (x2, y2))
  canvas.line((x2, y1), (x2, y2))

#Create particles
"""Randomly sets position and speed of particles and adds 
them to list."""
particles = []
for i in range(amount):
  x = random.randrange(200, 300)
  y = random.randrange(250, 350)
  xspeed = random.randrange(-100, 100)
  yspeed = random.randrange(-100, 100)
  #Each object is represented by a list of data (x/y position, x/y speed, radius). 
  #The list 'particles' is a list of these lists.
  particles.append([x, y, xspeed, yspeed, rad])



def move_accel(objects):
  """Moves particles.  Accelerates them opposite to their
  direction of motion to mimic a friction force, and reverses
  their direction when they come in contact with one another
  or the box boundaries."""
  #Keeps running while the primary object is within bounds
  while ((rad < objects[0][0] < x_bound) and (rad < objects[0][0] < y_bound)):
      for info in objects:
        #Detects if the object is touching any other object
        hit = False
        for i in range(0, len(objects)):
          #Checks to make sure the particle is not itself
          if not(info[0] == objects[i][0] and info[1] == objects[i][1]):
          	
            #Checks for a hit in a small collision area
            for j in range(-rng, rng):
            	for k in range(-rng, rng):
          			if (info[0] == (objects[i][0] + j)) and (info[1] == (objects[i][1] + k)) or (info[0] == x1 + info[4] + j or info[0] == x2 - info[4] + j or info[1] == y1 + info[4] + k or info[1] == y2 - info[4] + k):
          				hit = True 
        #If the object does hit another, reverses direction
        if hit:
          info[2] = info[2] * -1
          info[3] = info[3] * -1
        #Calls the move function
        info[0] = move(0, info)
        info[1] = move(1, info)
        #Changes the speed
        info[2] = accel(2, info)
        info[3] = accel(3, info)
      #Waits, then runs the loop again
      time.sleep(.03)
      canvas.reset()

def accel(x_or_y, info):
  """Applies acceleration in the opposite direction of 
  motion."""
  if info[x_or_y] > 0:
    #Mass of particle and time already factored in. Essentially 'friciton_force' here is already calculated to represent the change in velocity to be applied.
    return info[x_or_y] - friction_force
  elif info[x_or_y] < 0:
    return info[x_or_y] + friction_force
  else:
    return 0
      
def move(x_or_y, info):
  """Updates the particle's position according to its
  speed and redraws the canvas."""
  if x_or_y == 0:
  	canvas.circle((info[0], info[1]), info[4])
  draw_lines()
  return info[x_or_y] + (info[x_or_y + 2] / 30)
  
#Commands
move_accel(particles)

