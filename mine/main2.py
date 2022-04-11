import pygame
import random as rand
from pygame import mixer

#initialising the pygame:
pygame.init()

#creating the screen:
screen = pygame.display.set_mode((1000,750))

#Title and icon:
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load('game.png')
pygame.display.set_icon(icon)

#The Board:
board = pygame.image.load('board.png')
#green = pygame.image.load('green.png')
#green = pygame.transform.scale(green,(30,50))
blue = pygame.image.load('blue.png')
blue = pygame.transform.scale(blue,(30,50))
l = 30
#g = 1
b = 1
#start = 0

#The Physical Board:
lo = {}
p = 100
yl = 30
for i in range(0,5):
    xl = 30
    for j in range(0, 10):
        lo[p]= (xl, yl)
        xl += 70
        p -= 1
    yl += 140
    p -= 10
p = 81
yl = 100
for i in range(0,5):
    xl = 30
    for j in range(0,10):
        lo[p] = (xl, yl)
        xl += 70
        p += 1
    yl += 140
    p -= 30
(m1, n1) = lo[1]
(m2, n2) = lo[1]
l1 = {5:58, 14:49, 38:20, 51:10, 53:72, 76:54, 64:83, 91:73, 97:61}

#The Die:
red = (255,0,0)
white = (255,255,255)
x1 = 0; y1 = 0; x2 = 0; y2 = 0; x3 = 0; y3 = 0; x4 = 0; y4 = 0; x5 = 0; y5 = 0; x6 = 0; y6 = 0

#Background Music:
#mixer.music.load('All Time Low [simple edit].mp3')
#mixer.music.play(-1)
o = mixer.Sound('laser.wav')

def func_board():
      screen.blit(board, (l,l))

#def func_green(x,y):
    #screen.blit(green, (x, y))

def func_blue(x,y):
    screen.blit(blue, (x,y))

#Game Loop:
var = True
while var:
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            var = False

        #Associating Keyboard Controls:
        if i.type == pygame.KEYDOWN:
            t = i.unicode
            if t == ' ':
                v = mixer.Sound('die.wav')
                v.play()
                num = rand.randrange(1, 7)
                #if start == 0:
                    #turn = g
                #elif start == 1:
                turn = b
                if num == 1:
                    x1 = 865;y1 = 375;x2 = 865;y2 = 375;x3 = 865;y3 = 375;x4 = 865;y4 = 375;x5 = 865;y5 = 375;x6 = 865;y6 = 375
                elif num == 2:
                    x1 = 800;y1 = 310;x2 = 800;y2 = 310;x3 = 800;y3 = 310;x4 = 930;y4 = 440;x5 = 930;y5 = 440;x6 = 930;y6 = 440
                elif num == 3:
                    x1 = 800;y1 = 310;x2 = 800;y2 = 310;x3 = 930;y3 = 440;x4 = 930;y4 = 440;x5 = 865;y5 = 375;x6 = 865;y6 = 375
                elif num == 4:
                    x1 = 800;y1 = 310;x2 = 800;y2 = 310;x3 = 930;y3 = 440;x4 = 930;y4 = 440;x5 = 800;y5 = 440;x6 = 930;y6 = 310
                elif num == 5:
                    x1 = 800;y1 = 310;x2 = 800;y2 = 310;x3 = 930;y3 = 440;x4 = 800;y4 = 440;x5 = 930;y5 = 310;x6 = 865;y6 = 375
                elif num == 6:
                    x1 = 800;y1 = 310;x2 = 800;y2 = 440;x3 = 930;y3 = 310;x4 = 930;y4 = 440;x5 = 800;y5 = 375;x6 = 930;y6 = 375
                turn += num
                for j in lo:
                    if j == turn:
                        if j in l1:
                            o.play()
                            turn = l1[turn]
                        if start == 0:
                            (m1, n1) = lo[turn]
                        elif start == 1:
                            (m2, n2) = lo[turn]
        if i.type == pygame.KEYUP:
            if t == ' ':
                #if start == 0:
                    #g = turn
                    #if g >= 100:
                        #var = False
                        #print('green won!!!!')
                    #start = 1
                #elif start == 1:
                    b = turn
                    if b >= 100:
                        var = False
                        print('blue won!!!')
                    start = 0
        screen.fill((0, 200, 200))
        pygame.draw.rect(screen, red, (790, 300, 150, 150))
        pygame.draw.circle(screen, white, [x1, y1], 10)
        pygame.draw.circle(screen, white, [x2, y2], 10)
        pygame.draw.circle(screen, white, [x3, y3], 10)
        pygame.draw.circle(screen, white, [x4, y4], 10)
        pygame.draw.circle(screen, white, [x5, y5], 10)
        pygame.draw.circle(screen, white, [x6, y6], 10)
        func_board()
        func_blue(m2, n2)
        #func_green(m1, n1)
        pygame.display.flip()