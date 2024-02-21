import pygame
import random

GAME_WIDTH = 800
GAME_HEIGHT = 600
SPEED = 5
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = (0,255,0)
FOOD_COLOR = (255,0,0)
BACKGROUND_COLOR = "000000"
score = 0
direction = "down"
snakeCoordinates = []


def snake(snakeCoordinates):
    for x,y in snakeCoordinates:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x,y,SPACE_SIZE,SPACE_SIZE))

def food():
    x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
    y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
    pygame.draw.circle(screen, FOOD_COLOR, (x+SPACE_SIZE/2,y+SPACE_SIZE/2), 25)
    pygame.display.flip()

def next_turn(snake, food):
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass


pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

for i in range(0, BODY_PARTS):
    snakeCoordinates.append([0,0])

food()
clock= pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
    
    screen.fill((0,0,0))
    x,y = snakeCoordinates[0]
    if direction == "up":
        y-=SPACE_SIZE
    if direction == "down":
        y+=SPACE_SIZE
    if direction == "right":
        x+=SPACE_SIZE
    if direction == "left":
        x-=SPACE_SIZE

    snakeCoordinates.insert(0, [x,y])
    del snakeCoordinates[-1]
    snake(snakeCoordinates)
    pygame.display.update()
    clock.tick(SPEED)