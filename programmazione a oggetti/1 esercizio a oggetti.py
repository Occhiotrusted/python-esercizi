class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def verso(self, suono):
        print(f"La {self.specie} di nome {self.nome} fa: {suono}")


animale = Animale("Shizu", "rana")
animale.verso("braah braah")