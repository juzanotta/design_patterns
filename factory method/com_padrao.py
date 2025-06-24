class Pokemon:
    def __init__(this, nome: str):
        this.nome = nome

    def atacar(this):
        raise NotImplementedError("Subclasses devem implementar atacar().")

class Pikachu(Pokemon):
    def __init__(this):
        super().__init__("Pikachu")
    def atacar(this):
        print(f"{this.nome} usa Thunderbolt!")

class Charmander(Pokemon):
    def __init__(this):
        super().__init__("Charmander")
    def atacar(this):
        print(f"{this.nome} usa Ember!")

class Squirtle(Pokemon):
    def __init__(this):
        super().__init__("Squirtle")
    def atacar(this):
        print(f"{this.nome} usa Water Gun!")

# criador abstrato
class PokemonCreator:
    def criar_pokemon(this) -> Pokemon:
        raise NotImplementedError("Subclasses devem sobrescrever criar_pokemon().")

    def executar_ataque(this):
        p = this.criar_pokemon()
        p.atacar()

# criadores concretos
class PikachuCreator(PokemonCreator):
    def criar_pokemon(this) -> Pokemon:
        return Pikachu()

class CharmanderCreator(PokemonCreator):
    def criar_pokemon(this) -> Pokemon:
        return Charmander()

class SquirtleCreator(PokemonCreator):
    def criar_pokemon(this) -> Pokemon:
        return Squirtle()

def main():
    print("=== Com Factory Method ===")
    creators = [PikachuCreator(), CharmanderCreator(), SquirtleCreator()]
    for c in creators:
        c.executar_ataque()