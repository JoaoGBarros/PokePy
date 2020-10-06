import pygame as pg


def Clicou(pos):
    if 0 <= pos[0] <= 200:
        if 0 <= pos[1] <= 200:
            return "Sceptile"
        elif 200 < pos[1] <= 400:
            return "Milotic"
        elif 400 < pos[1] <= 600:
            return "Jolteon"
        elif 600 < pos[1] <= 800:
            return "Walrein"
    elif 200 < pos[0] <= 400:
        if 0 <= pos[1] <= 200:
            return "Flygon"
        elif 200 < pos[1] <= 400:
            return "Ninetales"
        elif 400 < pos[1] <= 600:
            return "Scizor"
        elif 600 < pos[1] <= 800:
            return "Cradily"
    elif 400 < pos[0] <= 600:
        if 0 <= pos[1] <= 200:
            return "Gengar"
        elif 200 < pos[1] <= 400:
            return "Gardevoir"
        elif 400 < pos[1] <= 600:
            return "Noctowl"
        elif 600 < pos[1] <= 800:
            return "Crobat"


def PrintFundo(quadrados, screen, cores):

    for i in range(12):
        pg.draw.rect(screen, cores[i], quadrados[i])


def PrintSplashs(splashs, screen):
    x = 0
    for i in range(len(splashs)):
        if i < 3:
            screen.blit(splashs[i], (3+x, 0))
            x += 200

        if i == 3:
            x = 0

        if 3 <= i < 6:
            screen.blit(splashs[i], (3+x, 200))
            x += 200

        if i == 6:
            x = 0

        if 6 <= i < 9:
            screen.blit(splashs[i], (3+x, 400))
            x += 200

        if i == 9:
            x = 0

        if 9 <= i < 12:
            screen.blit(splashs[i], (3+x, 600))
            x += 200


def DefineSplash(pokemons):
    sp = []
    for pk in pokemons:
        string = pk + ".png"
        imagem = pg.image.load(string)
        imagem = pg.transform.scale(imagem, (200, 200))
        sp.append(imagem)

    return sp


def DesenhaQuadrado():
    x = 0
    fund = []
    for i in range(12):
        if i < 3:
            a = pg.Rect(0 + x, 0, 210, 200)
            fund.append(a)
            x += 200

        if i == 3:
            x = 0

        if 3 <= i < 6:
            a = pg.Rect(0 + x, 200, 210, 200)
            fund.append(a)
            x += 200

        if i == 6:
            x = 0

        if 6 <= i < 9:
            a = pg.Rect(0 + x, 400, 210, 200)
            fund.append(a)
            x += 200

        if i == 9:
            x = 0

        if 9 <= i < 12:
            a = pg.Rect(0 + x, 600, 210, 200)
            fund.append(a)
            x += 200

    return fund


def menu_inicial(numero_jogadores):
    pg.init()
    screen = pg.display.set_mode((605, 800))
    pg.display.set_caption("Escolha do Pokemon")
    pokemon = []
    start = True
    contador = 0
    cores = [(0, 128, 0), (244, 164, 96), (153, 51, 153), (0, 0, 255), (255, 0, 0), (255, 0, 127), (255, 214, 5),
             (158, 240, 0), (150, 150, 150), (26, 151, 249), (3, 119, 9), (76, 3, 119)]
    pokemons = ["Sceptile", "Flygon", "Gengar", "Milotic", "Ninetales", "Gardevoir", "Jolteon", "Scizor", "Noctowl",
                "Walrein", "Cradily", "Crobat"]

    splashs = []
    quadrados = DesenhaQuadrado()


    for pk in pokemons:
        string = "Sprites\\splash\\" + pk + ".png"
        a = pg.image.load(string)
        a = pg.transform.scale(a, (200, 200))
        splashs.append(a)



    while start:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                start = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                pokemon.append(Clicou(pos))
                contador += 1
                if numero_jogadores == 2 and contador >= 2:
                    start = False
                if numero_jogadores == 1:
                    start = False
        PrintFundo(quadrados, screen, cores)
        PrintSplashs(splashs, screen)

        pg.display.flip()
        pg.display.update()
    return pokemon
