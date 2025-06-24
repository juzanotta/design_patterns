class Pokemon:
    def __init__(self, nome, tipo, hp, ataque, defesa):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa


    def exibir(self):
        print(f"{self.nome} ({self.tipo}) - HP: {self.hp}, ATK: {self.ataque}, DEF: {self.defesa}")


print("\nSem Prototype:\n")

pikachu = Pokemon("Pikachu", "Elétrico", 35, 55, 40)
print("Original:")
pikachu.exibir()

copia = Pokemon(pikachu.nome, pikachu.tipo, pikachu.hp, pikachu.ataque, pikachu.defesa)
print("\nCópia Manual:")
copia.exibir()
print()