import sys, pygame
from pygame.locals import *

pygame.init()

# setting the window
screen_width= 1200
screen_height= 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen_rect = (screen_width, screen_height)

# colors
black = (0,0,0)
red = (255,0,0)
orange = (255,128,0)

x = 260
y = 130
# image of jet
jet = pygame.image.load('images/jet.png')
jet = pygame.transform.scale(jet,(250,250))

jet_rect = jet.get_rect()
jet_rect_pos = [x,y]
jet_pos = jet_rect.center

right = pygame.Rect(400, 1000, 300, 300)
left = pygame.Rect(10,1000,300,300)

# text
text = pygame.font.SysFont('Arial',80)
label = text.render('X',1, red)

bg_color = black

# frames per second rate
clock = pygame.time.Clock()
fps = 60

def main():
    ''' main function'''
    fingers = {}
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(' ')                   
                    
            elif event.type == FINGERDOWN:
                x = event.x * screen.get_width()
                y = event.y * screen.get_height()
                fingers[event.finger_id] = x,y
                
                if y < 100:
                    if x > 630:
                        pygame.quit()
                        sys.exit(pygame)

        if event.type == FINGERUP:
            fingers.pop(event.finger_id, None)

        if jet_rect_pos[0] > 520:
            jet_rect_pos[0] = 520   
        elif jet_rect_pos[0] < -50:
            jet_rect_pos[0] = -50   
       
        for finger,pos in fingers.items():
            if left.collidepoint(pos):
                jet_rect_pos[0] -= 10
                
            if right.collidepoint(pos):
                jet_rect_pos[0] += 10
                          
        screen.fill(bg_color)

        screen.blit(jet,jet_rect_pos)
        screen.blit(label, (660,10))
        
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    main()