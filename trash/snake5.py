# adding score and playAgain button
import pygame
import random

windowWidth = 800
windowHeight = 600
windowTitle = "Snake Game"
windowColor=(0,0,0)
gridSize=20
snakeCoordinates=[]
snakeSize=3
snakeSpeed=5
snakeColor=(0,255,0)
foodColor=(255,0,0)
directionQue=["down"]
clock = pygame.time.Clock()

import pygame
pygame.init()
screen = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption(windowTitle)

# def generateRandomFoodPosition():
#     x=random.randint(0, windowWidth)
#     y=random.randint((0, windowWidth))
#     return [x,y]
def generateRandomFoodPosition():
    x = random.randint(0, (windowWidth/gridSize)-1) * gridSize
    y = random.randint(0, (windowHeight/gridSize)-1) * gridSize
    return [x, y]

def snake():
    x,y = snakeCoordinates[0]
    if directionQue[0]=="left":
        x-=gridSize
    elif directionQue[0]=="right":
        x+=gridSize
    elif directionQue[0]=="up":
        y-=gridSize
    elif directionQue[0]=="down":
        y+=gridSize
    snakeCoordinates.insert(0, [x,y])
    if len(directionQue)>1:
        directionQue.pop(0)

    for x,y in snakeCoordinates:
        pygame.draw.rect(screen, snakeColor, pygame.Rect(x,y,gridSize,gridSize))

def food(foodCoordinates):
    if snakeCoordinates[0]==foodCoordinates:
        foodCoordinates=generateRandomFoodPosition()
    else:
        snakeCoordinates.pop(-1)
    x,y=foodCoordinates
    pygame.draw.circle(screen, foodColor, (x+gridSize/2,y+gridSize/2), gridSize/2)
    pygame.display.flip()
    return foodCoordinates

def collision():
    x,y=snakeCoordinates[0]
    if x<0 or x>windowWidth:
        return True
    elif y<0 or y>windowWidth:
        return True
    for i in snakeCoordinates[1:]:
        if x==i[0] and y==i[1]:
            return True
    
for i in range(0, snakeSize):
    snakeCoordinates.append([0,0])
foodCoordinates=generateRandomFoodPosition()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            direction=directionQue[-1]
            if event.key==pygame.K_q:
                running=False
            elif event.key==pygame.K_LEFT and direction != "right":
                directionQue.append("left")
            elif event.key==pygame.K_RIGHT and direction != "left":
                directionQue.append("right")
            elif event.key==pygame.K_DOWN and direction != "up":
                directionQue.append("down")
            elif event.key==pygame.K_UP and direction != "down":
                directionQue.append("up")
    
    screen.fill(windowColor)
    snake()
    foodCoordinates=food(foodCoordinates)
    if collision():
        font=pygame.font.SysFont("freesarif", 150)
        TEXT_COLOUR = (255,255,255)
        textImg = font.render("GAME OVER", True, TEXT_COLOUR)
        screen.blit(textImg, (80,250))
        pygame.display.update()
        pygame.time.wait(1000)
        running = False
    pygame.display.update()
    clock.tick(5)