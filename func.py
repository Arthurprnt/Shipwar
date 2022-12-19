import random

def generatecoord():
    SHIP_COORD = {}
    x = random.randint(1, 5)
    y = random.randint(1, 10)
    SHIP_COORD["5x1"] = []
    for i in range(5):
        SHIP_COORD["5x1"].append((x, y))
        x = x + 1
    x = random.randint(1, 6)
    y = random.randint(1, 10)
    SHIP_COORD["4x1"] = []
    for i in range(4):
        SHIP_COORD["4x1"].append((x, y))
        x = x + 1
    return SHIP_COORD