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

class AplicacaoPokemon:
    def __init__(this, tipo: str):
        this.tipo = tipo.lower()

    def executar_ataque(this):
        if this.tipo == "pikachu":
            p = Pikachu()
        elif this.tipo == "charmander":
            p = Charmander()
        elif this.tipo == "squirtle":
            p = Squirtle()
        else:
            raise ValueError(f"Pokémon desconhecido: {this.tipo}")
        p.atacar()

def main():
    print("=== Sem Factory Method ===")
    for tipo in ["pikachu", "charmander", "squirtle"]:
        app = AplicacaoPokemon(tipo)
        app.executar_ataque()

if __name__ == "__main__":
    main()
