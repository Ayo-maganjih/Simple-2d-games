import random, pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1200,600))
bg = Color('black')

def draw_buttons():
    # all buttons
    ax = Rect(50,800,190,90)
    ay = Rect(250,800,190,90)
    az = Rect(450,800,190,90)
    bx = Rect(50,900,190,90)
    by = Rect(250,900,190,90)
    bz = Rect(450,900,190,90)
    cx = Rect(50,1000,190,90)
    cy = Rect(250,1000,190,90)
    cz = Rect(450,1000,190,90)
    dx = Rect(50,1100,190,90)
    dy = Rect(250,1100,190,90)
    dz = Rect(450,1100,190,90)
    
    buttons = [ax,ay,az,bx,by,bz,cx,cy,cz,dx,dy,dz]
    font = pygame.font.SysFont('timesnewroman',50,True,True)
    num = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','  -',' 0','OK']
    texts = []
    a = 0
    for m in num:
        text = font.render(num[a],ax,Color('yellow'), Color(40,40,40))
        texts.append(text)
        a += 1
    for t in buttons:       
        pygame.draw.rect(screen,Color(40,40,40),t)
        pygame.draw.rect(screen,Color(128,128,0),t,5)
    b = 0
    for e in buttons:
        screen.blit(texts[b],(e[0]+50,e[1]+20))
        b += 1

def rectangles():        
    h = Rect(100,710,450,80)
    pygame.draw.rect(screen,Color('gray'),h)
    pygame.draw.rect(screen,Color(40,40,40),h,5)     
    pygame.draw.rect(screen,Color(40,40,40),(10,150,680,230))
    pygame.draw.rect(screen,Color(0,255,0),(10,150,680,230),3)
    pygame.draw.rect(screen,Color(40,40,40),(10,400,680,299))
    pygame.draw.rect(screen,Color(0,255,0),(10,400,680,299),3)

def writings():
    font1 = pygame.font.SysFont('timesnewroman',78,True,True)
    font2 = pygame.font.SysFont('timesnewroman',60,True,True) 
    back = ' <<'
    game = 'GAME STATS'
    played = '  Played:'
    won = ' Won:'
    lost = ' Lost:'
    product = 'Product:'
    sum = '     Sum:'
    factors = 'Factors:'
    
    labels = [back,game,played,won,lost,product,sum,factors]
    backp = (0,0)
    gamep = (100,50)
    playedp = (80,160)
    wonp = (80,260)
    lostp = (380,260)
    productp = (80,420)
    sump = (110,520)
    factorsp = (100,620)
    
    pos = [backp,gamep,playedp,wonp,lostp,productp,sump,factorsp]
    co = 0
    for d in range(1,3):
        l = font1.render(labels[co],1,Color('yellow'))
        screen.blit(l,pos[co])
        co += 1
        
    for d in range(1,7):
        l = font2.render(labels[co],1,Color('yellow'))
        screen.blit(l,pos[co])
        co += 1

def play_screen():        
    while True:   
        screen.fill(bg)
        draw_buttons()
        rectangles()
        writings()
        pygame.display.flip()

play_screen()