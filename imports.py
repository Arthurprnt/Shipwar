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
FONT = pygame.font.Font('assets/Montserrat-Black.ttf', 55)
LOGO_MENU = Pygameimage("Logo menu", "assets/menu_name.png")
LOGO_MENU.multiplesize(0.6, X)
LOGO_MENU.center((X, Y), "x")
LOGO_MENU.add_y(Y/10)
PLAY_BUTTON = Pygameimage("Play button", "assets/play_button.png")
PLAY_BUTTON.multiplesize(0.5, X)
PLAY_BUTTON.center((X, Y), "all")
PLAY_BUTTON.add_y(Y/12)
PLAY_BUTTON.add_x(pixelinhd(60, X))
CLEAR_BUTTON = Pygameimage("Clear button", "assets/trash_button.png")
CLEAR_BUTTON.multiplesize(0.4, X)
CLEAR_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(340, X))
RANDOM_BUTTON = Pygameimage("Random button", "assets/randomise_button.png")
RANDOM_BUTTON.multiplesize(0.4, X)
RANDOM_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(540, X))
START_BUTTON = Pygameimage("Start button", "assets/play_button.png")
START_BUTTON.multiplesize(0.4, X)
START_BUTTON.set_pos(pixelinhd(1670, X), pixelinhd(740, X))
REPLAY_BUTTON = Pygameimage("Replay button", "assets/rejouer.png")
REPLAY_BUTTON.multiplesize(0.3, X)
REPLAY_BUTTON.center((X, Y), "x")
REPLAY_BUTTON.set_pos(REPLAY_BUTTON.position[0], Y/2+pixelinhd(Y/28, X))
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
CANT_PLACE = Pygameimage("Cant place", "assets/cant_place.png")
CANT_PLACE.multiplesize(1.5, X)
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
BUTTON_FACILE = Pygameimage("Facile", "assets/facile.png")
BUTTON_FACILE.multiplesize(0.5, X)
BUTTON_FACILE.center((X, Y), "all")
BUTTON_FACILE.add_y(Y/12)
BUTTON_FACILE.add_x(X/7.5)
BUTTON_MOYEN = Pygameimage("Moyen", "assets/moyen.png")
BUTTON_MOYEN.multiplesize(0.5, X)
BUTTON_MOYEN.center((X, Y), "all")
BUTTON_MOYEN.add_y(Y/12)
BUTTON_MOYEN.add_x(X/7.5)
BUTTON_DIFFICILE = Pygameimage("Difficile", "assets/difficile.png")
BUTTON_DIFFICILE.multiplesize(0.5, X)
BUTTON_DIFFICILE.center((X, Y), "all")
BUTTON_DIFFICILE.add_y(Y/12)
BUTTON_DIFFICILE.add_x(X/7.5)
DIFFICULTY_LIST = [BUTTON_FACILE, BUTTON_MOYEN, BUTTON_DIFFICILE]

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

IA_SHOOTS = []
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