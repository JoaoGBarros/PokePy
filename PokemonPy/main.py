import jogadores as jog
import menu_pokemon as mp
import menu_batalha as mb
import CriaPokemons as cp
import Bag as bg

if __name__ == "__main__":
    file = open("Pokemon.txt", "r")
    file.seek(0, 2)
    f = file.tell()
    lista_pokemons = cp.ConfiguraPokemon(file, f)
    if len(lista_pokemons) > 0:
        numero_jogadores = jog.menu_escolha()
        bag = bg.CriaBag(numero_jogadores)
        escolhidos = mp.menu_inicial(numero_jogadores)
        mb.SeparaPokemons(escolhidos, lista_pokemons, numero_jogadores, bag)


