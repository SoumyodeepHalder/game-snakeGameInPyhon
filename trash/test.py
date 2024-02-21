import pygame

foodCoordinates = []

def func1():
    foodCoordinates=[1,2]
    return foodCoordinates

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")
running = True
while running:
    # print("while loop running")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                foodCoordinates= func1()
                print(foodCoordinates)
    