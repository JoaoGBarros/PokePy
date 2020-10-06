class Pokeball:

    def __init__(self, ball, rate, qtd):
        self.ball = ball
        self.rate = rate
        self.qtd = qtd


class Medicine:

    def __init__(self, med, value, qtd):
        self.med = med
        self.value = value
        self.qtd = qtd

class Bag:
    def __init__(self):
        self.Pokeball = []
        self.Medicine = []

    def set_Pokeball(self, ball, rate, qtd):
        self.Pokeball.append(Pokeball(ball, rate, qtd))

    def set_Medicine(self, med, value, qtd):
        self.Medicine.append((Medicine(med, value, qtd)))