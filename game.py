import pygame

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello pygame')

screen = pygame.Surface((400, 400))


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((8, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1,x2,y1,y2):
    if(x1 > x2-40) and (x1 < x2+40) and (y1 > y2-40) and (y1 < y2+40):
        return True
    else:
        return False



hero = Sprite(200, 350, 'img/rocket.png')
hero.up = True
zet = Sprite(200, 10, 'img/goal.png')
zet.up = True

done = True

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50, 50, 50))

    if hero.up == True:
        hero.y -= 1
        if hero.y == 0:
            hero.up = False
    else:
        hero.y += 1
        if hero.y == 350:
            hero.up = True

    if zet.up == True:
        zet.y -= 1
        if zet.y == 0:
            zet.up = False
    else:
        zet.y += 1
        if zet.y == 350:
            zet.up = True

    if Intersect(zet.x, zet.y, hero.x, hero.y):
        hero.up = False
        zet.up = True

    hero.render()
    zet.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()

    pygame.time.delay(5)