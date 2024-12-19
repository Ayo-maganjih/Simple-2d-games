import pygame as py
import random, sys
py.init()

class Path:
    def __init__(self):
        self.screen = py.display.set_mode((1700,800))
        self.size = 49 # box size
        
        # win text
        self.font = py.font.SysFont('Arial',143,1,1)
        self.win = self.font.render('YOU WIN!',1,('cyan'),(20,20,20))
        self.win_pos = (30,500)
        
        self.values = Values()
        
        self.pathway = []
        self.rects = []
        for y in range(13):
            k = []
            for y in range(20):
                app = [x*50+30,y*50+100,self.size,self.size]
                k.append(app)
            self.rects.append(k)
        
        
        # self.player
        self.player = py.image.load('play.png')
        self.player = py.transform.scale(self.player,(49,49))
        self.player_rect = self.player.get_rect()
        self.player_rect.left = 30
        self.player_rect.top = 100
        
        # self.diamond
        self.diamond = py.image.load('diamond.png')
        self.diamond = py.transform.scale(self.diamond,(45,45))
        self.diamond_rect = self.diamond.get_rect()
        self.diamond_rect.left = 630
        self.diamond_rect.top = 1050
        
        # direction buttons
        self.up = py.image.load('up.png')
        self.down = py.image.load('down.png')
        self.right = py.image.load('right.png')
        self.left = py.image.load('left.png')
            
        self.up = py.transform.scale(self.up,(90,90))
        self.down = py.transform.scale(self.down,(90,90))
        self.right = py.transform.scale(self.right,(90,90))
        self.left = py.transform.scale(self.left,(90,90))
            
        # rects
        self.up_rect = self.up.get_rect()
        self.down_rect = self.down.get_rect()
        self.right_rect = self.right.get_rect()
        self.left_rect = self.left.get_rect()
            
        # buttons position
        self.up_rect.centerx = 340
        self.up_rect.centery = 1150
        self.down_rect.centerx = 340
        self.down_rect.centery = 1250
        self.right_rect.centerx = 440
        self.right_rect.centery = 1200
        self.left_rect.centerx = 240
        self.left_rect.centery = 1200
        
        # clock
        self.clock = py.time.Clock()
        
        self.dry = 0
        self.len = len(self.values.vals)

    def wall(self,a,b):
        wc = (150,150,150)
        y = self.rects[a][b]
        py.draw.rect(self.screen,wc,y)
    
    def path(self,a,b):
        pc = (50,50,50)
        y = self.rects[a][b]
        py.draw.rect(self.screen,pc,y) 
                    
    def write(self,text,t):
        font = py.font.SysFont('timesnewroman',54,1,1)
        img = font.render(text,1,(240,240,0),(60,60,60))
        self.screen.blit(img,t)
    
    def drawpath(self):
        # drawing the board
        self.pathway = []
        for a in range(20):
            for b in range(13):
                c = self.pathw[a][b]
                if c == 0:
                    self.wall(a,b)
                else:
                    self.path(a,b)
                    self.pathway.append(self.rects[a][b])

    def drawbuttons(self):
        # drawing the buttons
        self.screen.blit(self.up,self.up_rect)
        self.screen.blit(self.down,self.down_rect)
        self.screen.blit(self.right,self.right_rect)
        self.screen.blit(self.left,self.left_rect)
        # drawing the player and diamond
        self.screen.blit(self.diamond, self.diamond_rect)
        self.screen.blit(self.player,self.player_rect)

    def checkevents(self):
        # checking events
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                x,y = event.pos
                if self.up_rect.collidepoint(x,y):
                    touch = [self.player_rect.x, self.player_rect.y-50,self.size,self.size]
                    if touch in self.pathway:
                        self.player_rect.y -= 50
    
                if self.down_rect.collidepoint(x,y):
                    touch = [self.player_rect.x, self.player_rect.y+50,self.size,self.size]
                    if touch in self.pathway:
                        self.player_rect.y += 50
                
                if self.right_rect.collidepoint(x,y):
                    touch = [self.player_rect.x+50, self.player_rect.y,self.size,self.size]
                    if touch in self.pathway:
                        self.player_rect.x += 50
    
                if self.left_rect.collidepoint(x,y):
                    touch = [self.player_rect.x-50, self.player_rect.y,self.size,self.size]
                    if touch in self.pathway:
                        self.player_rect.x -= 50

    def checkwin(self):
        # checking player win
        if self.player_rect.colliderect(self.diamond_rect):
            self.screen.blit(self.win,self.win_pos)
            py.display.flip()
            py.time.wait(3000)
            self.player_rect.left = 30
            self.player_rect.top = 100
            if self.dry < self.len-1:
                self.dry += 1
                self.run()
            else:
                self.screen.fill('black')
                py.draw.rect(self.screen,(60,60,60),(30,150,650,900))
                py.draw.rect(self.screen,('green'),(30,150,650,900),5)
                self.end = self.font.render('Excellent',1,('green'))
                self.write('Thanks for playing...',(60,750))
                t = self.font.render('WINNER!',1,('cyan'),(60,60,60))
                self.screen.blit(t,(40,300))
                self.screen.blit(self.end,(40,500))
                py.display.flip()
                py.time.wait(5000)
                sys.exit(py)
        else:
            py.display.flip()

    def run(self):
        self.pathw = self.values.vals[self.dry]
        while True:
            self.screen.fill((0,0,0))
            # writing the title
            self.write('  Find the diamond  ',(50,20))
            self.drawpath()
            self.drawbuttons()
            self.checkevents()
            
            self.checkwin()
            self.clock.tick(60)

class Values:
    def __init__(self):
        self.vals = []
        # determining the pathway        
        self.one = [
            [1,0,0,1,1,1,1,1,0,0,1,1,1],
            [1,1,1,1,0,0,0,1,1,1,1,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,1,1],
            [1,0,1,1,1,0,1,0,1,1,1,0,1],
            [1,1,0,0,1,0,1,1,0,0,1,0,1],
            [0,1,0,1,1,0,0,1,1,1,1,0,1],
            [1,1,0,1,0,1,1,1,0,0,1,0,1],
            [1,0,0,1,1,1,0,1,0,1,1,0,1],
            [1,1,1,0,1,0,1,1,0,1,0,1,1],
            [0,0,1,0,1,0,0,1,1,1,0,1,0],
            [0,1,1,1,1,0,0,1,0,0,1,1,1],
            [0,1,0,1,0,1,1,1,0,1,1,0,1],
            [1,1,0,1,1,1,0,0,1,1,0,1,1],
            [1,0,0,0,0,1,0,1,1,0,1,1,0],
            [1,1,1,1,1,1,0,1,0,1,0,0,1],
            [0,0,1,0,1,0,1,1,0,1,0,0,1],
            [1,1,1,0,1,0,1,0,0,1,1,1,1],
            [1,0,0,0,1,0,1,1,1,0,0,1,0],
            [1,1,0,1,1,1,0,1,0,1,1,1,1],
            [0,1,1,1,0,1,0,1,1,1,0,0,1]
        ]
        self.vals.append(self.one)

me = Path()
me.run()