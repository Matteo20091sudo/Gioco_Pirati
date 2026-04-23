from time import sleep
import os
import json
from random import randint

tutto = {
    "monete" : 2000,
    "equipaggio":[],
    "scorte di cibo":[],
    "merci":[],
    "settimana":0
}

settimanePreviste = 8

equipaggioAcquistabile = [
    {"nome": "cuoco", "prezzo": 15},
    {"nome": "marinaio", "prezzo": 10},
    {"nome": "meccanico", "prezzo": 15},
    {"nome": "medico", "prezzo": 25},
    {"nome": "navigatore", "prezzo": 20}
]

scorteAcquistabili = [
    {"nome": "verdura", "unita": "kg", "prezzo": 0.5},
    {"nome": "frutta", "unita": "kg", "prezzo": 1},
    {"nome": "carne", "unita": "kg", "prezzo": 2},
    {"nome": "acqua", "unita": "barili", "prezzo": 0.5}
]

merciAcquistabili = [
    {"nome": "bottiglie di medicinale", "prezzo": 1},
    {"nome": "armi", "prezzo": 5},
    {"nome": "sale", "prezzo": 0.5},
    {"nome": "stuoia", "prezzo": 2},
    {"nome": "coltelli", "prezzo": 0.5},
    {"nome": "diamanti", "prezzo": 1}
]

def pulisci_schermo():
    os.system("cls")

def benvenuto():
    pulisci_schermo()
    print("Benvenuto nel gioco del nuovo mondo!!\n" \
    "All'interno di questo gioco l'obiettivo è di raggiungere il nuovo mondo\n" \
    "alla ricerca di nuove merci non presenti nella tua parte di globo.\n" \
    "Disporrai di una nave nuova di zecca e 2000 monete, il gioco si compone di 6 fasi:\n" \
    " - fase di acquisto dell'equipaggio\n" \
    " - fase di acquisto delle scorte di cibo\n" \
    " - fase di acquisto di merci da barattare all’arrivo nel nuovo mondo con le persone del posto\n" \
    " - viaggio (tempo previsto: 8 settimane)\n" \
    " - commercio nel nuovo mondo\n" \
    " - rientro nella propria terra con calcolo di guadagni o perdite\n" \
    "durante il tuo viaggio potranno esserci vari imprevisti\n")
    scelta = input("Sei pronto a iniziare il tuo viaggio? (s/n) ").lower().strip()
    return scelta

def visualizzaEquipaggioAquistabile():
    print("-----------EQUIPAGGIO-AQUISTABILE----------")
    for i,c in enumerate(equipaggioAcquistabile):
        print(f"{i+1}. {c["nome"]}, {c["prezzo"]} monete d'oro a settimana")
    print("-------------------------------------------")

def ingaggioEquipaggio():
    pulisci_schermo()
    print("Benvenuto nella prima fase del gioco, l'ingaggio dell'equipaggio!!!\n" \
    "in questa fase avrai la possibilità di ingaggiare tutti i membri della tua ciurma\n" \
    "puoi ingaggiare al massimo 16 persone, per salpare e iniziare il viaggio hai bisogno\n" \
    "di una persona per ogni tipologia (quindi minimo 5 persone).\n" \
    "i soldi verranno sottratti alla fine del viaggio (quindi occhio a quanto spendi)\n" \
    "i soldi verranno spesi anche in caso di morte di un membro poichè ancdranno donati agli orfani\n" \
    "e associazioni varie. ")

visualizzaEquipaggioAquistabile()
sleep(5)
scelta = benvenuto()
if scelta == "s":
    pass
elif scelta == "n":
    None
else:
    print("scelta non valida")