import pygame, sys
from settings import *
from level import Level

#pygame setup
pygame.init()

#icon and title
pygame.display.set_caption("Witchy Witch")
icon= pygame.image.load("graphics/witch.png")
pygame.display.set_icon(icon)

screen= pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(levelmap,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((173,216,230))
    level.run()
    pygame.display.update()
    clock.tick(60)
