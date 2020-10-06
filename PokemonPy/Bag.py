import Bag_class as bc
import pygame as pg
import Pokeball as pb

def CriaBag(numero_jogadores):
    bag = []
    a = bc.Bag()

    for i in range(numero_jogadores):
        a.set_Medicine("Potion", 20, 10)
        a.set_Medicine("Super Potion", 50, 7)
        a.set_Medicine("Hyper Potion", 200, 5)
        a.set_Medicine("Max Potion", 0, 1)

        if numero_jogadores == 1:
            a.set_Pokeball("Pokeball", 1.0, 50)
            a.set_Pokeball("Greatball", 1.5, 25)
            a.set_Pokeball("Ultraball", 2.0, 25)
            a.set_Pokeball("Masterball", 0, 1)

        bag.append(a)

    return bag



def BagBattle(barra_ataques, play1, seta, texto, escolhidos, screen, background, info, mochila, bag, play2):
    in_bag = True
    seta_x = 400
    seta_y = 50
    potion = pg.image.load("Sprites\\SpritesInterface\\potion.png")
    potion = pg.transform.scale(potion, (100, 100))
    superpotion = pg.image.load("Sprites\\SpritesInterface\\super potion.png")
    superpotion = pg.transform.scale(superpotion, (100, 100))
    hyperpotion = pg.image.load("Sprites\\SpritesInterface\\hyper potion.png")
    hyperpotion = pg.transform.scale(hyperpotion, (100, 100))
    maxpotion = pg.image.load("Sprites\\SpritesInterface\\max potion.png")
    maxpotion = pg.transform.scale(maxpotion, (100, 100))
    clock = pg.time.Clock()
    while in_bag:

        x = 0
        y = 0
        turno = 0
        mochila = pg.transform.scale(mochila, (1024, 576))
        screen.blit(mochila, (0, 0))
        clock.tick(10)

        if len(escolhidos) > 1:

            if play1.nome == escolhidos[0]:
                for i in range(4):
                    a = bag[0].Medicine[i].med
                    b = "X  " + str(bag[0].Medicine[i].qtd)
                    med = info.render(a, 1, (0, 0, 0))
                    qtd = info.render(b, 1, (0, 0, 0))
                    screen.blit(med, (450, 50 + y))
                    screen.blit(qtd, (800, 50 + y))

                    y += 60

                seta = pg.transform.scale(seta, (50, 50))
                titulo = info.render("Medicine", 1, (0, 0, 0))
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
                                if play1.stats.hp + bag[0].Medicine[0].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[0].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[0].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 110:
                                if play1.stats.hp + bag[0].Medicine[1].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[1].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[1].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 170:
                                if play1.stats.hp + bag[0].Medicine[2].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[2].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[2].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 230:
                                play1.stats.hp = play1.stats.max
                                bag[0].Medicine[3].qtd -= 1
                                turno += 1
                                in_bag = False

                        elif event.key == pg.K_x:
                            in_bag = False
                screen.blit(seta, (seta_x, seta_y))
                if seta_y == 50:

                    screen.blit(potion, (30, 440))

                elif seta_y == 110:
                    screen.blit(superpotion, (30, 440))

                elif seta_y == 170:
                    screen.blit(hyperpotion, (30, 440))

                elif seta_y == 230:
                    screen.blit(maxpotion, (30, 440))

                pg.display.update()

            else:
                for i in range(4):
                    a = bag[1].Medicine[i].med
                    b = "X  " + str(bag[1].Medicine[i].qtd)
                    med = info.render(a, 1, (0, 0, 0))
                    qtd = info.render(b, 1, (0, 0, 0))
                    screen.blit(med, (450, 50 + y))
                    screen.blit(qtd, (800, 50 + y))

                    y += 60

                seta = pg.transform.scale(seta, (50, 50))
                titulo = info.render("Medicine", 1, (0, 0, 0))
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
                                if play1.stats.hp + bag[1].Medicine[0].value <= play1.stats.max:
                                    play1.stats.hp += bag[1].Medicine[0].value
                                else:
                                    play1.stats.hp = play1.stats.max

                                turno += 1
                                bag[1].Medicine[0].qtd -= 1
                                in_bag = False
                            elif seta_y == 110:
                                if play1.stats.hp + bag[1].Medicine[1].value <= play1.stats.max:
                                    play1.stats.hp += bag[1].Medicine[1].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                turno += 1
                                bag[1].Medicine[1].qtd -= 1
                                in_bag = False
                            elif seta_y == 170:
                                if play1.stats.hp + bag[1].Medicine[2].value <= play1.stats.max:
                                    play1.stats.hp += bag[1].Medicine[2].value
                                else:
                                    play1.stats.hp = play1.stats.max

                                turno += 1
                                bag[1].Medicine[2].qtd -= 1
                                in_bag = False
                            elif seta_y == 230:
                                play1.stats.hp = play1.stats.max
                                bag[1].Medicine[3].qtd -= 1
                                turno += 1
                                in_bag = False
                        elif event.key == pg.K_x:
                            in_bag = False

                screen.blit(seta, (seta_x, seta_y))
                if seta_y == 50:

                    screen.blit(potion, (30, 440))

                elif seta_y == 110:
                    screen.blit(superpotion, (30, 440))

                elif seta_y == 170:
                    screen.blit(hyperpotion, (30, 440))

                elif seta_y == 230:
                    screen.blit(maxpotion, (30, 440))

                pg.display.update()


        else:
            if play1.nome == escolhidos[0]:
                for i in range(4):
                    a = bag[0].Medicine[i].med
                    b = "X  " + str(bag[0].Medicine[i].qtd)
                    med = info.render(a, 1, (0, 0, 0))
                    qtd = info.render(b, 1, (0, 0, 0))
                    screen.blit(med, (450, 50 + y))
                    screen.blit(qtd, (800, 50 + y))

                    y += 60

                seta = pg.transform.scale(seta, (50, 50))
                titulo = info.render("Medicine", 1, (0, 0, 0))
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
                                if play1.stats.hp + bag[0].Medicine[0].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[0].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[0].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 110:
                                if play1.stats.hp + bag[0].Medicine[1].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[1].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[1].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 170:
                                if play1.stats.hp + bag[0].Medicine[2].value <= play1.stats.max:
                                    play1.stats.hp += bag[0].Medicine[2].value
                                else:
                                    play1.stats.hp = play1.stats.max
                                bag[0].Medicine[2].qtd -= 1
                                turno += 1
                                in_bag = False
                            elif seta_y == 230:
                                play1.stats.hp = play1.stats.max
                                bag[0].Medicine[3].qtd -= 1
                                turno += 1
                                in_bag = False

                        elif event.key == pg.K_x:
                            in_bag = False

                        elif event.key == pg.K_RIGHT:
                            capt = pb.Pokeball(play2, bag, info, mochila, screen, seta, texto, background)
                            if capt == 1:
                                turno += 1
                                in_bag = False
                            else:
                                turno += 1
                screen.blit(seta, (seta_x, seta_y))

                if seta_y == 50:
                    screen.blit(potion, (30, 440))

                elif seta_y == 110:
                    screen.blit(superpotion, (30, 440))

                elif seta_y == 170:
                    screen.blit(hyperpotion, (30, 440))

                elif seta_y == 230:
                    screen.blit(maxpotion, (30, 440))

                pg.display.update()

    return turno