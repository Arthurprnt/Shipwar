import pygame

class Pygameimage():

    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.size = self.image.get_size()
        self.position = [0, 0]
        self.default_pos = [0, 0]
        self.area = [[self.position[0], self.position[0]+self.size[0]], [self.position[1], self.position[1]+self.size[1]]]
        self.clicked = False

    def multiplesize(self, ratio, screen_size):
        assert type(ratio) == float or type(ratio) == int
        assert type(screen_size) == int
        self.size = (round(self.size[0]*ratio*screen_size/2560), round(self.size[1]*ratio*screen_size/2560))
        self.image = pygame.transform.scale(self.image, self.size)
        self.area = [[self.position[0], self.position[0]+self.size[0]], [self.position[1], self.position[1]+self.size[1]]]

    def center(self, screen_sizes, x_or_y):
        assert type(x_or_y) == str
        if x_or_y.lower() == "all":
            self.position = [screen_sizes[0]/2-self.size[0]/2, screen_sizes[1]/2-self.size[1]/2]
            self.default_pos = [screen_sizes[0]/2-self.size[0]/2, screen_sizes[1]/2-self.size[1]/2]
            self.area = [[self.position[0], self.position[0]+self.size[0]], [self.position[1], self.position[1]+self.size[1]]]
        elif x_or_y.lower() == "x":
            self.position[0] = screen_sizes[0]/2-self.size[0]/2
            self.default_pos[0] = screen_sizes[0]/2-self.size[0]/2
            self.area = [[self.position[0], self.position[0]+self.size[0]], [self.position[1], self.position[1]+self.size[1]]]
        elif x_or_y.lower() == "y":
            self.position[1] = screen_sizes[1]/2-self.size[1]/2
            self.default_pos[1] = screen_sizes[1]/2-self.size[1]/2
            self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def add_y(self, new_y):
        new_y = round(new_y)
        self.position[1] = self.position[1]+new_y
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def add_x(self, new_x):
        new_x = round(new_x)
        self.position[0] = self.position[1]+new_x
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def set_y(self, new_y):
        self.position[1] = round(new_y)
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def set_x(self, new_x):
        self.position[0] = round(new_x)
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def set_pos(self, new_x, new_y):
        self.position = [round(new_x), round(new_y)]
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

    def set_defaultpos(self, new_x, new_y):
        self.position = [round(new_x), round(new_y)]
        self.default_pos = [round(new_x), round(new_y)]
        self.area = [[self.position[0], self.position[0] + self.size[0]], [self.position[1], self.position[1] + self.size[1]]]

def colide(image, mouse):
    return (mouse[0] <= image.area[0][1]) and (mouse[0] >= image.area[0][0]) and (mouse[1] <= image.area[1][1]) and (mouse[1] >= image.area[1][0])

def pixelinhd(length, screen):
    return length*screen/2560

def isclickable(liste):
    for i in liste:
        if i.clicked:
            return False
    return True

def findclicked(liste):
    for i in range(len(liste)):
        if liste[i].clicked:
            return i
    return False

def roundat(x, at):
    return at*round(x/at)