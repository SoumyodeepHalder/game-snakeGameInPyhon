import pygame
import random
#defining game constants
windowWidth = 800
windowHeight = 600
windowTitle="SNAKE GAME"
gridSize=50
backgroundColor=(0,0,0)
snakeColor=(0,255,0)
foodColor=(255,0,0)
snakeSize=3
snakeSpeed=6
# creating the window
pygame.init()
screen=pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(windowTitle)
clock=pygame.time.Clock()
#functions
def generateFood():
    x = random.randint(0, (windowWidth/gridSize)-1) * gridSize
    y = random.randint(0, (windowHeight/gridSize)-1) * gridSize
    return [x, y]
#initializing the snake, directionQue and food coordinates
snakeCoordinates=[]
directionQue=["down"]
foodCoordinates=[]
for i in range(0, snakeSize):
    snakeCoordinates.insert(0, [0,0])
foodCoordinates=generateFood()
#start the gameloop
running=True
while running:
    #event handling close and directionQue update
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False
            elif event.key==pygame.K_RIGHT and directionQue[0]!="left":
                directionQue.append("right")
            elif event.key==pygame.K_LEFT and directionQue[0]!="right":
                directionQue.append("left")
            elif event.key==pygame.K_DOWN and directionQue[0]!="up":
                directionQue.append("down")
            elif event.key==pygame.K_UP and directionQue[0]!="down":
                directionQue.append("up")
    #update snakeCoordinates and directionQue
    x,y=snakeCoordinates[0]
    if directionQue[0]=="right":
        x+=gridSize
    elif directionQue[0]=="left":
        x-=gridSize
    elif directionQue[0]=="down":
        y+=gridSize
    elif directionQue[0]=="up":
        y-=gridSize
    snakeCoordinates.insert(0, [x,y])
    if len(directionQue)>1:
        directionQue.pop(0)
    #food collision and snake enlargement
    if snakeCoordinates[0][0]==foodCoordinates[0] and snakeCoordinates[0][1]==foodCoordinates[1]:
        foodCoordinates=generateFood()
        for i in snakeCoordinates[0:]:
            if foodCoordinates==i and foodCoordinates==i:
                foodCoordinates=generateFood()
    else:
        snakeCoordinates.pop(-1)
    #wall collision and body collision
    if snakeCoordinates[0][0]<0 or snakeCoordinates[0][0]>windowWidth-1:
        running=False
    elif snakeCoordinates[0][1]<0 or snakeCoordinates[0][1]>windowHeight-1:
        running=False
    else:
        for i in snakeCoordinates[1:]:
            if snakeCoordinates[0][0]==i[0] and snakeCoordinates[0][1]==i[1]:
                running=False
    #draw the screen
    screen.fill(backgroundColor)
    if running==True:
        for x,y in snakeCoordinates:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(x, y, gridSize, gridSize))
        x,y=foodCoordinates
        pygame.draw.circle(screen, foodColor, (x+gridSize/2,y+gridSize/2), gridSize/2)
        pygame.display.flip()
    else:
        font=pygame.font.SysFont("freesarif", 150)
        TEXT_COLOUR = (255,255,255)
        textImg = font.render("GAME OVER", True, TEXT_COLOUR)
        screen.blit(textImg, (80,250))
        pygame.display.update()
        pygame.time.wait(1000)
    pygame.display.update()
    clock.tick(snakeSpeed)