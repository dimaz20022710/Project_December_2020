import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

x1 = 0
y1 = 0
x2 = screen_width
y2 = screen_height
N = 10
color = (255, 255, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
w = (y2-y1) // (N + 1)
y = y1 + w
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h
    line(screen, color, (x1, y), (x2, y))
    y += w
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
