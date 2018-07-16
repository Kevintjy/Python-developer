import pygame
import sys

# initialize the pygame
pygame.init()

# set the size of screen
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('The first turtle run game')

# put the turtle into screen
turtle = pygame.image.load('turtle.jpeg')
position = turtle.get_rect()

# set the turtle running speed
speed = [-8, 4]
turtle = pygame.transform.flip(turtle, True, False)  # turnover the turtle

# write a loop to make program run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # move the image
    position = position.move(speed)

    # collision
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)  # turnover the turtle
        speed[0] = -speed[0]   # change the horizontal velocity

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]  # change the vertical velocity

    # set the background
    bg = (255, 255, 255)  # three parameters represent RED,GREEN,BLUE, all 255 means white
    screen.fill(bg)

    # update the image
    screen.blit(turtle, position)

    # update the window
    pygame.display.flip()

    # set the delay
    pygame.time.delay(10)



