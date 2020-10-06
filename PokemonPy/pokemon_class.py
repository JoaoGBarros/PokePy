import moves_class as mv
import Status_class as st
import Type_class as tp


class Pokemon:
    stab = 1.5
    res = 0.5
    effective = 2

    def __init__(self, nome, tipo1, tipo2):
        self.nome = nome
        self.nickname = 0
        self.stats = 0
        self.type = tp.Type(tipo1, tipo2)
        self.moves = []
        self.level = 100
        self.back_sprite = 0
        self.front_sprite = 0
        self.capturado = 0
        self.pokeball = 0

    def set_stats(self, hp, attack, defense, sp_attack, sp_defense, speed):
        self.stats = st.Status(hp, attack, defense, sp_attack, sp_defense, speed)

    def set_moves(self, move, damage, pp, category, element, accuracy):
        self.moves.append(mv.Moves(move, damage, pp, category, element, accuracy))

    def set_nickname(self, nickname):
        self.nickname = nickname

    def get_moves(self):
        lista = []

        for at in self.moves:
            lista.append(at.get_ataque())

        return lista

    def get_atribbutes(self):
        return self.stats.get_stats()