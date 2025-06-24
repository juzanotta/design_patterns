import copy

class Pokemon:
    def __init__(self, nome, tipo, hp, ataque, defesa):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa


    def exibir(self):
        print(f"{self.nome} ({self.tipo}) - HP: {self.hp}, ATK: {self.ataque}, DEF: {self.defesa}")


    def clone(self):
        return copy.deepcopy(self)

print("\nCom Prototype:\n")

pikachu = Pokemon("Pikachu", "Elétrico", 35, 55, 40)
print("Original:")
pikachu.exibir()

copia = pikachu.clone()
print("\nClone:")
copia.exibir()
print()