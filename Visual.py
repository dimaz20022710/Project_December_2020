import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the screen
# Top-left coordinate
x1 = 0
y1 = 0
# Top-right coordinate
x2 = screen_width
y2 = screen_height
N = 10  # The number of lines vertically and horizontally, respectively
white_color = (255, 255, 255)
rect(screen, white_color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)  # Width of one cell
x = x1 + h
w = (y2 - y1) // (N + 1)  # Height of one cell
y = y1 + w
for i in range(N):
    """ This loop draws N horizontal and vertical lines """
    line(screen, white_color, (x, y1), (x, y2))  # Vertical lines
    x += h
    line(screen, white_color, (x1, y), (x2, y))  # Horizontal lines
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
