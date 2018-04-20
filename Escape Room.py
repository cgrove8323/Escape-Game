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

# Fonts
title_font = pygame.font.Font("fonts/NanumBrushScript.ttf", 72)
text_font = pygame.font.Font("fonts/Montserrat.ttf", 32)
messege_font = pygame.font.Font("fonts/Montserrat.ttf", 14)

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

def draw_keypad():
    pygame.draw.rect(screen, BLUE, [500, 280, 45, 50])
    pygame.draw.rect(screen, WHITE, [510, 285, 25, 10])
    buttons = [[510, 300, 5, 5], [520, 300, 5, 5], [530, 300, 5, 5],
               [510, 310, 5, 5], [520, 310, 5, 5], [530, 310, 5, 5],
               [510, 320, 5, 5], [520, 320, 5, 5], [530, 320, 5, 5]]
    for b in buttons:
        pygame.draw.rect(screen, WHITE, b)
        
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
    draw_keypad()
    
    pygame.draw.rect(screen, BLUE, [100, 460, 140, 100])
    
    pygame.draw.rect(screen, BLUE, [740, 540, 60, 60])
    pygame.draw.rect(screen, BLUE, [660, 540, 60, 60])

    pygame.draw.rect(screen, BLUE, [610, 80, 100, 40])

def display_messege():
    pygame.draw.rect(screen, WHITE, [200, 200, 400, 200])
    pygame.draw.rect(screen, RED, [580, 200, 20, 20])
    pygame.draw.line(screen, BLACK, (580, 200), (600, 220), 1)
    pygame.draw.line(screen, BLACK, (580, 220), (600, 200), 1)
    if chest_clicked:
        line1 = text_font.render("Locked", 1, BLACK)
        line2 = messege_font.render("Enter Keyword", 1, BLACK)
        screen.blit(line1, (340, 260))
        screen.blit(line2, (345, 300))
    if keypad_clicked:
        line1 = text_font.render("Enter Passcode", 1, BLACK)
        screen.blit(line1, (280, 284))
    if painting_clicked:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "PLMKOIJNBHUYGVCFTRDXZSEWAQ"
        letter_keys = []
        for i in range(26):
            letter = alphabet[i]
            translation = key[i]
            letter_keys.append(str(translation) + " = " + str(letter))
        x_coords = [280, 320, 360, 400, 440]
        y_coords = [260, 275, 290, 305, 320]
    
        coords = []
        for x in x_coords:
            for y in y_coords:
                coord = (x, y)
                coords.append(coord)
        for i in range(25):
            line = messege_font.render(letter_keys[i], 1, BLACK)
            screen.blit(line, coords[i])
                    
        '''y = 260
        for i in range(5):
            line = messege_font.render(letter_keys[i], 1, BLACK)
            screen.blit(line, (x_coords[i], y))
            y += 15'''
        
        '''second_line = letter_keys[0] + letter_keys[1] + letter_keys[2] + letter_keys[3] + letter_keys[4]
        third_line = letter_keys[5] + letter_keys[6] + letter_keys[7] + letter_keys[8] + letter_keys[9]
        fourth_line = letter_keys[10] + letter_keys[11] + letter_keys[12] + letter_keys[13] + letter_keys[14]
        fifth_line = letter_keys[15] + letter_keys[16] + letter_keys[17] + letter_keys[18] + letter_keys[19]
        sixth_line = letter_keys[20] + letter_keys[21] + letter_keys[22] + letter_keys[23] + letter_keys[24]'''
        line1 = messege_font.render("Decode the messege:", 1, BLACK)
        '''line2 = messege_font.render(second_line, 1, BLACK)
        line3 = messege_font.render(third_line, 1, BLACK)
        line4 = messege_font.render(fourth_line, 1, BLACK)
        line5 = messege_font.render(fifth_line, 1, BLACK)
        line6 = messege_font.render(sixth_line, 1, BLACK)'''
        line7 = text_font.render("BVXOY", 1, BLACK)
        screen.blit(line1, (280, 240))
        '''screen.blit(line2, (280, 260))
        screen.blit(line3, (280, 275))
        screen.blit(line4, (280, 290))
        screen.blit(line5, (280, 305))
        screen.blit(line6, (280, 320))'''
        screen.blit(line7, (340, 340))
        
    
messege_box = False
chest_clicked = False
keypad_clicked = False
painting_clicked = False

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
    painting = pygame.Rect(220, 200, 180, 160)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not messege_box:
                location = pygame.mouse.get_pos()
                if right.collidepoint(location):
                    print("right")
                elif left.collidepoint(location):
                    print("left")
                else:
                    if chest.collidepoint(location):
                        #print("chest")
                        chest_clicked = True
                        messege_box = True
                    if keypad.collidepoint(location):
                        #print("keypad")
                        keypad_clicked = True
                        messege_box = True
                    if painting.collidepoint(location):
                        painting_clicked = True
                        messege_box = True
                        
            if messege_box:
                box_loc = pygame.mouse.get_pos()
                if messege_x.collidepoint(box_loc):
                    messege_box = False
                    chest_clicked = False
                    keypad_clicked = False
                    painting_clicked = False


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
