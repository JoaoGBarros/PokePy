import pokemon_class as pc


def ConfiguraPokemon(file, f):
    dep = []
    file.seek(0)
    while file.tell() != f:

        linha = file.readline()
        nome, type1, type2 = linha.split()
        pk = pc.Pokemon(nome, type1, type2)
        linha = file.readline()
        hp, attack, defense, sp_attack, sp_defense, speed = linha.split()
        pk.set_stats(int(hp), int(attack), int(defense), int(sp_attack), int(sp_defense), int(speed))
        for i in range(4):
            move = file.readline()
            move = move.strip("\n")
            linha = file.readline()
            damage, pp, category, element, accuracy = linha.split()
            pk.set_moves(move, int(damage), int(pp), int(category), element, int(accuracy))
        dep.append(pk)
        linha = file.readline()

    return dep


