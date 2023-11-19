"""
Il programma crea una superficie rettangolare costituita da quadratini che assumono
il colore dello sfondo o un altro colore in funzione delle coordinate inserite dall'utente
"""

from pytamaro.it import (accanto, Colore, Grafica,
grafica_vuota, rettangolo, salva_animazione, sopra, visualizza_grafica, salva_grafica, sovrapponi)

BIANCO = Colore(255, 255, 255, 255)
NERO = Colore(0, 0, 0, 255)
SFONDO_SCHERMO = NERO
COLORE_SU_SCHERMO = BIANCO

LUNGHEZZA_RIGA = 300
NUMERO_RIGHE = 300

NUMERO_MASSIMO_COORDINATE = 8
LATO_QUADRATINO = 5
    
def crea_lista_bidimensionale() -> list[list[int]]:
    """
    Crea una lista di liste di zeri che rappresenta lo "schermo" vuoto.
    :returns: lista bidimensionale che rappresenta lo schermo, ancora "vuoto"
    """
    matrice = []
    for riga in range(NUMERO_RIGHE):
        riga_zeri = [0] * LUNGHEZZA_RIGA
        matrice.append(riga_zeri) 
    return matrice

def indaga_controlla(valore_minimo: int, valore_massimo: int) -> int:
    """
    Chiede un input e controlla che il valore inserito sia un valore intero
    entro un intervallo definito.
    Se le condizioni non sono rispettate, viene richiesto un valore; questo fino a quando
    le condizioni sono rispettate, poi viene restituito il valore.
    
    :param valore_minimo: valore minimo che deve avere il numero intero fornito come input
    :param valore_massimo: valore massimo che deve avere il numero intero fornito come input
    :returns: primo valore lecito dell'imain_esempio_video()nput fornito dall'utente
    """
    condizione = False
    while condizione == False:
        try:
            valore_inserito = int(input("Inserire un numero intero nell'intervallo corretto. "))
            if valore_inserito < valore_minimo or valore_inserito > valore_massimo:
                raise ValueError
        except ValueError:
            print("Input non adeguato. ")
        else:
            print("Inserimento riuscito. ")
            condizione = True     
    return valore_inserito
    
def accogli_coordinate() -> list[int, int]:
    """
    Chiede all'utente di inserire le coordinate, valore x e valore y.
    :returns: coordinata_x e coordinata_y
    """
    print("Inserisci coordinata x")
    coordinata_x = indaga_controlla(0, LUNGHEZZA_RIGA - 1)
    print("inserisci coordinata y")
    coordinata_y = indaga_controlla(0, NUMERO_RIGHE - 1)
    return [coordinata_x, coordinata_y]

def chiedi_numero_coordinate() -> int:
    """
    Permette all'utente di definire il numero di coordinate che vuole inserire.
    :returns: il valore int inserito dall'utente
    """
    print("Quante coordinate vanno inserite?")
    numero_coordinate_desiderato = indaga_controlla(0, NUMERO_MASSIMO_COORDINATE)
    return numero_coordinate_desiderato

def crea_lista_coordinate(numero: int) -> list[list[int, int]]:
    """
    Crea una lista di liste che contengono le coordinate scelte dall'utente.
    :param numero: numero di volte che deve richiamare accogli_coordinate
    :returns: la lista di coordinate in forma di liste di liste
    """
    lista_coordinate = []
    for indice in range(int(numero)):
        coordinate = accogli_coordinate()
        lista_coordinate.append(coordinate)
    return lista_coordinate

def modifica_lista_bidimensionale(lista_coordinate: list[list[int, int]], lista_bidimensionale: list[list[int]]) -> list[list[int]]:
    """
    Modifica la lista bidimensionale in modo che dove indicato con le coordinate dell'utente,
    lo 0 viene rimpiazzato da 1
    :param lista_coordinate: lista di coordinate inserite dall'utente in forma tuple
    :returns:lista bidimensionale modificata in base alle coordinate inserite dall'utente
    """
    for i in lista_coordinate:
        lista_bidimensionale[int(i[1])][int(i[0])] = 1
    return lista_bidimensionale


def crea_grafica_schermo(lista_bidimensionale: list[list[int]]) -> Grafica:
    """
    Mappa la lista bidimensionale in modo che gli 0 e gli 1 diventano quadrati
    di colore dello sfondo rispettivamente di un altro colore
    :param lista_bidimensionale: lista bidimensionale che contiene valori 0 e 1
    :returns: lista bidimensionale che contiene oggetti rettangolo
    """  
    schermo = grafica_vuota()
    for riga in range(NUMERO_RIGHE):
        riga_schermo = grafica_vuota()
        for colonna in range(LUNGHEZZA_RIGA):
            if lista_bidimensionale[riga][colonna] == 1:
                quadratino = rettangolo(LATO_QUADRATINO, LATO_QUADRATINO, COLORE_SU_SCHERMO)
            elif lista_bidimensionale[riga][colonna] == 0:
                quadratino = rettangolo(LATO_QUADRATINO, LATO_QUADRATINO, SFONDO_SCHERMO)
            riga_schermo = accanto(riga_schermo, quadratino)
        schermo = sopra(schermo, riga_schermo)
    return schermo

def main_grafica():
    numero = chiedi_numero_coordinate()
    lista_coordinate = crea_lista_coordinate(numero)
    lista_bidimensionale = crea_lista_bidimensionale()
    lista_bidimensionale = modifica_lista_bidimensionale(lista_coordinate, lista_bidimensionale)
    visualizza_grafica(crea_grafica_schermo(lista_bidimensionale))
    
def animazione_salva_gif(coordinate: list[list[int, int]]):
    progress = 1
    listagif = []
    for i in coordinate:
        lista_bidimensionale = crea_lista_bidimensionale()
        print("Starting Build " + str(progress))
        modifica_lista_bidimensionale(i, lista_bidimensionale)
        grafica_schermo = crea_grafica_schermo(lista_bidimensionale)
        listagif.append(grafica_schermo)
        progress += 1
    salva_animazione("gif" + str(progress), listagif, 100)


def passa_coordinate(lista_coordinate: list[list[int, int]]):
    """
    visualizza una grafica, usando una lista di coordinate fornita da un modulo esterno
    """
    lista_bidimensionale = crea_lista_bidimensionale()
    lista_bidimensionale = modifica_lista_bidimensionale(lista_coordinate, lista_bidimensionale)
    visualizza_grafica(crea_grafica_schermo(lista_bidimensionale))

def grafica_due_liste(lista1c, lista2c):
    lista = crea_lista_bidimensionale()
    for i in lista1c:
        lista = modifica_lista_bidimensionale(i, lista)
    for i in lista2c:
        lista = modifica_lista_bidimensionale(i, lista)
    visualizza_grafica(crea_grafica_schermo(lista))

def due_liste_gif(lista1c, lista2c):
    lista = crea_lista_bidimensionale()
    for i in lista1c:
        lista = modifica_lista_bidimensionale(i, lista)
    for i in lista2c:
        lista = modifica_lista_bidimensionale(i, lista)
    visualizza_grafica(crea_grafica_schermo(lista))
