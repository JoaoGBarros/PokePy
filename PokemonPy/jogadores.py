import pygame as pg

def PrintJog(img, screen):
    screen.blit(img, (0, 0))

def menu_escolha():
    pg.init()
    screen = pg.display.set_mode((605, 800))
    pg.display.set_caption("Jogadores")
    icon = pg.image.load('Sprites\\SpritesInterface\\gaming.png')
    pg.display.set_icon(icon)
    img = pg.image.load("Sprites\\jog.png")
    img = pg.transform.scale(img, (605, 800))


    menu = True


    while menu:
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(pos)
                if 150 <= pos[0] <= 310:
                    if 510 <= pos[1] <= 540:
                        num = 1
                        menu = False
                    elif 580 <= pos[1] <= 700:
                        num = 2
                        menu = False

        PrintJog(img, screen)

        pg.display.flip()
        pg.display.update()

    return num