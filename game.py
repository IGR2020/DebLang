import pygame as pg
from debLang import Debuger, createEnvironment

createEnvironment("game.py")

deb = Debuger(("game.py",))
deb.start()

pg.font.init()

window_width, window_height = 900, 500
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Multiplayer Test")

run = True
fps = 60
clock = pg.time.Clock()


def blit_text(window, text, pos, colour=(0, 0, 0), size=30):
    text = str(text)
    x, y = pos
    font_style = pg.font.SysFont("arialblack", size)
    text_surface = font_style.render(text, True, colour)
    window.blit(text_surface, (x-text_surface.get_width()/2, y-text_surface.get_height()/2))


class Player:
    def __init__(self, x, y, width, height, name, color) -> None:
        self.rect = pg.Rect(x, y, width, height)
        self.name = name
        self.color = color

    def display(self, window):
        pg.draw.rect(window, self.color, self.rect)
        blit_text(window, self.name, (self.rect.centerx, self.rect.y - 20), (0, 0, 0), 30)


players = {"": Player(100, 100, 50, 100, "IGR2020", (255, 0, 0))}
name = ""

while run:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        players[name].rect.x -= 3
    if keys[pg.K_d]:
        players[name].rect.x += 3
    if keys[pg.K_w]:
        players[name].rect.y -= 3
    if keys[pg.K_s]:
        players[name].rect.y += 3

    window.fill((255, 255, 255))
    for player in players:
        players[player].display(window)
    pg.display.update()
pg.quit()
quit()