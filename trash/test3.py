#window gets resized from (800,800) to (800,600) by pressing q

import pygame

pygame.init()
screen=pygame.display.set_mode((800,800))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False
            if event.key==pygame.K_b:
                screen = pygame.display.set_mode((800,600))