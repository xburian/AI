import pygame


def start_gui(defaults: str):
    pygame.init()
    black = (0, 0, 0)
    screen = pygame.display.set_mode((1200, 600))
    screen.fill((255, 255, 255))

    myFont = pygame.font.SysFont("Times New Roman", 18)

    label = myFont.render("Defaults:", True, black)
    text = myFont.render(defaults, True, black)

    screen.blit(label, (10, 20))
    screen.blit(text, (10, 40))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        pygame.display.flip()
