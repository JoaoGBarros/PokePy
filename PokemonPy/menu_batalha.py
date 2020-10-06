import pygame as pg
import random as rand
import Fight as ft
import time
import Bag as bg

"""def AnimacaoDerrota(background, texto, screen, play2, play1, escolhidos):
    clock = pg.time.Clock()
    andar = 0
    if play1.stats.hp == 0 and play1.nome == escolhidos[0]:
        y = CoordYPoke(play1.nome)
        img = pg.image.load('costas/' + play1.nome + '.png')
        img = pg.transform.scale(img, (250, 250))
        for i in range(10):
            clock.tick(1)
            fundo(background, 0, 0, texto, 0, 377, screen)
            screen.blit(img, (120 - andar, y))
            andar += 60
            pg.display.update()
    else:
        y = 0
        img = pg.image.load('frente/' + play2.nome + '.png')
        img = pg.transform.scale(img, (200, 200))

        while 150 - y > 120:
            fundo(background, 0, 0, texto, 0, 377, screen)
            screen.blit(img, (720, 150 - y))
            y += 10
            pg.display.update()"""

def Texto(string, texto, screen):
    co = pg.font.Font('Sprites\\fonte\\pokemon_fire_red.ttf', 50)
    texto = pg.transform.scale(texto, (1024, 200))
    screen.blit(texto, (0, 377))
    x = 0

    for i in string:
        letra = co.render(i, 1, (0, 0, 0))
        screen.blit(letra, (40+x, 450))
        pg.time.delay(100)
        pg.display.update()
        x += 20
    time.sleep(0.2)


def PrintTreinador(spr, coord_trainer_x, coord_trainer_y, screen):
    screen.blit(spr, (coord_trainer_x, coord_trainer_y))


def fundo(background, coord_back_X, coord_back_Y, texto, coord_text_X, coord_text_Y, screen):
    background = pg.transform.scale(background, (1024, 376))
    texto = pg.transform.scale(texto, (1024, 200))
    screen.blit(background, (coord_back_X, coord_back_Y))
    screen.blit(texto, (coord_text_X, coord_text_Y))


def menu(main_menu, coord_menu_X, coord_menu_Y, seta, coord_seta_X, coord_seta_Y, screen):
    main_menu = pg.transform.scale(main_menu, (510, 190))
    screen.blit(main_menu, (coord_menu_X, coord_menu_Y))
    seta = pg.transform.scale(seta, (40, 40))
    screen.blit(seta, (coord_seta_X, coord_seta_Y))


def animacao(treinador, andar, screen, background, coord_back_X, coord_back_Y, texto, coord_text_X, coord_text_Y, joga, clock):
    for i in range(10):
        if i >= 4:
            spr = treinador[3]
        else:
            spr = treinador[i]
        fundo(background, coord_back_X, coord_back_Y, texto, coord_text_X, coord_text_Y, screen)
        PrintTreinador(spr, 120 - andar, 80, screen)
        if joga > 1:
            PrintTreinador(treinador[4], 570+andar, 20, screen)
        pg.display.update()
        if i == 0:
            clock.tick(1)
        else:
            clock.tick(12)
        andar += 60


def CoordYPoke(nome):

    if nome == "Sceptile" or "Ninetales" or "Gardevoir" or "Jolteon":
        y = 150
    elif nome == "Milotic" or "Walrein" or "Cradily":
        y = 75
    elif nome == "Flygon":
        y = 90
    elif nome == "Gengar":
        y = 113
    elif nome == "Scizor":
        y = 100
    elif nome == "Noctowl":
        y = 92
    elif nome == "Crobat":
        y = 80

    return y


def BarraVida1(play1, escolhidos):

    damage = play1.stats.max - play1.stats.hp

    tam = 100 * damage / play1.stats.max
    tam = 140 * tam / 100
    tam = int(tam)
    if len(escolhidos) == 1 and play1.nome != escolhidos[0]:
        v = pg.Rect(220, 105, 140 - tam, 12)
    else:
        v = pg.Rect(790, 312, 140 - tam, 12)


    return v

def BarraVida2(play2, escolhidos):
    damage = play2.stats.max - play2.stats.hp

    tam = 100 * damage / play2.stats.max
    tam = 140 * tam / 100
    tam = int(tam)
    if len(escolhidos) == 1 and play2.nome == escolhidos[0]:
        v = pg.Rect(790, 312, 140 - tam, 12)
    else:
        v = pg.Rect(220, 105, 140 - tam, 12)

    return v

def GetCor(play1, play2):
    w = [0, 0]

    if play1.stats.hp > play1.stats.max * 0.5:
        w[0] = (50, 205, 50)
    elif play1.stats.max * 0.3 < play1.stats.hp <= play1.stats.max * 0.5:
        w[0] = (255, 255, 0)
    elif play1.stats.hp <= play1.stats.max * 0.3:
        w[0] = (255, 0, 0)

    if play2.stats.hp > play2.stats.max * 0.5:
        w[1] = (50, 205, 50)
    elif play2.stats.max * 0.3 < play2.stats.hp <= play2.stats.max * 0.5:
        w[1] = (255, 255, 0)
    elif play2.stats.hp <= play2.stats.max * 0.3:
        w[1] = (255, 0, 0)

    return w


def SpawnaPokemon(play1, play2, screen, lista_pokemon, turno, escolhidos, barra_hp_1, barra_hp_2, info):

    """Coordenada bonita para cada pokemon
        Sceptile: x 120 y 105 -
        Flygon: x 120 y 90
        Milotic: x 120   y 75 -
        Gengar: x 120 y 113
        Ninetales: x 120 y 105 -
        Gardevor: 120 y 105 -
        Jolteon: x 120 y 105 -
        Scizor: x 120 y 100
        Noctowl: x 120 y 92
        Walrein x 120 y 75 -
        Cradily x 120 y 75 -
        Crobat x 120 y 80



    """
    i = 0
    if len(escolhidos) > 1:
        nomeBS = play1.nome
        nomeFS = play2.nome
    else:
        if play1.nome == escolhidos[0]:
            nomeBS = play1.nome
            nomeFS = play2.nome
        else:
            nomeBS = play2.nome
            nomeFS = play1.nome

    bs = pg.image.load('Sprites\\costas\\' + nomeBS + ".png")
    if play2.capturado == 0:
        fs = pg.image.load('Sprites\\frente\\' + nomeFS + ".png")
        fs = pg.transform.scale(fs, (200, 200))
    else:
        fs = pg.image.load("Sprites\\SpritesInterface\\" + play2.pokeball + ".png")
        fs = pg.transform.scale(fs, (50, 50))
    bs = pg.transform.scale(bs, (250, 250))
    y = CoordYPoke(nomeBS)
    lv1 = str(play1.level)
    lv2 = str(play2.level)
    nome1 = info.render(nomeBS, 1, (0, 0, 0))
    level1 = info.render(lv1, 1, (0, 0, 0))
    level2 = info.render(lv2, 1, (0, 0, 0))
    nome2 = info.render(nomeFS, 1, (0, 0, 0))
    if len(escolhidos) > 1:
        vida1 = BarraVida1(play1, escolhidos)
        vida2 = BarraVida2(play2, escolhidos)
    else:
        vida1 = BarraVida1(play1, escolhidos)
        vida2 = BarraVida2(play2, escolhidos)
    screen.blit(bs, (120, y))
    if play2.capturado == 0:
        screen.blit(fs, (625, 60))
    else:
        screen.blit(fs, (720, 150))
    screen.blit(barra_hp_1, (650, 265))
    screen.blit(barra_hp_2, (100, 50))
    screen.blit(nome1, (700, 275))
    screen.blit(level1, (880, 280))
    screen.blit(nome2, (130, 60))
    screen.blit(level2, (290, 60))
    warning = GetCor(play1, play2)
    pg.draw.rect(screen, warning[0], vida1)
    pg.draw.rect(screen, warning[1], vida2)
    pg.display.update()

def menu_batalha(play1, play2, lista_pokemons, escolhidos, j, bag):
    pg.init()

    # Cria a tela
    screen = pg.display.set_mode((1024, 576))

    # Titulo e icone
    pg.display.set_caption("Pokemon")
    icon = pg.image.load('Sprites\\SpritesInterface\\gaming.png')
    pg.display.set_icon(icon)
    background = pg.image.load('Sprites\\SpritesInterface\\FundoPokemon.png').convert()
    main_menu = pg.image.load('Sprites\\SpritesInterface\\fgt_options.png').convert()
    texto = pg.image.load('Sprites\\SpritesInterface\\text_bar.png').convert()
    seta = pg.image.load('Sprites\\SpritesInterface\\le_setinha.png').convert()
    barra_hp_1 = pg.image.load('Sprites\\SpritesInterface\\barra_2.png')
    barra_hp_2 = pg.image.load('Sprites\\SpritesInterface\\barra_1.png')
    barra_hp_1 = pg.transform.scale(barra_hp_1, (300, 100))
    barra_hp_2 = pg.transform.scale(barra_hp_2, (300, 100))
    barra_ataques = pg.image.load('Sprites\\SpritesInterface\\pp_bar.png')
    barra_ataques = pg.transform.scale(barra_ataques, (1024, 200))
    info = pg.font.Font('Sprites\\fonte\\pokemon_fire_red.ttf', 35)
    mochila = pg.image.load('Sprites\\SpritesInterface\\FRLGBag.png')

    treinador = []
    for i in range(1, 5):
        n = str(i)
        trainer = pg.image.load('Sprites\\trainer\\costas_' + n + ".png")
        trainer = pg.transform.scale(trainer, (300, 300))
        treinador.append(trainer)
        if len(escolhidos) > 1 and i == 4:
            trainer = pg.image.load('Sprites\\trainer\\frente_2.png')
            trainer = pg.transform.scale(trainer, (200, 200))
            treinador.append(trainer)


    turno = 0
    clock = pg.time.Clock()
    running = True
    posicao_seta_x = 540
    posicao_seta_y = 430
    aux = play1
    adcTurno = 0
    # Loop para rodar
    while running:
        # RGB

        adcTurno = 0



        screen.fill((0, 0, 0))

        fundo(background, 0, 0, texto, 0, 377, screen)
        menu(main_menu, 512, 380, seta, posicao_seta_x, posicao_seta_y, screen)
        andar = 120
        if j == 0:
            pg.mixer.music.load("Pokemon Sword & Shield - Marnie Final Battle Music (HQ).mp3")
            pg.mixer.music.play()
            print(pg.mixer.music.get_volume())
            pg.mixer.music.set_volume(0.35)
            animacao(treinador, andar, screen, background, 0, 0, texto, 0, 377, len(escolhidos), clock)
            j += 1

        SpawnaPokemon(play1, play2, screen, lista_pokemons, turno, escolhidos, barra_hp_1, barra_hp_2, info)

        if len(escolhidos) == 1 and play1.nome != escolhidos[0]:
            adcTurno = ft.Luta(barra_ataques, play1, play2, seta, texto, escolhidos, screen, background,
                               lista_pokemons, barra_hp_1, barra_hp_2, info)
        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if posicao_seta_y + 60 <= 490:
                            j += 1
                            posicao_seta_y += 60
                    elif event.key == pg.K_UP:
                        if posicao_seta_y - 60 >= 430:
                            j += 1
                            posicao_seta_y -= 60
                    elif event.key == pg.K_LEFT:
                        if posicao_seta_x - 230 >= 540:
                            j += 1
                            posicao_seta_x -= 230
                    elif event.key == pg.K_RIGHT:
                        if posicao_seta_x + 230 <= 770:
                            j += 1
                            posicao_seta_x += 230
                    elif event.key == pg.K_z:
                        if posicao_seta_x == 540 and posicao_seta_y == 430:
                            adcTurno = ft.Luta(barra_ataques, play1, play2, seta, texto, escolhidos, screen, background, lista_pokemons,
                                    barra_hp_1, barra_hp_2, info)

                        if posicao_seta_x == 540 and posicao_seta_y == 490:
                            stt = "AINDA NAO BOTEI, DESCULPA!"
                            Texto(stt, texto, screen)

                        if posicao_seta_x == 770 and posicao_seta_y == 430:
                            adcTurno = bg.BagBattle(barra_ataques, play1, seta, texto, escolhidos, screen, background, info,
                                         mochila, bag, play2)


                        if posicao_seta_x == 770 and posicao_seta_y == 490:
                            run = rand.randint(0, 10)
                            if run <= 7:
                                stt = play1.nome + " fled from the battle!"
                                Texto(stt, texto, screen)
                                running = False
                            else:
                                stt = "Couldn't run away!"
                                Texto(stt, texto, screen)

            # Local ideal menu x:512 y:380
            # Fight x:540 y:430
            # Pokemon x:540 y:490
            # Bag x:770 y:430
            # Run x:770 y:490
            if play1.stats.hp <= 0 or play2.stats.hp <= 0:
                if play1.stats.hp == 0:
                    stt = play2.nome + " won the battle!!"
                else:
                    stt = play1.nome + " won the battle!!"
                fundo(background, 0, 0, texto, 0, 377, screen)
                SpawnaPokemon(play1, play2, screen, lista_pokemons, turno, escolhidos, barra_hp_1, barra_hp_2, info)
                #AnimacaoDerrota(background, texto, screen, play2, play1, escolhidos)
                Texto(stt, texto, screen)
                running = False
            elif play2.capturado == 1:
                fundo(background, 0, 0, texto, 0, 377, screen)
                SpawnaPokemon(play1, play2, screen, lista_pokemons, turno, escolhidos, barra_hp_1, barra_hp_2, info)
                stt = "Congrats!!" + play2.nome + " got caught!!!"
                Texto(stt, texto, screen)
                running = False

        if adcTurno == 1:
            turno += adcTurno
            if turno > 0:
                if turno % 2 == 0:
                    play2 = play1
                    play1 = aux

                else:
                    play1 = play2
                    play2 = aux

        pg.display.update()




def SeparaPokemons(escolhidos, lista_pokemons, numero_jogadores, bag):

    contador = 0

    for i in range(len(escolhidos)):
        for j in range(len(lista_pokemons)):
            if escolhidos[i] == lista_pokemons[j].nome and contador == 0:
                play1 = lista_pokemons[j]
                contador += 1
            elif escolhidos[i] == lista_pokemons[j].nome and contador > 0:
                play2 = lista_pokemons[j]

    if numero_jogadores == 1:
        while True:
            pc = rand.randint(0, len(lista_pokemons) - 1)
            if lista_pokemons[pc].nome != escolhidos[0]:
                play2 = lista_pokemons[pc]
                break


    if play1.stats.speed <= play2.stats.speed:
        aux = play1
        play1 = play2
        play2 = aux

    j = 0

    menu_batalha(play1, play2, lista_pokemons, escolhidos, j, bag)
