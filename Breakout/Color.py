import random

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grey = (157, 157, 157)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



