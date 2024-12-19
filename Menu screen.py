import pygame,sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((700,1200))
width = screen.get_width()
height = screen.get_height()

# colors
black = Color('black')
red = Color('red')
white = Color('white')
blue = Color('blue')
white = Color('white')
yellow = Color('yellow')

# colors allocation
title_color = white
subtitle_color = yellow
back_color = red
menubg = black

# backgrounds
bg1 = pygame.image.load('space3.png')
bg2 = pygame.image.load('space4.png')
bg1 = pygame.transform.scale(bg1,(width, height))
bg2 = pygame.transform.scale(bg2,(width, height))


# fonts and texts
title = pygame.font.SysFont('Arial',120,True,True)
menu_title = title.render('    MENU',1,title_color)
start_title = title.render('   START',1,title_color)
options_title = title.render(' OPTIONS',1,title_color)
settings_title = title.render('SETTINGS',1,title_color)

subtitle = pygame.font.SysFont(None,100,)
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
        check_event2()
        screen.blit(bg1,(0,0))
        pygame.draw.rect(screen,title_color,title_rect,5)
        pygame.draw.rect(screen,back_color,back_rect,5)
        screen.blit(start_title,(50,100))
        screen.blit(back_subtitle, (50,1200))
        
        pygame.display.flip()

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