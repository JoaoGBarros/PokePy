import pygame as pg
import random as rand
import menu_batalha as mb
import Combate as comb





def Luta(barra_ataques, play1, play2, seta, texto, escolhidos, screen, background, lista_pokemons,  barra_hp_1,
         barra_hp_2, info):
    pg.font.init()
    comandos = pg.font.Font('Sprites\\fonte\\pokemon_fire_red.ttf', 50)
    rodando = True
    seta_X = 30
    seta_Y = 425
    j = 0
    turno = 0
    clock = pg.time.Clock()
    aux = play1
    while rodando:
        at = 0
        x = 0
        y = 0
        clock.tick(5)

        if len(escolhidos) > 1 or play1.nome == escolhidos[0]:
            mb.fundo(background, 0, 0, texto, 0, 377, screen)
            mb.SpawnaPokemon(play1, play2, screen, lista_pokemons, turno, escolhidos,  barra_hp_1, barra_hp_2, info)
            screen.blit(barra_ataques, (0, 377))

            for i in range(4):
                a = play1.moves[i].move
                text = comandos.render(a, 1, (0, 0, 0))
                if i >= 2:
                    x = 0
                    if i > 2:
                        x += 350
                    else:
                        x = 0
                        y += 75

                elif i == 1:
                    y = 0
                    x += 350
                screen.blit(text, (75 + x, 425 + y))
            seta = pg.transform.scale(seta, (40, 40))
        pg.display.update()


        if len(escolhidos) > 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_z:
                        if seta_X == 30 and seta_Y == 425:
                            movimento = 0
                            comb.Ataca(play1, play2, movimento, texto, screen)
                            turno += 1
                            rodando = False
                        elif seta_X == 30 and seta_Y == 500:
                            movimento = 2
                            comb.Ataca(play1, play2, movimento, texto, screen)
                            turno += 1
                            rodando = False
                        elif seta_X == 380 and seta_Y == 425:
                            movimento = 1
                            comb.Ataca(play1, play2, movimento, texto, screen)
                            turno += 1
                            rodando = False
                        elif seta_X == 380 and seta_Y == 500:
                            movimento = 3
                            comb.Ataca(play1, play2, movimento, texto, screen)
                            turno += 1
                            rodando = False


                    if event.key == pg.K_LEFT:
                        if seta_X - 350 >= 30:
                            seta_X -= 350

                    elif event.key == pg.K_RIGHT:
                        if seta_X + 350 <= 380:
                            seta_X += 350

                    elif event.key == pg.K_UP:
                        if seta_Y - 75 >= 425:
                            seta_Y -= 75

                    elif event.key == pg.K_DOWN:
                        if seta_Y + 75 <= 500:
                            seta_Y += 75

                    if event.key == pg.K_x:
                        rodando = False
        else:
            if play1.nome == escolhidos[0]:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_z:
                            if seta_X == 30 and seta_Y == 425:
                                movimento = 0
                                comb.Ataca(play1, play2, movimento, texto, screen)
                                turno += 1
                                rodando = False
                            elif seta_X == 30 and seta_Y == 500:
                                movimento = 2
                                comb.Ataca(play1, play2, movimento, texto, screen)
                                turno += 1
                                rodando = False
                            elif seta_X == 380 and seta_Y == 425:
                                movimento = 1
                                comb.Ataca(play1, play2, movimento, texto, screen)
                                turno += 1
                                rodando = False
                            elif seta_X == 380 and seta_Y == 500:
                                movimento = 3
                                comb.Ataca(play1, play2, movimento, texto, screen)
                                turno += 1
                                rodando = False

                        if event.key == pg.K_LEFT:
                            if seta_X - 350 >= 30:
                                seta_X -= 350
                        elif event.key == pg.K_RIGHT:
                            if seta_X + 350 <= 380:
                                seta_X += 350
                        elif event.key == pg.K_UP:
                            if seta_Y - 75 >= 425:
                                seta_Y -= 75
                        elif event.key == pg.K_DOWN:
                            if seta_Y + 75 <= 500:
                                seta_Y += 75

                        if event.key == pg.K_x:
                            rodando = False
            else:
                movimento = rand.randint(0, 3)
                comb.Ataca(play1, play2, movimento, texto, screen)
                turno += 1
                break


        if seta_X == 30 and seta_Y == 425:
            at = 1
        elif seta_X == 30 and seta_Y == 500:
            at = 3
        elif seta_X == 380 and seta_Y == 425:
            at = 2
        elif seta_X == 380 and seta_Y == 500:
            at = 4

        if len(escolhidos) > 1 or play1.nome == escolhidos[0]:
            a = play1.moves[at - 1].pp
            a = str(a)
            pp = comandos.render(a, 1, (0, 0, 0))
            a = play1.moves[at - 1].max_pp
            a = str(a)
            max_pp = comandos.render(a, 1, (0, 0, 0))
            type = comandos.render(play1.moves[at - 1].element, 1, (0, 0, 0))
            screen.blit(pp, (870, 430))
            screen.blit(max_pp, (940, 430))
            screen.blit(type, (830, 500))
            screen.blit(seta, (seta_X, seta_Y))
            pg.display.update()
            j += 1

    return turno