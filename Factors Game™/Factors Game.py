import pygame as py
import sys, random

py.init()

class FactorsMain:
    def __init__(self):
        # screen resolution
        self.width, self.height = 720, 1340
        self.screen = py.display.set_mode((self.width,self.height))
        
        # range of numbers from which factors are taken
        self.numbers = list(range(-15,16))
        
        # variables that takes in values of factors
        self.r1 = None
        self.r2 = None
        
        # buttons attributes
        self.labels = ('1','2','3','4','5','6','7','8','9','0','-','Ok','<')
        self.buttonsRects = []
        for y in range(5):
            for x in range(3):
                xsize = 170
                ysize = 90
                xx = (180*(x+1))-(xsize/2)
                yy = (750+(100*y))-(ysize/2)
                rect = py.Rect(xx,yy,xsize,ysize)
                self.buttonsRects.append(rect)
        del self.buttonsRects[-1]
        del self.buttonsRects[-2]
                
        # circles attributes
        self.circles = 20
        self.radius = 17
        self.interval = (self.width-40)/self.circles
        self.centers = []
        for r in range(self.circles):
            x = (r+1)*self.interval
            y = 650
            center = (x,y)
            self.centers.append(center)
        self.circleColors = ['gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray']
                      
        # guesses and trials
        self.guesses = self.circles
        self.trials = 0
        
        # correct answer and score
        self.correct = None
        self.scores = 0
        
        # inner loop
        self.inner = None
        
        # variable that receives the touch value
        self.touch = None
        
        # bg image
        self.bg = py.image.load('bg.png')
        self.bg = py.transform.scale(self.bg,(self.width, self.height))
        
        # fonts (aTS6x9ck6h)
        self.font1 = py.font.SysFont('timesnewroman',66,1,0)
        self.font2 = py.font.SysFont(None,92,1,0)
        self.font3 = py.font.SysFont('georgia',64,1,0)
        self.font4 = py.font.SysFont('georgia',84,1,0)
        
        # texts and values
        self.sumText = self.font1.render('Sum',1, 'white')
        self.productText = self.font1.render('Product',1, 'white')
        self.factorsText = self.font1.render('Factors',1, 'white')
        
        self.sum = None
        self.product = None
        self.f1a = None
        self.f1b = None
        self.f2a = None
        self.f2b = None
        
        self.sumValueText = self.font3.render(str(self.sum),1,'blue')
        self.productValueText = self.font3.render(str(self.product),1,'blue')
        self.factor1ValueText = self.font3.render(str(self.f1b),1,'black')
        self.factorsValueText = self.font3.render(str(self.f1b) + str(self.f2b),1,'black')
        self.backText = self.font1.render(' BACK ',1,(0,0,0))
        
        # texts rects
        self.backTextRect = self.backText.get_rect()
        self.backTextRect.centery = 1280
        self.backTextRect.centerx = 130
        self.sumTextRect = py.Rect(self.width/4-150,100,300,90)
        self.productTextRect = py.Rect(self.width*3/4-150,100,300,90)
        self.factorsTextRect = py.Rect(self.width/2-300,400,600,90)
        
        self.sumTextRect2 = self.sumText.get_rect()
        self.productTextRect2 = self.productText.get_rect()
        self.factorsTextRect2 = self.factorsText.get_rect()
        
        self.sumTextRect2.centerx = self.sumTextRect.centerx
        self.sumTextRect2.centery = self.sumTextRect.centery
        self.productTextRect2.centerx = self.productTextRect.centerx
        self.productTextRect2.centery = self.productTextRect.centery
        self.factorsTextRect2.centerx = self.factorsTextRect.centerx
        self.factorsTextRect2.centery = self.factorsTextRect.centery
        
        self.sumValueRect = py.Rect(self.width/4-150,200,300,90)
        self.productValueRect = py.Rect(self.width*3/4-150,200,300,90)
        self.factorsValueRect = py.Rect(self.width/2-300,500,600,90)
        
        self.sumValueRect2 = self.sumValueText.get_rect()
        self.productValueRect2 = self.productValueText.get_rect()
        self.factorsValueRect2 = self.factorsValueText.get_rect()
        
        self.sumValueRect2.centerx = self.sumValueRect.centerx + 45
        self.productValueRect2.centerx = self.productValueRect.centerx + 45
        self.factorsValueRect2.centerx = self.factorsValueRect.centerx
        
        self.sumValueRect2.centery = self.sumValueRect.centery
        self.productValueRect2.centery = self.productValueRect.centery
        self.factorsValueRect2.centery = self.factorsValueRect.centery
        
        ''' END OF GAME ATTRIBUTES '''
        
    def drawValuesRects(self):
        # draws rects for inputs
        for t in (self.sumValueRect, self.productValueRect):
            py.draw.rect(self.screen, (0,0,0),t)
            py.draw.rect(self.screen, (200,0,0),t,1)
            
        py.draw.rect(self.screen, (200,200,200), self.factorsValueRect)
        py.draw.rect(self.screen, (100,100,100), self.factorsValueRect,10)

    def drawCircles(self):
        # draws the circles
        for c in range(len(self.centers)):
            py.draw.circle(self.screen, self.circleColors[c], self.centers[c],self.radius)
            py.draw.circle(self.screen, 'white', self.centers[c], self.radius,1)
     
    def drawSmallCircles(self):
        # draws smaller circles
        circles = self.circles
        radius = self.radius - 3
        interval = (600)/circles
        centers = []
        for r in range(circles):
            x = (r+1)*interval + 40
            y = 700
            center = (x,y)
            centers.append(center)
        for c in range(len(centers)):
            py.draw.circle(self.screen, self.circleColors[c], centers[c],radius)
            py.draw.circle(self.screen, 'white',centers[c], radius,1)
            
    def drawButtons(self):
        # draws the buttons
        for t in self.buttonsRects:
            py.draw.rect(self.screen, (0,0,0),t)
            py.draw.rect(self.screen, 'yellow',t,1)
        py.draw.rect(self.screen, (120,0,0),self.backTextRect)
        py.draw.rect(self.screen, (200,0,0),self.backTextRect,5)

    def drawTexts(self):
        # writes the constant texts on screen
        self.screen.blit(self.sumText, self.sumTextRect2)
        self.screen.blit(self.productText, self.productTextRect2)
        self.screen.blit(self.factorsText, self.factorsTextRect2)
        self.screen.blit(self.backText, self.backTextRect)
        for t in range(13):
            text = self.font2.render(self.labels[t], 1, (200,200,200))
            rect = text.get_rect()
            rect.centerx = self.buttonsRects[t].centerx
            rect.centery = self.buttonsRects[t].centery
            self.screen.blit(text, rect)
        if self.trials != self.guesses:
            self.findFactors()
            
    def findFactors(self):
        ''' gives random values of two factors '''
        self.r1 = random.choice(self.numbers)
        self.r2 = random.choice(self.numbers)
        ''' sets inner loop tu true '''
        self.inner = True
        ''' resets factors value '''
        self.f1a = None
        self.f1b = None
        self.f2a = None
        self.f2b = None
        ''' calculates a new sum and product values '''
        self.sum = self.r1 + self.r2
        self.product = self.r1 * self.r2
        self.drawSumProductValues()
        self.innerLoop()

    def innerLoop(self):
        while self.inner:
            self.checkEvents()
            self.assignValues()
            self.checkWin()
            py.display.flip()
        
    def drawSumProductValues(self):
        self.sumValueText = self.font3.render(str(self.sum),1,'gray')
        self.productValueText = self.font3.render(str(self.product),1,'gray')
        self.screen.blit(self.sumValueText, self.sumValueRect2)
        self.screen.blit(self.productValueText, self.productValueRect2)
        
    def checkEvents(self):
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONUP:
                pos = event.pos
                if self.backTextRect.collidepoint(pos):
                    sys.exit(py)
                elif self.buttonsRects[0].collidepoint(pos):
                    self.touch = '1'
                elif self.buttonsRects[1].collidepoint(pos):
                    self.touch = '2'
                elif self.buttonsRects[2].collidepoint(pos):
                    self.touch = '3'
                elif self.buttonsRects[3].collidepoint(pos):
                    self.touch = '4'
                elif self.buttonsRects[4].collidepoint(pos):
                    self.touch = '5'
                elif self.buttonsRects[5].collidepoint(pos):
                    self.touch = '6'
                elif self.buttonsRects[6].collidepoint(pos):
                    self.touch = '7'
                elif self.buttonsRects[7].collidepoint(pos):
                    self.touch = '8'
                elif self.buttonsRects[8].collidepoint(pos):
                    self.touch = '9'
                elif self.buttonsRects[9].collidepoint(pos):
                    self.touch = '0'
                elif self.buttonsRects[10].collidepoint(pos):
                    self.touch = '-'
                elif self.buttonsRects[11].collidepoint(pos):
                    self.touch = '>'
                elif self.buttonsRects[12].collidepoint(pos):
                    self.touch = 'del'
                else:
                    pass    
    
    def assignValues(self):
        if self.touch != None:
            # ASSIGNING VALUES TO self.f1b AND self.f2b
            if self.f1a == None and self.f1b == None:
                if self.touch == '>' or self.touch == 'del':
                    pass
                else:
                    self.f1b = self.touch
                self.displayf1b()
                
            elif self.f1a == None and self.f1b != None:
                if self.touch == '-':
                    pass
                elif self.touch == 'del':
                    if len(self.f1b) == 1:
                        self.f1b = None
                    else:
                        self.f1b = self.f1b[:-1]
                elif self.touch == '>':
                    if self.f1b != '-' and len(self.f1b) < 5:
                        self.f1a = int(self.f1b)
                        self.f1b += ' and '
                    else:
                        pass
                else:
                    if len(self.f1b) < 5:
                        self.f1b += self.touch
                self.displayf1b()
            
            elif self.f1a != None and self.f2b == None:
                if self.touch == '>':
                    pass
                elif self.touch == 'del':
                    self.f1b = self.f1b[:-5]
                    self.f1a = None
                    l = len(self.f1b)
                    if l < 1 or self.f1b == '-':
                        self.f1b = None
                    else:
                        pass
                else:
                    self.f2b = self.touch
                self.displayf1bf2b()
                
            elif self.f1a != None and self.f2b != None:
                if self.touch == '-':
                    pass
                elif self.touch == 'del':
                    if len(self.f2b) == 1:
                        self.f2b = None
                    else:
                        self.f2b = self.f2b[:-1]
                elif self.touch == '>':
                    if self.f2b != '-':
                        self.f2a = int(self.f2b)
                    else:
                        pass
                else:
                    if len(self.f2b) < 5:
                        self.f2b += self.touch
                self.displayf1bf2b()
        self.touch = None
    
    def checkWin(self):
        # CHECKING WIN OR LOOSE
        if self.f2a != None:
            self.inner = False
            sum = self.f1a + self.f2a
            product = self.f1a * self.f2a
            if sum == self.sum and product == self.product:
                # player is correct
                self.circleColors[self.trials] = 'green'
                self.scores += 1
                self.trials += 1
                self.run()
            else:
                # player is wrong
                self.circleColors[self.trials] = 'red'
                self.drawCircles()
                py.display.flip()
                py.time.wait(1000)
                
                self.displayCorrectAnswer()
                py.display.flip()
                py.time.wait(2000)
                self.trials += 1
                self.run()
        else:
            pass

    def displayf1b(self):
        if self.f2b != None:
            text = self.f1b + self.f2b
        else:
            text = self.f1b
        self.factor1ValueText = self.font3.render(text,1,'black')
        self.factorsValueRect2 = self.factor1ValueText.get_rect()
        self.factorsValueRect2.centerx = self.factorsValueRect.centerx
        self.factorsValueRect2.centery = self.factorsValueRect.centery
        py.draw.rect(self.screen, (200,200,200), self.factorsValueRect)
        py.draw.rect(self.screen, (100,100,100), self.factorsValueRect,10)
        if self.f1b != None:
            self.screen.blit(self.factor1ValueText, self.factorsValueRect2)
        
    def displayf1bf2b(self):
        if self.f2b != None:
            text = self.f1b + self.f2b
        else:
            text = self.f1b
        self.factorsValueText = self.font3.render(text,1,'black')
        self.factorsValueRect2 = self.factorsValueText.get_rect()
        py.draw.rect(self.screen, (200,200,200), self.factorsValueRect)
        py.draw.rect(self.screen, (100,100,100), self.factorsValueRect,10)
        self.displayf1b()
        self.factorsValueRect2.centerx = self.factorsValueRect.centerx
        self.factorsValueRect2.centery = self.factorsValueRect.centery
        if self.f2b != None:
            self.screen.blit(self.factorsValueText, self.factorsValueRect2)
       
    def displayCorrectAnswer(self):
        py.draw.rect(self.screen, 'red',self.factorsValueRect)
        py.draw.rect(self.screen, 'green',self.factorsValueRect,4)
        self.correct = self.font3.render(str(self.r1) + ' and '+ str(self.r2),1,'green')
        self.screen.blit(self.correct, self.factorsValueRect2)
    
    def endGame(self):
        self.screen.blit(self.bg,(0,0))
        rect = py.Rect(0,0,600,900)
        rect.centerx = self.width / 2
        rect.centery = self.height / 2
        py.draw.rect(self.screen, (10,10,10),rect)
        py.draw.rect(self.screen, 'green',rect,1)
        self.drawSmallCircles()
        score = round(self.scores / self.guesses * 100)
        
        statText = self.font4.render(' GAME STATS ', 1, 'yellow', (60,30,30))
        if score < 50:
            scoreText = self.font4.render('> ' +str(score) + ' % ', 1, 'red')
        elif score < 70:
            scoreText = self.font4.render('> ' +str(score) + ' % ', 1, 'white')
        else:
            scoreText = self.font4.render('> ' +str(score) + ' % ', 1, 'green')
        hello = self.font4.render('> Your score:',1,'gray')
        rect1 = statText.get_rect()
        rect2 = scoreText.get_rect()
        rect3 = hello.get_rect()
        rect1.centerx = rect2.centerx = rect3.centerx = self.width / 2
        rect1.centery = 400
        rect2.centery = 800
        rect3.centery = 600
        self.screen.blit(statText, rect1)
        self.screen.blit(scoreText, rect2)
        self.screen.blit(hello, rect3)
        
    def reset(self):
        self.circleColors = ['gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray']
        self.trials = 0
        self.scores = 0
    
    def drawScreen(self):
        self.drawCircles()
        self.drawValuesRects()
        self.drawButtons()
        self.drawTexts()
        
    def run(self):
        while self.trials < self.guesses:
            self.screen.blit(self.bg,(0,0))
            self.drawScreen()
            
            py.display.flip()
        self.endGame()
        py.display.flip()
        py.time.wait(5000)
        self.reset()
        self.run()
        # write winner then go back to main menu
            
main = FactorsMain()
main.run()

''' back button and the menu screen'''