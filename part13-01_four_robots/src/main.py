
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

ecran = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

ecran.fill((0,0,0))

width = 640 - robot.get_width() 
height = 480 - robot.get_height()

ecran.blit(robot,(0,0))
ecran.blit(robot,(width,0))
ecran.blit(robot,(0,height))
ecran.blit(robot,(width,height))

pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()