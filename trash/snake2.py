# snake game with direction que
import pygame

GAME_WIDTH = 800
GAME_HEIGHT = 600
SPEED = 5
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = (0,255,0)
FOOD_COLOR = (255,0,0)
directionQue = ["down"]
snakeCoordinates = []
snakeSize=3

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

def updateSnakeCoordinate():
    x,y = snakeCoordinates[0]
    if directionQue[0] == "up":
        y-=SPACE_SIZE
    if directionQue[0] == "down":
        y+=SPACE_SIZE
    if directionQue[0] == "right":
        x+=SPACE_SIZE
    if directionQue[0] == "left":
        x-=SPACE_SIZE
    del snakeCoordinates[-1]
    snakeCoordinates.insert(0, [x,y])

def drawSnake():
    for x,y in snakeCoordinates:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x,y,SPACE_SIZE,SPACE_SIZE))

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

for i in range(0, BODY_PARTS):
    snakeCoordinates.append([0,0])

clock= pygame.time.Clock()
running = True
while running:
    # print("while loop running")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_q:
                running =False
            directionQue.append(updateSnakeDirection(event.key, directionQue[-1]))
    
    updateSnakeCoordinate()
    if len(directionQue)>1:
        directionQue.pop(0)
    screen.fill((0,0,0))
    drawSnake()
    pygame.display.update()
    clock.tick(SPEED)