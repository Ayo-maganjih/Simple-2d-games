# Memory puzzle
import random, pygame, sys
from pygame.locals import *

fps = 30 # frames per second
wwidth = 1200
wheight = 600
revealSpeed = 10
box_size = 80
gap_size = 20
bwidth = 10
bheight = 7

assert (bwidth * bheight) % 2 == 0, 'Board needs an even number of boxes'

xmargin = int((wwidth - (bwidth * (box_size + gap_size)))/2+10)
ymargin = -50

# colors
black = (0,0,0)
gray = (60,60,60)
navyblue = (60,60,100)
white = (255, 255, 255)
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = ( 0, 255, 255)

bgcolor = black
lightbgcolor = navyblue
boxcolor = gray
highlightcolor = (80,150,0)

donut = 'donut'
square = 'square'
diamond = 'diamond'
lines = 'lines'
oval = 'oval'

allcolors = (red, green, blue, yellow, orange, purple, cyan)
allshapes = (donut, square, diamond, lines, oval)

assert len(allcolors) * len(allshapes) * 2 >= bwidth * bheight, 'board too big for color/shapes defined'

def main():
    global fpsClock, screen
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((wwidth, wheight))
    
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory game')
    
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    
    firstSelection = None
    screen.fill(bgcolor)
    startGameAnimation(mainBoard)
    
    while True:
        mouseClicked = False
        
        screen.fill(bgcolor)
        drawBoard(mainBoard, revealedBoxes)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True
                
                if firstSelection == None:
                    firstSelection = (boxx, boxy)
                else:
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(100)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]),(boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)
                        
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)
                        
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        
                        startGameAnimation(mainBoard)
                    firstSelection = None
                    
        pygame.display.update()
        fpsClock.tick(fps)
        
def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(bwidth):
        revealedBoxes.append([val] * bheight)
    return revealedBoxes
    
def getRandomizedBoard():
    icons = []
    for color in allcolors:
        for shape in allshapes:
            icons.append((shape, color))
    random.shuffle(icons)
    numIconsUsed = int(bwidth * bheight / 2)
    icons = icons[: numIconsUsed] * 2
    random.shuffle(icons)
    
    board = []
    for x in range(bwidth):
        column = []
        for y in range(bheight):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board
        
def splitIntoGroupsOf(groupSize, theList):
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (box_size + gap_size) + xmargin
    top = boxy * (box_size + gap_size) - 4*ymargin
    return (left, top)
    
def getBoxAtPixel(x, y):
    for boxx in range(bwidth):
        for boxy in range(bheight):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, box_size, box_size)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(box_size * 0.25)
    half = int(box_size * 0.5)
    
    left, top = leftTopCoordsOfBox(boxx, boxy)
    
    if shape == donut:
        pygame.draw.circle(screen, color, (left + half, top + half), half - 5)
        pygame.draw.circle(screen, bgcolor, (left + half, top + half), quarter - 5)
        
    elif shape == square:
        pygame.draw.rect(screen, color, (left + quarter, top + quarter, box_size - half, box_size - half))
    
    elif shape == diamond:
        pygame.draw.polygon(screen, color, ((left + half, top),(left + box_size - 1, top + half),(left + half, top + box_size - 1),(left, top + half)))
        
    elif shape == lines:
        for i in range(0, box_size, 4):
            pygame.draw.line(screen, color, (left, top + i), (left + i, top))
            pygame.draw.line(screen, color, (left + i, top + box_size - 1), (left + box_size - 1, top + i))
    
    elif shape == oval:
        pygame.draw.ellipse(screen, color, (left, top + quarter, box_size, half))
        

def getShapeAndColor(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]
    
def drawBoxCovers(board, boxes, coverage):
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(screen, bgcolor, (left, top, box_size, box_size))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        
        if coverage > 0:
            pygame.draw.rect(screen, boxcolor, (left, top, coverage, box_size))
    pygame.display.update()
    fpsClock.tick(fps)
    
def revealBoxesAnimation(board, boxesToReveal):
    for coverage in range(box_size, (-revealSpeed) - 1, - revealSpeed):
        drawBoxCovers(board, boxesToReveal, coverage)
    
def coverBoxesAnimation(board, boxesToCover):
    for coverage in range(0, box_size + revealSpeed, revealSpeed):
        drawBoxCovers(board, boxesToCover, coverage)
    
def drawBoard(board, revealed):
    for boxx in range(bwidth):
        for boxy in range(bheight):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(screen, boxcolor, (left, top, box_size, box_size))
            else:
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)
                
def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(screen, highlightcolor, (left - 5, top - 5, box_size + 10, box_size + 10),4)
    
def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []

    for x in range(bwidth):

        for y in range(bheight):

            boxes.append( (x, y) )

    random.shuffle(boxes)

    boxGroups = splitIntoGroupsOf(8, boxes)



    drawBoard(board, coveredBoxes)

    for boxGroup in boxGroups:

        revealBoxesAnimation(board, boxGroup)

        coverBoxesAnimation(board, boxGroup)

        

def gameWonAnimation(board):

    coveredBoxes = generateRevealedBoxesData(True)

    color1 = lightbgcolor
    color2 = bgcolor
 

    for i in range(13):

        color1, color2 = color2, color1 
        screen.fill(color1)

        drawBoard(board, coveredBoxes)

        pygame.display.update()

        pygame.time.wait(300)



def hasWon(revealedBoxes):

    for i in revealedBoxes:

        if False in i:

            return False
    return True

 

if __name__ == '__main__':
    main()