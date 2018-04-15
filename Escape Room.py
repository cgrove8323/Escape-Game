# to load an image in, just use screen.blit(name, (x, y)) after setting it
# equal to the name with the pygame function used in bunny run

# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Escape Room"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (93, 242, 67)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (135, 85, 35)
SILVER = (188, 185, 183)
FLOOR = (99, 58, 13)
GOLD = (239, 201, 50)


def draw_wall_one():
    paintings = [[220, 200, 180, 160], [40, 40, 100, 80], [200, 60, 100, 100],
                 [20, 160, 80, 80], [140, 180, 60, 60], [60, 280, 120, 100]]
    for p in paintings:
        pygame.draw.rect(screen, RED, p)
        left = p[0]
        right = p[0] + p[2]
        top = p[1]
        bottom = p[1] + p[3]
        width = p[2]
        height = p[3]
        borders = [[left, top, width, 10], [right - 10, top, 10, height],
                   [left, bottom - 10, width, 10], [left, top, 10, height]]
        for b in borders:
            pygame.draw.rect(screen, GOLD, b)
   
    pygame.draw.rect(screen, BROWN, [580, 200, 160, 300])
    pygame.draw.rect(screen, BLUE, [500, 280, 40, 40])

    pygame.draw.rect(screen, BLUE, [100, 460, 140, 100])
    
    pygame.draw.rect(screen, BLUE, [740, 540, 60, 60])
    pygame.draw.rect(screen, BLUE, [660, 540, 60, 60])

def display_messege():
    pygame.draw.rect(screen, WHITE, [200, 200, 400, 200])
    pygame.draw.rect(screen, RED, [580, 200, 20, 20])
    
messege_box = False
chest_clicked = False
keypad_clicked = False

# Game Loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    chest = pygame.Rect(100, 460, 140, 100)
    keypad = pygame.Rect(500, 280, 40, 40)
    right = pygame.Rect(740, 540, 60, 60)
    left = pygame.Rect(660, 540, 60, 60)
    messege_x = pygame.Rect(580, 200, 20, 20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            while not messege_box:
                location = pygame.mouse.get_pos()
                if right.collidepoint(location):
                    print("right")
                elif left.collidepoint(location):
                    print("left")
                else:
                    if chest.collidepoint(location):
                        print("chest")
                        #chest_clicked = True
                        messege_box = True
                    if keypad.collidepoint(location):
                        print("keypad")
                        #keypad_clicked = True
                        messege_box = True
            if messege_box:
                box_loc = pygame.mouse.get_pos()
                if messege_x.collidepoint(box_loc):
                    messege_box = False


    # Game logic (Check for collisions, update points, etc.)



    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SILVER)
    pygame.draw.rect(screen, BLACK, [0, 500, 800, 100])
    draw_wall_one()
    if messege_box:
        display_messege()
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
