import pygame,sys, random
pygame.init()

screen = pygame.display.set_mode((600,1350))
pygame.display.set_caption('Snowfall')
snow = []
for f in range(150):
    x = random.randrange(50,670)
    y = random.randrange(50,1400)
    snow.append([x,y])
clock = pygame.time.Clock()

while True:
    screen.fill('black')
    for ice in range(len(snow)):
        pygame.draw.circle(screen,'white',snow[ice],3)
        snow[ice][1] += 5
        if snow[ice][1] > 1400:
            snow[ice][1] = random.randrange(-50,-10)
            snow[ice][0] = random.randrange(50,670)
        
    pygame.display.flip()
    clock.tick(30)