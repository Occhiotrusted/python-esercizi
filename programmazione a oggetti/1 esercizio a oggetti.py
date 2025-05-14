class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def verso(self):
        print("La "+self.specie, "di nome", self.nome, "ha fatto un verso")


animale = Animale("Shizu", "rana")
animale.verso()