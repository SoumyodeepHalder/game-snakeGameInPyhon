# organizing code
# first draw the Snake
# if the snake have eaten a food then create a new food
# else cut the tail of the snake
# draw the food
# if collision happened then display game over

import pygame
import random

GAME_WIDTH = 800
GAME_HEIGHT = 600
SPEED = 10
SPACE_SIZE = 20
BODY_PARTS = 9
SNAKE_COLOR = (0,255,0)
FOOD_COLOR = (255,0,0)
directionQue = ["down"]
snakeCoordinates = []
snakeEnlargement =False
foodCoordinates = []
snakeSize=3
playAgain =False

def updateSnakeDirection(key, direction):
    if key == pygame.K_UP and direction != "down":
        direction = "up"
    elif key == pygame.K_DOWN and direction != "up":
        direction = "down"
    elif key == pygame.K_LEFT and direction != "right":
        direction = "left"
    elif key == pygame.K_RIGHT and direction != "left":
        direction = "right"
    return direction


def collisionDetection():
    x,y = snakeCoordinates[0]
    if x<0 or x> GAME_WIDTH or y<0 or y>GAME_HEIGHT:
        return True
    for i in snakeCoordinates[1:]:
        if x == i[0] and y == i[1]:
            return True

def generateRandomFoodPosition():
    x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
    y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
    return [x, y]

def snake():
    x,y = snakeCoordinates[0]
    if directionQue[0] == "up":
        y-=SPACE_SIZE
    elif directionQue[0] == "down":
        y+=SPACE_SIZE
    elif directionQue[0] == "right":
        x+=SPACE_SIZE
    elif directionQue[0] == "left":
        x-=SPACE_SIZE
        
    if len(directionQue)>1:
        directionQue.pop(0)
    snakeCoordinates.insert(0, [x,y])

    for x,y in snakeCoordinates:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x,y,SPACE_SIZE,SPACE_SIZE))
    
def food(foodCoordinates):
    if snakeCoordinates[0]==foodCoordinates:
        foodCoordinates=generateRandomFoodPosition()
    else:
        del snakeCoordinates[-1]
    x,y=foodCoordinates
    pygame.draw.circle(screen, FOOD_COLOR, (x+SPACE_SIZE/2,y+SPACE_SIZE/2), SPACE_SIZE/2)
    pygame.display.flip()
    return foodCoordinates

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

for i in range(0, BODY_PARTS):
    snakeCoordinates.append([0,0])
foodCoordinates = generateRandomFoodPosition()
clock= pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_q:
                running =False
            elif event.key == pygame.K_p:
                playAgain =True
            directionQue.append(updateSnakeDirection(event.key, directionQue[-1]))
    
    screen.fill((0,0,0))
    snake()
    foodCoordinates=food(foodCoordinates)
    if collisionDetection():
        font=pygame.font.SysFont("freesarif", 150)
        TEXT_COLOUR = (255,255,255)
        textImg = font.render("GAME OVER", True, TEXT_COLOUR)
        screen.blit(textImg, (80,250))
        pygame.display.update()
        pygame.time.wait(1000)
        running = False

    pygame.display.update()
    clock.tick(SPEED)