import pygame,sys

pygame.init()


screen = pygame.display.set_mode(((750,750)))

/create caption
pygame.display.set_caption("retro snake")
clock =  pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()