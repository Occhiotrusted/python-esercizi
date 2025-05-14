from studente import Studente

mario = Studente("Mario", "Rossi", 2007)
mario.aggiungi_voto(7)
mario.aggiungi_voto(8)
mario.aggiungi_voto(6)
mario.scheda()
print("Media voti:", mario.media())
