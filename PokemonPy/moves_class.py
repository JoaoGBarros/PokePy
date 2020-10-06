class Moves:

    def __init__(self, move, damage, pp, category, element, accuracy):
        self.move = move
        self.damage = damage
        self.max_pp = pp
        self.pp = pp
        self.category = category
        self.element = element
        self.accuracy = accuracy

    def get_ataque(self):
        lista = {
            self.move: [self.damage, self.element, self.accuracy, self.pp, self.category]
        }
        return lista