import pygame
import sys

pygame.init()

longueur = 600
largeur = 600
screen = pygame.display.set_mode((longueur,largeur))
pygame.display.set_caption("morpion by antho")

green = (70,176,119)
red = (134,56,65)
lineSize = 15
background = screen.fill(red)

def Grid():
    for x in range(1,4):
        pygame.draw.line(screen,green,(0,x*205), (longueur,x*205), lineSize)
        pygame.draw.line(screen,green,(x*205,0),(x*205,largeur), lineSize)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(red)
    Grid()
    pygame.display.update()