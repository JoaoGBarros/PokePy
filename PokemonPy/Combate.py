import random as rand
import menu_batalha as mb

def Print_Ataque(play1, movimento, texto, screen):
    movimento_turno = play1.nome + " used " + play1.moves[movimento].move
    mb.Texto(movimento_turno, texto, screen)


def CalculaDano(play1, play2, s, movimento, texto, screen):
    crit = rand.randint(0, 100) / 100
    mult = rand.randint(85, 100) / 100
    ef = 0
    res = 0
    lev = play1.level
    critical = 0

    if crit > 0.85:
        lev = play1.level * 2
        critical = 1

    dano = (2 * lev / 5) + 2
    if play1.moves[movimento].category == 1:
        dano = dano * play1.moves[movimento].damage
        dano = dano * (play1.stats.ataque / play2.stats.defense)
    elif play1.moves[movimento].category == 2:
        dano = dano * play1.moves[movimento].damage
        dano = dano * (play1.stats.sp_attack / play2.stats.sp_defense)

    dano = (dano / 50) + 2

    if s == 1:
        dano = dano * play1.stab

    for at in play2.type.weakness:
        if play1.moves[movimento].element in at:
            ef += 1

    for ol in play2.type.resistence:
        if play1.moves[movimento].element in ol:
            res += 1

    if ef == 0 and res == 0:
        Print_Ataque(play1, movimento, texto, screen)
    elif ef > 0:
        Print_Ataque(play1, movimento, texto, screen)
        dano = dano * (ef * play1.effective)
    elif res > 0:
        Print_Ataque(play1, movimento, texto, screen)
        dano = dano * (play1.res / res)

    if ef == 1 and res == 0:
        effective = 'It Was Effective!!'
        mb.Texto(effective, texto, screen)
        print(effective)
    elif ef == 2 and res == 0:
        super_effective = 'It was Super Effective!!'
        mb.Texto(super_effective, texto, screen)
        print(super_effective)

    if res == 1 and ef == 0:
        not_very_effective = 'It wasn`t very effective!!'
        mb.Texto(not_very_effective, texto, screen)
        print(not_very_effective)
    elif res == 2 and ef == 0:
        not_effective = 'It wasn`t effective!!'
        mb.Texto(not_effective, texto, screen)
        print(not_effective)

    if critical == 1:
        criti = 'Critical Hit!'
        mb.Texto(criti, texto, screen)
        print(criti)

    dano = dano / 2
    dano = dano * mult

    return int(dano)


def Ataca(play1, play2, movimento, texto, screen):
    s = 0
    imune = False
    acerto = rand.randint(0, 100)
    if acerto <= play1.moves[movimento].accuracy:
        if play1.moves[movimento].element in play2.type.immunity:
            it_doesnt = "It doesnt affect " + play2.nome + "!!"
            imune = True
            mb.Texto(it_doesnt, texto, screen)
        if play1.moves[movimento].element == play1.type.type1 or play1.moves[movimento].element == play1.type.type2:
            s = 1
        if not imune:
            dano = CalculaDano(play1, play2, s, movimento, texto, screen)
            print("{} sofreu {} de dano".format(play2.nome, dano))
            play1.moves[movimento].pp = play1.moves[movimento].pp - 1
            print(play2.stats.hp)
            play2.stats.hp = play2.stats.hp - dano
            if play2.stats.hp < 0:
                play2.stats.hp = 0
            print(play2.stats.hp)
    else:
        missed = "It missed !!"
        mb.Texto(missed, texto, screen)
