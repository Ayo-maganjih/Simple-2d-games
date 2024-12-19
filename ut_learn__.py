import pygame, sys, random
from pygame.locals import *
pygame.font.init()


WIDTH, HEIGHT = 750, 1400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FIRST GAME!')

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,100,0)
ORANGE = (255,128,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIME = (0,255,0)
YELLOW = (255,255,0)

HEALTH_FONT = pygame.font.SysFont('timesnewroman', 60, bold=True, italic=True)
mssg_color = Color('green')
WINNER_FONT = pygame.font.SysFont('arial', 150, bold = True, italic = True)
win_color = Color('yellow')


FPS = 60
VEL = 10
BULLET_VEL = 30
MAX_BULLETS = 10


SHIP_WIDTH = 250
SHIP_HEIGHT = 250
SHIP = pygame.image.load('images/jet.png')
SHIP = pygame.transform.scale(SHIP,(SHIP_WIDTH,SHIP_HEIGHT))

bgs = ['images/space3.png','images/space4.png']
background = random.choice(bgs)

BACK = pygame.image.load(background)
BACK = pygame.transform.scale(BACK,(WIDTH, HEIGHT))

ENE_POS = [30,100]
sp = 5
ENE_HIT = pygame.USEREVENT + 1


def draw_winner(text):
    WIN.blit(BACK,(0,0))
    win = WINNER_FONT.render(text,1,win_color)
    WIN.blit(win, (25,450))
    cr = HEALTH_FONT.render('Created by: MAPESSAH',1,mssg_color)
    WIN.blit(cr,(5, 700))
    
    pygame.display.update()
    pygame.time.delay(3000)
    menu()
       

def draw_window(ship1, bullets, ENE_RECT, eneHealth, mssg_color):
    
    WIN.blit(BACK,(0,0))
    #pygame.draw.line(WIN,BLACK,(0,1050),(750,1050),160)

    if eneHealth < 10:
        if eneHealth > 4:
            mssg_color = ORANGE
        elif eneHealth < 5:
            mssg_color = RED


    mssg = HEALTH_FONT.render('Health: ' + str(eneHealth), 1, mssg_color)
    WIN.blit(mssg,(10,10))
    
    WIN.blit(SHIP,(ship1.x, ship1.y))  
    pygame.draw.rect(WIN, yellow, ENE_RECT)
    
    for bullet in bullets:
        pygame.draw.rect(WIN, ORANGE, bullet)   

    pygame.display.update() 
    
def ene_movements(pos,sp):
        
        if pos[0] < 1:
            sp = sp
        
        elif pos[0] > 740:
            pos[0] = -50
            
        else:
            pass
            
        pos[0] += sp
        
    
def ship1_handle_movements(x,y,ship1):
    if y > 1200:        
        if x > 541:
            ship1.x += VEL
                        
        elif x > 179:
            if x < 540:
                ship1.x -= VEL
                        
    

def check_margin(ship1):
    if ship1.x > 620:
        ship1.x = 620   
    elif ship1.x < -50:
        ship1.x = -50
        
        
def bullet_firing(x,y, bullets, ship1):
        bullet = pygame.Rect(ship1.x + SHIP_WIDTH / 2, ship1.y + 3,10,20)
        if len(bullets) < MAX_BULLETS:
            bullets.append(bullet)


def handle_bullets(bullets, ENE_RECT):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if ENE_RECT.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ENE_HIT))
            bullets.remove(bullet)
        elif bullet.y < 10:
            bullets.remove(bullet)


def main():
    ship1 = pygame.Rect(100, 980, SHIP_WIDTH, SHIP_HEIGHT)
    
    bullets = []
    enes = []

    eneHealth = 25
    tex = ''
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        ENE_RECT = pygame.Rect(ENE_POS[0], ENE_POS[1], 100, 100)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.FINGERMOTION:
                x = event.x * WIN.get_width()
                y = event.y * WIN.get_height()
                
                ship1_handle_movements(x,y,ship1)
                
            elif event.type == pygame.FINGERDOWN:
                xb = event.x * WIN.get_width()
                yb = event.y * WIN.get_height() 
                
                if xb < 179:
                    if yb > 1000:
                        bullet_firing(xb,yb, bullets, ship1)
            if event.type == ENE_HIT:
                eneHealth -= 1
                
            if eneHealth == -1:
               tex = 'YOU WIN!'
               
            if tex != '':
               draw_winner(tex)
               break
               
               
        check_margin(ship1)  
        
        ene_movements(ENE_POS,sp)   
        
        handle_bullets(bullets, ENE_RECT)    
                
        draw_window(ship1, bullets, ENE_RECT, eneHealth, mssg_color)
             
    return
    
screen = pygame.display.set_mode((700,1200))
width = screen.get_width()
height = screen.get_height()

# colors
black = Color('black')
red = Color('red')
white = Color('white')
blue = Color('blue')
green = Color('green')
yellow = Color('yellow')

# colors allocation
title_color = green
subtitle_color = green
back_color = red
menubg = black

# backgrounds
bg1 = pygame.image.load('images/space3.png')
bg2 = pygame.image.load('images/space4.png')
bg1 = pygame.transform.scale(bg1,(width, height))
bg2 = pygame.transform.scale(bg2,(width, height))


# fonts and texts
title = pygame.font.SysFont('Arial',120,True,True)
menu_title = title.render('    MENU',1,title_color)
start_title = title.render('   START',1,title_color)
options_title = title.render(' OPTIONS',1,title_color)
settings_title = title.render('SETTINGS',1,title_color)

subtitle = pygame.font.SysFont('timesnewroman',70, True, True)
start_subtitle = subtitle.render('   > Start',1,subtitle_color)
options_subtitle = subtitle.render('   > Options',1,subtitle_color)
settings_subtitle = subtitle.render('   > Settings',1, subtitle_color)
quit_subtitle = subtitle.render('   > Exit',1,subtitle_color) 
back_subtitle = subtitle.render('BACK',1,back_color)

title_rect = (10,100,670,150)
back_rect = (40,1190,230,120)

def check_event1():
    for even in pygame.event.get():
        if even.type == FINGERUP:
            x = even.x * screen.get_width()
            y = even.y * screen.get_height()
            
            if x > 50 and x < 500:
                if y > 300 and y < 370:
                    start()
                    
                if y > 400 and y < 470:
                    options()
                    
                if y > 500 and y < 570:
                    settings()
                    
                if y > 600 and y < 670:
                    quit()

def check_event2():
    for even in pygame.event.get():
        if even.type == FINGERUP:
            x = even.x * screen.get_width()
            y = even.y * screen.get_height()
            
            if x > 50 and x < 500:   
                if y > 1200:
                    menu()

def menu():
    while True:
        check_event1()
        screen.fill(menubg)
        pygame.draw.rect(screen,title_color,title_rect,5)
        screen.blit(menu_title,(50,100))
        screen.blit(start_subtitle,(50,300))
        screen.blit(options_subtitle,(50,400))
        screen.blit(settings_subtitle,(50,500))
        screen.blit(quit_subtitle,(50,600))
        
        pygame.display.flip()

def start():
    while True:
        main()

def options():
    while True:
        check_event2()
        screen.blit(bg2,(0,0))
        pygame.draw.rect(screen,title_color,title_rect,5)
        pygame.draw.rect(screen,back_color,back_rect,5)
        screen.blit(options_title,(50,100))
        screen.blit(back_subtitle, (50,1200))
        
        pygame.display.flip()
        
def settings():
    while True:
        check_event2()
        screen.blit(bg2,(0,0))
        pygame.draw.rect(screen,title_color,title_rect,5)
        pygame.draw.rect(screen,back_color,back_rect,5)
        screen.blit(settings_title,(50,100))
        screen.blit(back_subtitle, (50,1200))
        
        pygame.display.flip()

# calling the main function
menu()