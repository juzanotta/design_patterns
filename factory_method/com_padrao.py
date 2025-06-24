class Pokemon:
    def __init__(self, nome: str):
        self.nome = nome


    def atacar(self):
        raise NotImplementedError("Subclasses devem implementar atacar().")


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu")


    def atacar(self):
        print(f"{self.nome} usa Thunderbolt!")


class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander")
    def atacar(self):
        print(f"{self.nome} usa Ember!")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle")
    def atacar(self):
        print(f"{self.nome} usa Water Gun!")


# criador abstrato
class PokemonCreator:
    def criar_pokemon(self) -> Pokemon:
        raise NotImplementedError("Subclasses devem sobrescrever criar_pokemon().")


    def executar_ataque(self):
        p = self.criar_pokemon()
        p.atacar()


# criadores concretos
class PikachuCreator(PokemonCreator):
    def criar_pokemon(self) -> Pokemon:
        return Pikachu()


class CharmanderCreator(PokemonCreator):
    def criar_pokemon(self) -> Pokemon:
        return Charmander()


class SquirtleCreator(PokemonCreator):
    def criar_pokemon(self) -> Pokemon:
        return Squirtle()


def main():
    print("\nCom Factory Method:\n")
    creators = [PikachuCreator(), CharmanderCreator(), SquirtleCreator()]
    for c in creators:
        c.executar_ataque()

if __name__ == "__main__":
    main()
    print()