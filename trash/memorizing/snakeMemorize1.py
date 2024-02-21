import pygame
import random
#creating game constants
windowWidth=800
windowHeitht=600
gridSize=50
windowTitle="SNAKE GAME"
backgroundColor=(0,0,0)
snakeColor=(0,255,0)
foodColor=(255,0,0)
snakeSpeed=5
snakeSize=3
#creating window and setting clock
pygame.init()
screen=pygame.display.set_mode((windowWidth,windowHeitht))
pygame.display.set_caption(windowTitle)
clock=pygame.time.Clock()
#functions
def generateFood():
    x=random.randint(0,(windowWidth/gridSize-1))*gridSize
    y=random.randint(0, (windowHeitht/gridSize-1))*gridSize
    return [x,y]
#initialize snakeCoordinates, foodCoordinates, directionQue
snakeCoordinates=[]
for i in range(0, snakeSize):
    snakeCoordinates.insert(0, [0,0])
directionQue=["down"]
foodCoordinates=generateFood()
#start gameLoop
running=True
while running:
    #event handling close and directionQue update
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False
            elif event.key==pygame.K_SPACE:
                pygame.time.wait(5000)
            elif event.key==pygame.K_RIGHT and directionQue[0]!="left":
                directionQue.append("right")
            elif event.key==pygame.K_LEFT and directionQue[0]!="right":
                directionQue.append("left")
            elif event.key==pygame.K_DOWN and directionQue[0]!="up":
                directionQue.append("down")
            elif event.key==pygame.K_UP and directionQue[0]!="down":
                directionQue.append("up")
    #update snakeCoordinates, directionQue
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
    #food collision check and snake enlargement
    if x==foodCoordinates[0] and y==foodCoordinates[1]:
        foodCoordinates=generateFood()
    else:
        snakeCoordinates.pop(-1)
    #wall collision and body collision check
    if x<0 or x>(windowWidth-gridSize) or y<0 or y>(windowHeitht-gridSize):
        running=False
    for i in snakeCoordinates[1:]:
        if snakeCoordinates[0]==i:
            running=False
    #draw snake and food
    screen.fill(backgroundColor)
    if running == True:
        for x,y in snakeCoordinates:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(x, y, gridSize, gridSize))
            x,y=foodCoordinates
            pygame.draw.circle(screen, foodColor, (x+gridSize/2, y+gridSize/2), gridSize/2)
    elif running==False:
        screen.blit(pygame.font.SysFont("freesarif", 150).render("GAME OVER", True, (255,255,255)), (80,250))
        pygame.display.update()
        pygame.time.wait(1000)
    pygame.display.update()
    clock.tick(snakeSpeed)