import pygame as pg
import menu_batalha as mb


def Captura(play2, bag, i, j, texto, screen, background, info):
    sucess = (3 * play2.stats.max) - (2 * play2.stats.hp)
    sucess = sucess * 45 * bag[i].Pokeball[j].rate
    sucess = sucess / (3 * play2.stats.max)
    sucess = sucess / 100
    bag[i].Pokeball[j].qtd -= 1
    if sucess >= 0.4:
        play2.pokeball = bag[i].Pokeball[j].ball
        return True
    elif bag[i].Pokeball[j].ball == 'Masterball':
        play2.pokeball = bag[i].Pokeball[j].ball
        return True
    else:
        return False

def Pokeball(play2, bag, info, mochila, screen, seta, texto, background):
    turno = 0
    seta_x = 400
    seta_y = 50
    in_pokeball = True
    pokeball = pg.image.load("Sprites\\SpritesInterface\\Pokeball.png")
    greatball = pg.image.load("Sprites\\SpritesInterface\\Greatball.png")
    ultraball = pg.image.load("Sprites\\SpritesInterface\\Ultraball.png")
    masterball = pg.image.load("Sprites\\SpritesInterface\\Masterball.png")
    pokeball = pg.transform.scale(pokeball, (100, 100))
    greatball = pg.transform.scale(greatball, (100, 100))
    ultraball = pg.transform.scale(ultraball, (100, 100))
    masterball = pg.transform.scale(masterball, (100, 100))
    clock = pg.time.Clock()
    while in_pokeball:
        x = 0
        y = 0
        clock.tick(10)
        screen.blit(mochila, (0, 0))
        for i in range(4):
            a = bag[0].Pokeball[i].ball
            b = "X  " + str(bag[0].Pokeball[i].qtd)
            ball = info.render(a, 1, (0, 0, 0))
            qtd = info.render(b, 1, (0, 0, 0))
            screen.blit(ball, (450, 50 + y))
            screen.blit(qtd, (800, 50 + y))

            y += 60

        seta = pg.transform.scale(seta, (50, 50))
        titulo = info.render("Pokeballs", 1, (0, 0, 0))
        screen.blit(titulo, (100, 30))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if seta_y + 60 <= 230:
                        seta_y += 60
                elif event.key == pg.K_UP:
                    if seta_y - 60 >= 50:
                        seta_y -= 60
                elif event.key == pg.K_z:
                    if seta_y == 50:
                        if Captura(play2, bag, 0, 0, texto, screen, background, info):
                            play2.capturado = 1
                            turno += 1
                            in_pokeball = False
                        else:
                            turno += 1
                            in_pokeball = False
                    elif seta_y == 110:
                        if Captura(play2, bag, 0, 1, texto, screen, background, info):
                            play2.capturado = 1
                            turno += 1
                            in_pokeball = False
                        else:
                            turno += 1
                            in_pokeball = False
                    elif seta_y == 170:
                        if Captura(play2, bag, 0, 2, texto, screen, background, info):
                            play2.capturado = 1
                            turno += 1
                            in_pokeball = False
                        else:
                            turno += 1
                            in_pokeball = False
                    elif seta_y == 230:
                        if Captura(play2, bag, 0, 3, texto, screen, background, info):
                            play2.capturado = 1
                            turno += 1
                            in_pokeball = False
                        else:
                            turno += 1
                            in_pokeball = False
                elif event.key == pg.K_LEFT:
                    in_pokeball = False

                elif event.key == pg.K_x:
                    in_pokeball = False

        screen.blit(seta, (seta_x, seta_y))

        if seta_y == 50:
            screen.blit(pokeball, (30, 440))
        elif seta_y == 110:
            screen.blit(greatball, (30, 440))
        elif seta_y == 170:
            screen.blit(ultraball, (30, 440))
        elif seta_y == 230:
            screen.blit(masterball, (30, 440))

        pg.display.update()

    return turno