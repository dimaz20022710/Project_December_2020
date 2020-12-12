import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

myimage = pygame.image.load("toy_sniper.png")

game_over = False
while game_over == False:
    for event in pygame.get():
        if event.type == pygame.KEYDOWN():
            game_over = True
    screen.blit(myimage, (100, 100))
    pygame.display.flip()
