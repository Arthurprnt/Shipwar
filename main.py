from betterpygame import *
import pygame
pygame.init()

SCREEN = pygame.display.set_mode()
X, Y = SCREEN.get_size()
pygame.display.set_caption('ShipWar')
ICON = pygame.image.load('assets/icon.png')
pygame.display.set_icon(ICON)
pygame.display.flip()

FOND = pygame.image.load('assets/background.png')
FOND = pygame.transform.scale(FOND, (X, Y))
LOGO_MENU = Pygameimage("assets/menu_name.png")
LOGO_MENU.multiplesize(0.6, X)
LOGO_MENU.center((X, Y), "x")
LOGO_MENU.add_y(Y/10)
PLAY_BUTTON = Pygameimage("assets/play_button.png")
PLAY_BUTTON.multiplesize(0.5, X)
PLAY_BUTTON.center((X, Y), "all")
PLAY_BUTTON.add_y(Y/12)
MAIN_GRID = Pygameimage("assets/grid.png")
MAIN_GRID.multiplesize(1.5, X)
MAIN_GRID.center((X, Y), "all")
print(MAIN_GRID.size)
SHIP_FIVE = Pygameimage("assets/5x1.png")
SHIP_FIVE.multiplesize(1.5, X)
SHIP_FIVE.set_defaultpos(pixelinhd(304, X), pixelinhd(691, X))
SHIP_FOUR = Pygameimage("assets/4x1.png")
SHIP_FOUR.multiplesize(1.5, X)
SHIP_FOUR.set_defaultpos(pixelinhd(334.7, X), pixelinhd(607, X))

LIST_SHIP = [SHIP_FIVE, SHIP_FOUR]

RUNNING = True
stats = 0
"""
Diffrents stats:
MENU: 0
PLACE_SHIPS: 1
PLAYER_1_PLAY: 2
PLAYER_1_RESULT: 3
PLAYER_2_PLAY: 4
PLAYER_2_RESULT: 5
END: 6
"""

while RUNNING:

    SCREEN.blit(FOND, (0, 0))

    if stats == 0:
        SCREEN.blit(LOGO_MENU.image, LOGO_MENU.position)
        SCREEN.blit(PLAY_BUTTON.image, PLAY_BUTTON.position)
    elif stats == 1:
        for i in LIST_SHIP:
            if i.clicked:
                try:
                    i.set_pos(event.pos[0]-pixelinhd(37, X), event.pos[1]-pixelinhd(37, X))
                except:
                    pass
        SCREEN.blit(MAIN_GRID.image, MAIN_GRID.position)
        SCREEN.blit(SHIP_FIVE.image, SHIP_FIVE.position)
        SCREEN.blit(SHIP_FOUR.image, SHIP_FOUR.position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if colide(PLAY_BUTTON, event.pos) and stats == 0:
                    stats = 1
                for i in LIST_SHIP:
                    if colide(i, event.pos) and stats == 1 and isclickable(LIST_SHIP):
                        i.clicked = True
                    elif i.clicked and colide(MAIN_GRID, (event.pos[0]+pixelinhd(37, X), event.pos[1]+pixelinhd(37, X))) and i.position[0]+i.size[0] < MAIN_GRID.position[0]+MAIN_GRID.size[0] and i.position[1]+i.size[1] < MAIN_GRID.position[1]+MAIN_GRID.size[1]:
                        i.clicked = False
                        i.set_defaultpos(roundat(i.position[0], 75)+pixelinhd(5, X), roundat(i.position[1], 75)-pixelinhd(29, X))
                        print(i.default_pos)
                    else:
                        i.clicked = False
                        i.set_pos(i.default_pos[0], i.default_pos[1])

    pygame.display.flip()

pygame.quit()
