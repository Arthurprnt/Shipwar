import random

def generatecoord():
    SHIP_COORD = {}
    list_y = []
    x = random.randint(1, 5)
    y = random.randint(1, 10)
    SHIP_COORD["5x1"] = []
    for i in range(5):
        SHIP_COORD["5x1"].append((x, y))
        x = x + 1
    list_y.append(y)
    x = random.randint(1, 6)
    while y in list_y:
        y = random.randint(1, 10)
    SHIP_COORD["4x1"] = []
    for i in range(4):
        SHIP_COORD["4x1"].append((x, y))
        x = x + 1
    return SHIP_COORD

def aishoot(shotsmade):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    while (x, y) in shotsmade:
        x, y = aishoot(shotsmade)
    return (x, y)