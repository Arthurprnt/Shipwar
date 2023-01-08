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

DEBUG = False
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
CLEAR_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(340, X))
RANDOM_BUTTON = Pygameimage("Random button", "assets/randomise_button.png")
RANDOM_BUTTON.multiplesize(0.4, X)
RANDOM_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(540, X))
START_BUTTON = Pygameimage("Start button", "assets/play_button.png")
START_BUTTON.multiplesize(0.4, X)
START_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(740, X))
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
PLAYER2_LOGO.set_defaultpos(pixelinhd(1445, X), pixelinhd(1135, X))
SHIP_FIVE = Pygameimage("5x1", "assets/5x1.png")
SHIP_FIVE.multiplesize(1.5, X)
SHIP_FIVE.set_defaultpos(pixelinhd(304, X), pixelinhd(691, X))
SHIP_FOUR = Pygameimage("4x1", "assets/4x1.png")
SHIP_FOUR.multiplesize(1.5, X)
SHIP_FOUR.set_defaultpos(pixelinhd(304, X), pixelinhd(607, X))
SHIP_THIRD_FIRST = Pygameimage("3x1_1", "assets/3x1.png")
SHIP_THIRD_FIRST.multiplesize(1.5, X)
SHIP_THIRD_FIRST.set_defaultpos(pixelinhd(304, X), pixelinhd(523, X))
SHIP_THIRD_SECOND = Pygameimage("3x1_2", "assets/3x1.png")
SHIP_THIRD_SECOND.multiplesize(1.5, X)
SHIP_THIRD_SECOND.set_defaultpos(pixelinhd(304, X), pixelinhd(439, X))
SHIP_TWO = Pygameimage("2x1", "assets/2x1.png")
SHIP_TWO.multiplesize(1.5, X)
SHIP_TWO.set_defaultpos(pixelinhd(304, X), pixelinhd(355, X))
SHIPS_LIST = {
    "5x1": SHIP_FIVE,
    "4x1": SHIP_FOUR,
    "3x1_1": SHIP_THIRD_FIRST,
    "3x1_2": SHIP_THIRD_SECOND,
    "2x1": SHIP_TWO
}

P1_LIST = [
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
P2_LIST = [
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

EMPTY_CASE = []
# By player 2
COORD_EMPTY_CASE_P1 = []
COORD_TOUCHED_CASE_P1 = []
TOUCHED_CASE = []
COORD_EMPTY_CASE_P2 = []
COORD_TOUCHED_CASE_P2 = []

LIST_SHIP = [SHIP_FIVE, SHIP_FOUR, SHIP_THIRD_FIRST, SHIP_THIRD_SECOND, SHIP_TWO]
SHIP_COORD_P1 = {}
SHIP_COORD_P2 = {}
"""
0: No shot made
1: Shot here but no ship
2: Shot here and ship
"""

RUNNING = True
pass_stats = False
stats = 0
txt = ""
"""
Diffrents stats:
MENU: 0
PLACE_SHIPS: 1
PLAYER_1_PLAY: 2
PLAYER_1_RESULT: 3
PLAYER_2_PLAY: 4
PLAYER_2_RESULT: 5
END: 6
CLOSING GAME: 7
"""

while RUNNING:

    SCREEN.blit(FOND, (0, 0))

    if DEBUG:
        # For debug
        FONT2 = pygame.font.Font('assets/Montserrat-Black.ttf', 25)
        showtext(SCREEN, f"Stats: {stats}", FONT2, pixelinhd(85, X), pixelinhd(20, X), (0, 0, 0))
        showtext(SCREEN, "P1_LIST:", FONT2, pixelinhd(87, X), pixelinhd(42, X), (0, 0, 0))
        y = pixelinhd(64, X)
        for i in P1_LIST:
            showtext(SCREEN, str(i), FONT2, pixelinhd(200, X), y, (0, 0, 0))
            y = y+pixelinhd(22, X)

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
        SCREEN.blit(SHIP_THIRD_FIRST.image, SHIP_THIRD_FIRST.position)
        SCREEN.blit(SHIP_THIRD_SECOND.image, SHIP_THIRD_SECOND.position)
        SCREEN.blit(SHIP_TWO.image, SHIP_TWO.position)
        SCREEN.blit(CLEAR_BUTTON.image, CLEAR_BUTTON.position)
        SCREEN.blit(RANDOM_BUTTON.image, RANDOM_BUTTON.position)
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
    elif stats == 3:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, txt, FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        for i in EMPTY_CASE:
            SCREEN.blit(i.image, i.position)
        for i in TOUCHED_CASE:
            SCREEN.blit(i.image, i.position)
    elif stats == 4:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, "Au tour de l'ia de jouer.", FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        for i in EMPTY_CASE:
            SCREEN.blit(i.image, i.position)
        for i in TOUCHED_CASE:
            SCREEN.blit(i.image, i.position)
        response = aishoot(COORD_TOUCHED_CASE_P1+COORD_EMPTY_CASE_P1)
        nb_x = response[0]
        nb_y = response[1]

        x1 = GRID_P1.position[0]+(nb_x-1)*multiplypixelinhd(1.5, 50, X)
        x = GRID_P1.position[0]+(nb_x-1)*multiplypixelinhd(1.5, 50, X)
        y1 = GRID_P1.position[1]+(nb_y-1)*multiplypixelinhd(1.5, 50, X)
        y = GRID_P1.position[1]+(nb_y-1)*multiplypixelinhd(1.5, 50, X)

        case_exist = False
        if nb_x > 0 and nb_y > 0:
            for i in SHIP_COORD_P1.values():
                for ii in i:
                    if ii == (nb_x, nb_y):
                        case_exist = True
            if ((nb_x, nb_y) in COORD_TOUCHED_CASE_P1) == False and ((nb_x, nb_y) in COORD_EMPTY_CASE_P1) == False and case_exist:
                txt = "touché"
                TOUCHED_CASE.append(Pygameimage("Something case", "assets/something_touched.png"))
                TOUCHED_CASE[-1].multiplesize(1.5, X)
                TOUCHED_CASE[-1].set_defaultpos(x1, y1)
                COORD_TOUCHED_CASE_P1.append((nb_x, nb_y))
            elif ((nb_x, nb_y) in COORD_TOUCHED_CASE_P1) == False and ((nb_x, nb_y) in COORD_EMPTY_CASE_P1) == False:
                txt = "loupé"
                EMPTY_CASE.append(Pygameimage("Empty case", "assets/nothing_touched.png"))
                EMPTY_CASE[-1].multiplesize(1.5, X)
                EMPTY_CASE[-1].set_defaultpos(x1, y1)
                COORD_EMPTY_CASE_P1.append((nb_x, nb_y))
            length = 0
            for i in SHIP_COORD_P1:
                length = length + int(i[0])
            if length == len(COORD_TOUCHED_CASE_P1):
                winner = "l'ia"
                stats = 6
        stats = 5
    elif stats == 5:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, f"L'ia a {txt} son tire.", FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        for i in EMPTY_CASE:
            SCREEN.blit(i.image, i.position)
        for i in TOUCHED_CASE:
            SCREEN.blit(i.image, i.position)
    elif stats == 6:
        showtext(SCREEN, f"Le gagnant de match est {winner} !", FONT, X//2, Y//2, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if stats == 3:
                    length = 0
                    for i in SHIP_COORD_P2:
                        length = length + int(i[0])
                    if length == len(COORD_TOUCHED_CASE_P2):
                        winner = "le joueur 1"
                        stats = 6
                    else:
                        stats = 4
                elif stats == 5:
                    stats = 2
                elif stats == 6:
                    RUNNING = False
            elif event.key == pygame.K_F4:
                DEBUG = not(DEBUG)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if colide(PLAY_BUTTON, event.pos) and stats == 0:
                    stats = 1
                elif stats == 1:
                    for i in LIST_SHIP:
                        if colide(i, event.pos) and stats == 1 and isclickable(LIST_SHIP):
                            # Ship is clicked to be placed next
                            x = i.position[0] - pixelinhd(5, X)
                            y = i.position[1] + pixelinhd(30, X)
                            if i.position != i.default_pos:
                                nb_x = 1
                                while x > MAIN_GRID.position[0] - pixelinhd(5, X):
                                    x = x - multiplypixelinhd(1.5, 50, X)
                                    nb_x = nb_x + 1
                                y = i.position[1] + pixelinhd(30, X)
                                nb_y = 1
                                while y > MAIN_GRID.position[1] + pixelinhd(30, X):
                                    y = y - multiplypixelinhd(1.5, 50, X)
                                    nb_y = nb_y + 1
                                TEMP_COORD = []
                                for ii in range(int(i.name[0])):
                                    TEMP_COORD.append((nb_x, nb_y))
                                    nb_x = nb_x + 1
                                print(TEMP_COORD)
                                for y in TEMP_COORD:
                                    P1_LIST[y[1]-1][y[0]-1] = 0
                            i.clicked = True
                        elif i.clicked and colide(MAIN_GRID, (event.pos[0]+pixelinhd(37, X), event.pos[1]+pixelinhd(37, X))) and i.position[0]+i.size[0] < MAIN_GRID.position[0]+MAIN_GRID.size[0] and i.position[1]+i.size[1] < MAIN_GRID.position[1]+MAIN_GRID.size[1]:
                            # Ship is placed
                            i.clicked = False
                            i.set_pos(roundat(i.position[0], multiplypixelinhd(1.5, 50, X))+pixelinhd(5, X), roundat(i.position[1], multiplypixelinhd(1.5, 50, X))-pixelinhd(30, X))
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
                            if not placable(SHIP_COORD_P1[i.name], P1_LIST):
                                del SHIP_COORD_P1[i.name]
                                i.clicked = True
                            else:
                                for iii in SHIP_COORD_P1[i.name]:
                                    P1_LIST[iii[1]-1][iii[0]-1] = 1
                        elif colide(i, event.pos):
                            i.clicked = False
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            if i.name in SHIP_COORD_P1.keys():
                                del SHIP_COORD_P1[i.name]
                    if colide(CLEAR_BUTTON, event.pos):
                        # Reset all boats
                        P1_LIST = [
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
                        for i in LIST_SHIP:
                            i.clicked = False
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            if i.name in SHIP_COORD_P1.keys():
                                del SHIP_COORD_P1[i.name]
                    elif colide(RANDOM_BUTTON, event.pos):
                        # Randomise boat position
                        P1_LIST = [
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
                        for i in LIST_SHIP:
                            i.clicked = False
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            if i.name in SHIP_COORD_P1.keys():
                                del SHIP_COORD_P1[i.name]
                        random_coords = generatecoord(P1_LIST)
                        for i in random_coords:
                            SHIP_COORD_P1[i] = []
                            for y in range(int(i[0])):
                                SHIP_COORD_P1[i].append(random_coords[i][y])
                            SHIPS_LIST[i].set_pos(MAIN_GRID.position[0] + (random_coords[i][0][0]-1)*pixelinhd(75, X), MAIN_GRID.position[1] + (random_coords[i][0][1]-1)*pixelinhd(75, X))
                    elif colide(START_BUTTON, event.pos):
                        SHIP_COORD_P2 = generatecoord(P2_LIST)
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
                            if not((nb_x, nb_y) in COORD_EMPTY_CASE_P2+COORD_TOUCHED_CASE_P2) and case_exist:
                                TOUCHED_CASE.append(Pygameimage("Something case", "assets/something_touched.png"))
                                TOUCHED_CASE[-1].multiplesize(1.5, X)
                                TOUCHED_CASE[-1].set_defaultpos(x1, y1)
                                COORD_TOUCHED_CASE_P2.append((nb_x, nb_y))
                                txt = "Touché !"
                                pass_stats = True
                            elif not((nb_x, nb_y) in COORD_EMPTY_CASE_P2+COORD_TOUCHED_CASE_P2):
                                EMPTY_CASE.append(Pygameimage("Empty case", "assets/nothing_touched.png"))
                                EMPTY_CASE[-1].multiplesize(1.5, X)
                                EMPTY_CASE[-1].set_defaultpos(x1, y1)
                                COORD_EMPTY_CASE_P2.append((nb_x, nb_y))
                                txt = "Loupé !"
                                pass_stats = True
                    if pass_stats:
                        pass_stats = False
                        stats = 3

    pygame.display.flip()

pygame.quit()