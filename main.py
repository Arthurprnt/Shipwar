from betterpygame import *
import pygame
from func import *
pygame.init()

SCREEN = pygame.display.set_mode()
X, Y = SCREEN.get_size()
pygame.display.set_caption('ShipWar')
ICON = pygame.image.load('assets/icon.png')
pygame.display.set_icon(ICON)
pygame.display.flip()

FOND = pygame.image.load('assets/background.png')
FOND = pygame.transform.scale(FOND, (X, Y))
FONT = pygame.font.Font('assets/Montserrat-Black.ttf', 55)
LOGO_MENU = Pygameimage("Logo menu", "assets/menu_name.png")
LOGO_MENU.multiplesize(0.6, X)
LOGO_MENU.center((X, Y), "x")
LOGO_MENU.add_y(Y/10)
PLAY_BUTTON = Pygameimage("Play button", "assets/play_button.png")
PLAY_BUTTON.multiplesize(0.5, X)
PLAY_BUTTON.center((X, Y), "all")
PLAY_BUTTON.add_y(Y/12)
CLEAR_BUTTON = Pygameimage("Clear button", "assets/trash_button.png")
CLEAR_BUTTON.multiplesize(0.4, X)
CLEAR_BUTTON.set_pos(1670, 340)
START_BUTTON = Pygameimage("Start button", "assets/play_button.png")
START_BUTTON.multiplesize(0.4, X)
START_BUTTON.set_pos(1670, 540)
MAIN_GRID = Pygameimage("Main grid", "assets/grid.png")
MAIN_GRID.multiplesize(1.5, X)
MAIN_GRID.center((X, Y), "all")
GRID_P1 = Pygameimage("Grid player 1", "assets/grid.png")
GRID_P1.multiplesize(1.5, X)
GRID_P1.set_defaultpos(pixelinhd(430, X), pixelinhd(345, X))
GRID_P2 = Pygameimage("Grid player 2", "assets/grid.png")
GRID_P2.multiplesize(1.5, X)
GRID_P2.set_defaultpos(pixelinhd(1380, X), pixelinhd(345, X))
PLAYER1_LOGO = Pygameimage("Player 1 logo", "assets/player1.png")
PLAYER1_LOGO.multiplesize(1, X)
PLAYER1_LOGO.set_defaultpos(pixelinhd(490, X), pixelinhd(1135, X))
PLAYER2_LOGO = Pygameimage("Player 2 logo", "assets/player2.png")
PLAYER2_LOGO.multiplesize(1, X)
PLAYER2_LOGO.set_defaultpos(pixelinhd(1419, X), pixelinhd(1135, X))
SHIP_FIVE = Pygameimage("5x1", "assets/5x1.png")
SHIP_FIVE.multiplesize(1.5, X)
SHIP_FIVE.set_defaultpos(pixelinhd(304, X), pixelinhd(691, X))
SHIP_FOUR = Pygameimage("4x1", "assets/4x1.png")
SHIP_FOUR.multiplesize(1.5, X)
SHIP_FOUR.set_defaultpos(pixelinhd(334.7, X), pixelinhd(607, X))

EMPTY_CASE = []
COORD_EMPTY_CASE_P2 = []
TOUCHED_CASE = []
COORD_TOUCHED_CASE_P2 = []

LIST_SHIP = [SHIP_FIVE, SHIP_FOUR]
SHIP_COORD_P1 = {}
"""
0: No shot made
1: Shot here but no ship
2: Shot here and ship
"""
GRID_LIST_P1 = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]
GRID_LIST_P2 = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]

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
        SCREEN.blit(CLEAR_BUTTON.image, CLEAR_BUTTON.position)
        if len(SHIP_COORD_P1) == len(LIST_SHIP):
            SCREEN.blit(START_BUTTON.image, START_BUTTON.position)
    elif stats == 2:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, "Au tour du Joueur1 de jouer.", FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        for i in EMPTY_CASE:
            SCREEN.blit(i.image, i.position)
        for i in TOUCHED_CASE:
            SCREEN.blit(i.image, i.position)

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
                elif stats == 1:
                    for i in LIST_SHIP:
                        if colide(i, event.pos) and stats == 1 and isclickable(LIST_SHIP):
                            # Ship is clicked to be placed next
                            i.clicked = True
                        elif i.clicked and colide(MAIN_GRID, (event.pos[0]+pixelinhd(37, X), event.pos[1]+pixelinhd(37, X))) and i.position[0]+i.size[0] < MAIN_GRID.position[0]+MAIN_GRID.size[0] and i.position[1]+i.size[1] < MAIN_GRID.position[1]+MAIN_GRID.size[1]:
                            # Ship is placed
                            i.clicked = False
                            i.set_pos(roundat(i.position[0], multiplypixelinhd(1.5, 50, X))+pixelinhd(5, X), roundat(i.position[1], multiplypixelinhd(1.5, 50, X))-pixelinhd(30, X))
                            SHIP_COORD_P1[i.name] = []
                            x = i.position[0]-pixelinhd(5, X)
                            nb_x = 1
                            while x > MAIN_GRID.position[0]-pixelinhd(5, X):
                                x = x-multiplypixelinhd(1.5, 50, X)
                                nb_x = nb_x + 1
                            y = i.position[1]+pixelinhd(30, X)
                            nb_y = 1
                            while y > MAIN_GRID.position[1]+pixelinhd(30, X):
                                y = y - multiplypixelinhd(1.5, 50, X)
                                nb_y = nb_y + 1
                            SHIP_COORD_P1[i.name] = []
                            for ii in range(int(i.name[0])):
                                SHIP_COORD_P1[i.name].append((nb_x, nb_y))
                                nb_x = nb_x + 1
                        elif colide(i, event.pos):
                            i.clicked = False
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            del SHIP_COORD_P1[i.name]
                    if colide(CLEAR_BUTTON, event.pos):
                        for i in LIST_SHIP:
                            i.clicked = False
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            if i.name in SHIP_COORD_P1.keys():
                                del SHIP_COORD_P1[i.name]
                    elif colide(START_BUTTON, event.pos):
                        SHIP_COORD_P2 = generatecoord()
                        stats = 2
                elif stats == 2:
                    if colide(GRID_P2, event.pos):
                        x1 = roundat(event.pos[0], multiplypixelinhd(1.5, 50, X))-multiplypixelinhd(1.5, 29, X)
                        x = roundat(event.pos[0], multiplypixelinhd(1.5, 50, X))
                        y1 = roundat(event.pos[1], multiplypixelinhd(1.5, 50, X))-multiplypixelinhd(1.5, 20, X)
                        y = roundat(event.pos[1], multiplypixelinhd(1.5, 50, X))
                        nb_x = 0
                        nb_y = 0
                        while x > GRID_P2.position[0]:
                            x = x-multiplypixelinhd(1.5, 50, X)
                            nb_x = nb_x + 1
                        while y > GRID_P2.position[1]:
                            y = y-multiplypixelinhd(1.5, 50, X)
                            nb_y = nb_y + 1
                        case_exist = False
                        if nb_x > 0 and nb_y > 0:
                            for i in SHIP_COORD_P2.values():
                                for ii in i:
                                    if ii == (nb_x, nb_y):
                                        case_exist = True
                            if ((nb_x, nb_y) in COORD_TOUCHED_CASE_P2) == False and ((nb_x, nb_y) in COORD_EMPTY_CASE_P2) == False and case_exist:
                                TOUCHED_CASE.append(Pygameimage("Something case", "assets/something_touched.png"))
                                TOUCHED_CASE[-1].multiplesize(1.5, X)
                                TOUCHED_CASE[-1].set_defaultpos(x1, y1)
                                COORD_TOUCHED_CASE_P2.append((nb_x, nb_y))
                            elif ((nb_x, nb_y) in COORD_TOUCHED_CASE_P2) == False and ((nb_x, nb_y) in COORD_EMPTY_CASE_P2) == False:
                                EMPTY_CASE.append(Pygameimage("Empty case", "assets/nothing_touched.png"))
                                EMPTY_CASE[-1].multiplesize(1.5, X)
                                EMPTY_CASE[-1].set_defaultpos(x1, y1)
                                COORD_EMPTY_CASE_P2.append((nb_x, nb_y))

    pygame.display.flip()

pygame.quit()