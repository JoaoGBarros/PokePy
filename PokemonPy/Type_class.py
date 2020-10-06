class Type:

    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2
        self.weakness = self.PegaFraqueza()
        self.immunity = sum(self.Imune(), [])
        self.resistence = self.Resistencia()

    def PegaFraqueza(self):
        weak = []
        tipo = [self.type1, self.type2]

        for i in range(0, 2):
            if tipo[i] == 'Fire':
                weak.append(['Water', 'Ground', 'Rock'])

            elif tipo[i] == 'Water':
                weak.append(['Grass', 'Electric'])

            elif tipo[i] == 'Grass':
                weak.append(['Bug', 'Fire', 'Flying', 'Ice', 'Poison'])

            elif tipo[i] == 'Bug':
                weak.append(['Fire', 'Flying', 'Rock'])

            elif tipo[i] == 'Electric':
                weak.append(['Ground'])

            elif tipo[i] == 'Normal':
                weak.append(['Fighting'])

            elif tipo[i] == 'Rock':
                weak.append(['Water', 'Grass', 'Fight', 'Ground', 'Steel'])

            elif tipo[i] == 'Dark':
                weak.append(['Bug', 'Fight', 'Fairy'])

            elif tipo[i] == 'Fairy':
                weak.append(['Steel', 'Poison'])

            elif tipo[i] == 'Flying':
                weak.append(['Ice', 'Rock', 'Electric'])

            elif tipo[i] == 'Ground':
                weak.append(['Grass', 'Ice', 'Water'])

            elif tipo[i] == 'Poison':
                weak.append(['Psychic', 'Ground'])

            elif tipo[i] == 'Steel':
                weak.append(['Fight', 'Fire', 'Ground'])

            elif tipo[i] == 'Dragon':
                weak.append(['Dragon', 'Ice', 'Fairy'])

            elif tipo[i] == 'Ghost':
                weak.append(['Ghost', 'Dark'])

            elif tipo[i] == 'Ice':
                weak.append(['Fight', 'Fire', 'Rock', 'Steel'])

            elif tipo[i] == 'Psychic':
                weak.append(['Bug', 'Dark', 'Ghost'])

            elif tipo[i] == 'Fighting':
                weak.append(['Fairy', 'Flying', 'Psychic'])

        return weak

    def Imune(self):
        tipo = [self.type1, self.type2]
        imunidade = []

        for i in range(2):

            if tipo[i] == 'Normal':
                imunidade.append(['Ghost'])

            elif tipo[i] == 'Ghost':
                imunidade.append(['Normal', 'Fighting'])

            elif tipo[i] == 'Ground':
                imunidade.append(['Electric'])

            elif tipo[i] == 'Flying':
                imunidade.append(['Ground'])

            elif tipo[i] == 'Fairy':
                imunidade.append(['Dragon'])

            elif tipo[i] == 'Dark':
                imunidade.append(['Pyschic'])

            elif tipo[i] == 'Steel':
                imunidade.append(['Poison'])

        return imunidade

    def Resistencia(self):
        resist = []
        tipo = [self.type1, self.type2]

        for i in range(0, 2):
            if tipo[i] == 'Fire':
                resist.append(['Bug', 'Ice', 'Fairy', 'Grass', 'Steel'])

            elif tipo[i] == 'Water':
                resist.append(['Fire', 'Ice', 'Steel', 'Water'])

            elif tipo[i] == 'Grass':
                resist.append(['Electric', 'Grass', 'Ground', 'Water'])

            elif tipo[i] == 'Bug':
                resist.append(['Fighting', 'Grass', 'Ground'])

            elif tipo[i] == 'Electric':
                resist.append(['Electric', 'Flying', 'Steel'])

            elif tipo[i] == 'Normal':
                resist.append([''])

            elif tipo[i] == 'Rock':
                resist.append(['Fire', 'Flying', 'Normal', 'Poison'])

            elif tipo[i] == 'Dark':
                resist.append(['Dark', 'Ghost'])

            elif tipo[i] == 'Fairy':
                resist.append(['Bug', 'Dark', 'Fighting'])

            elif tipo[i] == 'Flying':
                resist.append(['Bug', 'Fighting', 'Grass'])

            elif tipo[i] == 'Ground':
                resist.append(['Poison', 'Rock'])

            elif tipo[i] == 'Poison':
                resist.append(['Bug', 'Fairy', 'Fighting', 'Grass', 'Poison'])

            elif tipo[i] == 'Steel':
                resist.append(
                    ['Bug', 'Dragon', 'Fairy', 'Flying', 'Grass', 'Ice', 'Normal', 'Psychic', 'Rock', 'Steel'])

            elif tipo[i] == 'Dragon':
                resist.append(['Electric', 'Fire', 'Grass', 'Water'])

            elif tipo[i] == 'Ghost':
                resist.append(['Bug', 'Poison'])

            elif tipo[i] == 'Ice':
                resist.append(['Ice'])

            elif tipo[i] == 'Psychic':
                resist.append(['Fighting', 'Psychic'])

            elif tipo[i] == 'Fighting':
                resist.append(['Bug', 'Dark', 'Rock'])

        return resist