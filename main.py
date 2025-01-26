import pygame


background_colour = (000,000,000)
screen = pygame.display.set_mode((600, 600))
screen.fill(background_colour)
pygame.display.set_caption('Isometric Adventure')
icon = pygame.image.load('grass_block.png')
pygame.display.set_icon(icon)
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT: running = False

