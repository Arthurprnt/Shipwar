from func import *
from imports import *
pygame.init()

DEBUG = False

RUNNING = True
pass_stats = False
stats = 0
difficulty = 0
txt = ""
clickedship = ""

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

    if DEBUG:
        # For debug
        FONT2 = pygame.font.Font('assets/Montserrat-Black.ttf', 25)
        showtext(SCREEN, f"Stats: {stats}", FONT2, pixelinhd(85, X), pixelinhd(20, X), (0, 0, 0))
        showtext(SCREEN, f"Mouse pos: {str(pygame.mouse.get_pos())}", FONT2, pixelinhd(180, X), pixelinhd(42, X), (0, 0, 0))
        if clickedship != "":
            showtext(SCREEN, f"Axe clickedship: {SHIPS_LIST[clickedship].axe}", FONT2, pixelinhd(160, X), pixelinhd(64, X), (0, 0, 0))
            y = 86
        else:
            y = 64
        showtext(SCREEN, "P1_LIST:", FONT2, pixelinhd(87, X), pixelinhd(y, X), (0, 0, 0))
        y = pixelinhd(y+22, X)
        for i in P1_LIST:
            showtext(SCREEN, str(i), FONT2, pixelinhd(200, X), y, (0, 0, 0))
            y = y+pixelinhd(22, X)

    # Display every sprite needed per stats of the game
    if stats == 0:
        SCREEN.blit(LOGO_MENU.image, LOGO_MENU.position)
        SCREEN.blit(PLAY_BUTTON.image, PLAY_BUTTON.position)
        SCREEN.blit(DIFFICULTY_LIST[difficulty].image, DIFFICULTY_LIST[difficulty].position)
    elif stats == 1:
        for i in LIST_SHIP:
            if i.clicked:
                try:
                    i.set_pos(event.pos[0]-pixelinhd(37, X), event.pos[1]-pixelinhd(37, X))
                except:
                    pass
        SCREEN.blit(MAIN_GRID.image, MAIN_GRID.position)
        CANT_PLACE_DICT = {}
        for i in SHIP_COORD_P1:
            for y in SHIP_COORD_P1[i]:
                for xx in range(-1, 2):
                    for yy in range(-1, 2):
                        if 10 >= y[0] + xx >= 1 and 10 >= y[1] + yy >= 1:
                            if not (i in CANT_PLACE_DICT.keys()):
                                CANT_PLACE_DICT[f"{y[0] + xx - 1}{y[1] + yy - 1}"] = (y[0] + xx - 1, y[1] + yy - 1)
        for i in CANT_PLACE_DICT:
            CANT_PLACE.set_pos(MAIN_GRID.position[0] + pixelinhd(75, X) * CANT_PLACE_DICT[i][0], MAIN_GRID.position[1] + pixelinhd(75, X) * CANT_PLACE_DICT[i][1])
            SCREEN.blit(CANT_PLACE.image, CANT_PLACE.position)
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
        updatecases(EMPTY_CASE, TOUCHED_CASE, SCREEN)
    elif stats == 3:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, txt, FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        updatecases(EMPTY_CASE, TOUCHED_CASE, SCREEN)
    elif stats == 4:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, "Au tour de l'ia de jouer.", FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        updatecases(EMPTY_CASE, TOUCHED_CASE, SCREEN)
        response = aishoot(IA_SHOOTS, COORD_TOUCHED_CASE_P1, SHIP_COORD_P1, difficulty)
        IA_SHOOTS.append(response)
        nb_x = response[0]
        nb_y = response[1]

        x1 = GRID_P1.position[0]+(nb_x-1)*multiplypixelinhd(1.504, 50, X)
        x = GRID_P1.position[0]+(nb_x-1)*multiplypixelinhd(1.504, 50, X)
        y1 = GRID_P1.position[1]+(nb_y-1)*multiplypixelinhd(1.504, 50, X)
        y = GRID_P1.position[1]+(nb_y-1)*multiplypixelinhd(1.504, 50, X)

        case_exist = False
        if nb_x > 0 and nb_y > 0:
            for i in SHIP_COORD_P1.values():
                for ii in i:
                    if ii == (nb_x, nb_y):
                        case_exist = True
            if case_exist:
                txt = checkshipstats(SHIP_COORD_P1, (nb_x, nb_y))
                addcase(TOUCHED_CASE, COORD_TOUCHED_CASE_P1, Pygameimage("Something case", "assets/something_touched.png"), x1, y1, nb_x, nb_y)
            else:
                txt = "loup??"
                addcase(EMPTY_CASE, COORD_EMPTY_CASE_P1, Pygameimage("Empty case", "assets/nothing_touched.png"), x1, y1, nb_x, nb_y)
            if 2+2*3+4+5 == len(COORD_TOUCHED_CASE_P1):
                winner = "l'ia"
                stats = 6
            else:
                stats = 5
    elif stats == 5:
        SCREEN.blit(GRID_P1.image, GRID_P1.position)
        SCREEN.blit(GRID_P2.image, GRID_P2.position)
        SCREEN.blit(PLAYER1_LOGO.image, PLAYER1_LOGO.position)
        SCREEN.blit(PLAYER2_LOGO.image, PLAYER2_LOGO.position)
        showtext(SCREEN, f"L'ia a {txt} un bateau.", FONT, X//2, pixelinhd(170, X), (0, 0, 0))
        updatecases(EMPTY_CASE, TOUCHED_CASE, SCREEN)
    elif stats == 6:
        showtext(SCREEN, f"Le gagnant de match est {winner} !", FONT, X//2, Y//2-pixelinhd(Y/28, X), (0, 0, 0))
        SCREEN.blit(REPLAY_BUTTON.image, REPLAY_BUTTON.position)

    # Check the event made by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if stats == 3:
                    if 2+2*3+4+5 == len(COORD_TOUCHED_CASE_P2):
                        winner = "le joueur 1"
                        stats = 6
                    else:
                        stats = 4
                elif stats == 5:
                    stats = 2
            elif event.key == pygame.K_F4:
                DEBUG = not(DEBUG)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if stats == 0:
                    # Change the difficulty
                    if colide(BUTTON_FACILE, event.pos):
                        difficulty = difficulty + 1
                        if difficulty == 3:
                            difficulty = 0
                    elif colide(PLAY_BUTTON, event.pos):
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
                                if i.axe == "x":
                                    for ii in range(int(i.name[0])):
                                        TEMP_COORD.append((nb_x, nb_y))
                                        nb_x = nb_x + 1
                                else:
                                    for ii in range(int(i.name[0])):
                                        TEMP_COORD.append((nb_x, nb_y))
                                        nb_y = nb_y + 1
                                for y in TEMP_COORD:
                                    P1_LIST[y[1]-1][y[0]-1] = 0
                            i.clicked = True
                            clickedship = i.name
                        elif i.clicked and colide(MAIN_GRID, event.pos) and i.position[0]+i.getimagesize()[0] <= MAIN_GRID.position[0]+MAIN_GRID.getimagesize()[0] and i.position[1]+i.getimagesize()[1] <= MAIN_GRID.position[1]+MAIN_GRID.getimagesize()[1]:
                            # Ship is placed
                            i.clicked = False
                            clickedship = ""
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
                            if i.axe == "x":
                                for ii in range(int(i.name[0])):
                                    SHIP_COORD_P1[i.name].append((nb_x, nb_y))
                                    nb_x = nb_x + 1
                            else:
                                for ii in range(int(i.name[0])):
                                    SHIP_COORD_P1[i.name].append((nb_x, nb_y))
                                    nb_y = nb_y + 1
                            if not(placable(SHIP_COORD_P1[i.name], P1_LIST)) or i.position[1] == 270:
                                # But the ship is not placable
                                del SHIP_COORD_P1[i.name]
                                i.clicked = True
                            else:
                                for iii in SHIP_COORD_P1[i.name]:
                                    P1_LIST[iii[1]-1][iii[0]-1] = 1
                        elif colide(i, event.pos):
                            # Reset the position of the ship
                            i.clicked = False
                            clickedship = ""
                            if i.axe == "y":
                                i.image = pygame.transform.rotate(i.image, 90)
                            i.axe = "x"
                            i.set_pos(i.default_pos[0], i.default_pos[1])
                            if i.name in SHIP_COORD_P1.keys():
                                del SHIP_COORD_P1[i.name]
                    if colide(CLEAR_BUTTON, event.pos):
                        # Reset all boats
                        P1_LIST, clickedship = cleargride(P1_LIST, LIST_SHIP, SHIP_COORD_P1)
                    elif colide(RANDOM_BUTTON, event.pos):
                        # Randomise boat position
                        P1_LIST, clickedship = cleargride(P1_LIST, LIST_SHIP, SHIP_COORD_P1)
                        returnedcoords = generatecoord(P1_LIST)
                        random_coords = returnedcoords[0]
                        for i in returnedcoords[1]:
                            if SHIPS_LIST[i].axe != returnedcoords[1][i]:
                                SHIPS_LIST[i].image = pygame.transform.rotate(SHIPS_LIST[i].image, 90)
                                if SHIPS_LIST[i].axe == "x":
                                    SHIPS_LIST[i].axe = "y"
                                else:
                                    SHIPS_LIST[i].axe = "x"
                        for i in random_coords:
                            SHIP_COORD_P1[i] = []
                            for y in range(int(i[0])):
                                SHIP_COORD_P1[i].append(random_coords[i][y])
                            SHIPS_LIST[i].set_pos(MAIN_GRID.position[0] + (random_coords[i][0][0]-1)*pixelinhd(75, X), MAIN_GRID.position[1] + (random_coords[i][0][1]-1)*pixelinhd(75, X))
                    elif colide(START_BUTTON, event.pos):
                        if len(SHIP_COORD_P1) == len(LIST_SHIP):
                            SHIP_COORD_P2 = generatecoord(P2_LIST)[0]
                            stats = 2
                elif stats == 2:
                    if colide(GRID_P2, event.pos):
                        x = roundat(event.pos[0], multiplypixelinhd(1.5, 50, X))
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
                        x1 = GRID_P2.position[0] + (nb_x - 1) * multiplypixelinhd(1.504, 50, X)
                        y1 = GRID_P2.position[1] + (nb_y - 1) * multiplypixelinhd(1.504, 50, X)
                        if nb_x > 0 and nb_y > 0:
                            for i in SHIP_COORD_P2.values():
                                for ii in i:
                                    if ii == (nb_x, nb_y):
                                        case_exist = True
                            if not((nb_x, nb_y) in COORD_EMPTY_CASE_P2+COORD_TOUCHED_CASE_P2) and case_exist:
                                addcase(TOUCHED_CASE, COORD_TOUCHED_CASE_P2, Pygameimage("Something case", "assets/something_touched.png"), x1, y1, nb_x, nb_y)
                                txt = checkshipstats(SHIP_COORD_P2, (nb_x, nb_y))
                                txt = txt[0].upper() + txt[1:] + " !"
                                pass_stats = True
                            elif not((nb_x, nb_y) in COORD_EMPTY_CASE_P2+COORD_TOUCHED_CASE_P2):
                                addcase(EMPTY_CASE, COORD_EMPTY_CASE_P2, Pygameimage("Empty case", "assets/nothing_touched.png"), x1, y1, nb_x, nb_y)
                                txt = "Loup?? !"
                                pass_stats = True
                    if pass_stats:
                        pass_stats = False
                        stats = 3
                elif stats == 6:
                    if colide(REPLAY_BUTTON, event.pos):
                        difficulty = 0
                        stats = 0
                        P1_LIST, clickedship = cleargride(P1_LIST, LIST_SHIP, SHIP_COORD_P1)
                        P2_LIST, clickedship = cleargride(P2_LIST, LIST_SHIP, SHIP_COORD_P2)
                        IA_SHOOTS = []
                        EMPTY_CASE = []
                        COORD_EMPTY_CASE_P1 = []
                        COORD_TOUCHED_CASE_P1 = []
                        TOUCHED_CASE = []
                        COORD_EMPTY_CASE_P2 = []
                        COORD_TOUCHED_CASE_P2 = []
                        SHIP_COORD_P1 = {}
                        SHIP_COORD_P2 = {}
            # Wheel button to rotate the clicked ship
            elif event.button == 2:
                if stats == 1:
                    if clickedship != "":
                        if SHIPS_LIST[clickedship].axe == "x":
                            SHIPS_LIST[clickedship].axe = "y"
                        else:
                            SHIPS_LIST[clickedship].axe = "x"
                        SHIPS_LIST[clickedship].image = pygame.transform.rotate(SHIPS_LIST[clickedship].image, 90)

    pygame.display.flip()

pygame.quit()