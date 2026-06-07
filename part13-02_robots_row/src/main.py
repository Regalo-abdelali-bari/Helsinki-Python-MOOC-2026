# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

page = pygame.display.set_mode((640,480))
robot = pygame.image.load("robot.png")

page.fill((0,0,0))
width = robot.get_width()

for i in range(10):
    page.blit(robot,(50 + (i * width),100 ))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
