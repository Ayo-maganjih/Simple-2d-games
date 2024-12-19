import pygame
pygame.init()

w,h= 720,1344
screen = pygame.display.set_mode((w,h))
size = 49 # box size

# creating the rects
rects = []
for y in range(20):
    k = []
    for x in range(13):
        a = [x*50+30,y*50+100,size,size]
        k.append(a)
    rects.append(k)

# determining the pathway
val = [
    [1,0,0,0,1,1,1,0,0,1,0,0,0],
    [1,1,0,0,0,0,1,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,1,0,0,1,0,1,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,0,1],
    [1,1,0,0,0,1,1,1,1,0,1,0,1],
    [1,0,1,1,1,0,0,0,0,0,1,0,0],
    [1,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,1,0,1,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,0,1],
    [0,0,1,0,0,0,0,1,1,0,1,1,1],
    [1,1,1,1,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,0,0,0],
    [1,0,1,0,0,1,0,1,0,0,1,1,1],
    [0,0,1,1,0,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,1,0,1,0,0,0,0,1],
    [1,1,0,1,0,1,1,1,1,0,1,1,1],
    [1,0,1,1,0,0,1,0,1,0,1,0,0],
    [1,1,1,0,1,0,0,0,1,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,1,0,0,1]
]

def wall(screen,a,b,rects):
    wc = (150,150,150)
    y = rects[a][b]
    pygame.draw.rect(screen,wc,y)

def path(screen,a,b,rects):
    pc = (50,50,50)
    y = rects[a][b]
    pygame.draw.rect(screen,pc,y) 
                
def write(text,t,b,i):
    font = pygame.font.SysFont('timesnewroman',54,b,i)
    img = font.render(text,1,(240,240,0),(60,60,60))
    screen.blit(img,t)

# player
player = pygame.image.load('play.png')
player = pygame.transform.scale(player,(49,49))
player_rect = player.get_rect()
player_rect.left = 30
player_rect.top = 100

# diamond
diamond = pygame.image.load('diamond.png')
diamond = pygame.transform.scale(diamond,(45,45))
diamond_rect = diamond.get_rect()
diamond_rect.left = 630
diamond_rect.top = 1050

# direction buttons
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')
right = pygame.image.load('right.png')
left = pygame.image.load('left.png')
    
up = pygame.transform.scale(up,(90,90))
down = pygame.transform.scale(down,(90,90))
right = pygame.transform.scale(right,(90,90))
left = pygame.transform.scale(left,(90,90))
    
# rects
up_rect = up.get_rect()
down_rect = down.get_rect()
right_rect = right.get_rect()
left_rect = left.get_rect()
    
# buttons position
up_rect.centerx = 340
up_rect.centery = 1150
down_rect.centerx = 340
down_rect.centery = 1250
right_rect.centerx = 440
right_rect.centery = 1200
left_rect.centerx = 240
left_rect.centery = 1200

# clock
clock = pygame.time.Clock()

# win text
font = pygame.font.SysFont('Arial',141,1,1)
win = font.render('YOU WIN!',1,('yellow'),(50,50,50))
win_pos = (30,500)

while True:    
    screen.fill((0,0,0))
    
    # writing the title
    write('  Find the diamond  ',(50,20),1,1)
    
    # drawing the buttons
    screen.blit(up,up_rect)
    screen.blit(down,down_rect)
    screen.blit(right,right_rect)
    screen.blit(left,left_rect)
    
    # drawing the board
    pathway = []
    for a in range(20):
        for b in range(13):
            c = val[a][b]
            if c == 0:
                wall(screen,a,b,rects)
            else:
                path(screen,a,b,rects)
                pathway.append(rects[a][b])

    # drawing the player and diamond
    screen.blit(diamond, diamond_rect)
    screen.blit(player,player_rect)
        
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if up_rect.collidepoint(x,y):
                touch = [player_rect.x, player_rect.y-50,size,size]
                if touch in pathway:
                    player_rect.y -= 50

            if down_rect.collidepoint(x,y):
                touch = [player_rect.x, player_rect.y+50,size,size]
                if touch in pathway:
                    player_rect.y += 50
            
            if right_rect.collidepoint(x,y):
                touch = [player_rect.x+50, player_rect.y,size,size]
                if touch in pathway:
                    player_rect.x += 50

            if left_rect.collidepoint(x,y):
                touch = [player_rect.x-50, player_rect.y,size,size]
                if touch in pathway:
                    player_rect.x -= 50
    
    # checking player win
    if player_rect.colliderect(diamond_rect):
        screen.blit(win,win_pos)
        pygame.display.flip()
        pygame.time.wait(4000)
        player_rect.left = 30
        player_rect.top = 100
        continue
    else:                
        pygame.display.flip()
    clock.tick(60)