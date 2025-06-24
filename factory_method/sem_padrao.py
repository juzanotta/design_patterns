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


class AplicacaoPokemon:
    def __init__(self, tipo: str):
        self.tipo = tipo.lower()


    def executar_ataque(self):
        if self.tipo == "pikachu":
            p = Pikachu()
        elif self.tipo == "charmander":
            p = Charmander()
        elif self.tipo == "squirtle":
            p = Squirtle()
        else:
            raise ValueError(f"Pokémon desconhecido: {self.tipo}")
        p.atacar()


def main():
    print("\nSem Factory Method:\n")
    for tipo in ["pikachu", "charmander", "squirtle"]:
        app = AplicacaoPokemon(tipo)
        app.executar_ataque()

if __name__ == "__main__":
    main()
    print()
