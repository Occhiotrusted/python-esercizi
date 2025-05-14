# PRIMO ESERCIZIO

def saluta():
    print("Benvenuto, utente!")

saluta()

# SECONDO ESERCIZIO
def quadrato(numero):
    print("Quadrato:", numero**2)

quadrato(3)

# TERZO ESERCIZIO

def n_pari(numero):
    if numero % 2 == 0:
        print("Il numero "+ str(numero) + " è pari")
    else:
        print("Il numero "+ str(numero) + " non è pari")

n_pari(3)

# QUARTO ESERCIZIO

def media(lista_numeri):
    return sum(lista_numeri) / len(lista_numeri)

m = media([25,61,2,57,8])
print(m)
