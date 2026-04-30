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
 
membri = 0
settimanePreviste = 8
 
equipaggioAcquistato = {
    "cuoco":0,
    "marinaio":0,
    "meccanico":0,
    "medico":0,
    "navigatore":0
 
}
 
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
        print(f"{i+1}. {c['nome']}, {c['prezzo']} monete d'oro a settimana")
    print("-------------------------------------------")
 
def ingaggioEquipaggio():
    pulisci_schermo()
    print("Benvenuto nella prima fase del gioco, l'ingaggio dell'equipaggio!!!\n" \
    "in questa fase avrai la possibilità di ingaggiare tutti i membri della tua ciurma\n" \
    "puoi ingaggiare al massimo 16 persone, per salpare e iniziare il viaggio hai bisogno\n" \
    "di una persona per ogni tipologia (quindi minimo 5 persone).\n" \
    "devi avere almeno 1 personaggio di ogni tipo prima di andare avanti.\n" \
    "i soldi verranno sottratti alla fine del viaggio (quindi occhio a quanto spendi)\n" \
    "i soldi verranno spesi anche in caso di morte di un membro poichè ancdranno donati agli orfani\n" \
    "e associazioni varie. ")
 
def ha_tutti_i_ruoli():
    return all(count > 0 for count in equipaggioAcquistato.values())
 
def sceltaEquipaggio(membri):
    ingaggioEquipaggio()
    fine = False
    visualizzaEquipaggioAquistabile()
    while membri < 16 and not fine:
        try:
            scelta = int(input("Scegli il numero del membro dell'equipaggio che vuoi ingaggiare (0 per terminare) "))
            if scelta == 0:
                if ha_tutti_i_ruoli():
                    fine = True
                else:
                    print("Devi avere almeno 1 personaggio per ogni ruolo prima di andare avanti.")
            elif scelta == 1:
                membri += 1
                equipaggioAcquistato["cuoco"] += 1
            elif scelta == 2:
                membri += 1
                equipaggioAcquistato["marinaio"] += 1
            elif scelta == 3:
                membri += 1
                equipaggioAcquistato["meccanico"] += 1
            elif scelta == 4:
                membri += 1
                equipaggioAcquistato["medico"] += 1
            elif scelta == 5:
                membri += 1
                equipaggioAcquistato["navigatore"] += 1
            else:
                print("Numero sbagliato oppure non hai inserito una classe valida.")
        except ValueError:
            print("Formato sbagliato! Inserisci un numero.")
    if not ha_tutti_i_ruoli():
        print("Non hai completato l'equipaggio minimo. Riprova.")
    return membri
 
 
scelta = benvenuto()
if scelta == "s":
    sceltaEquipaggio(membri)
    print(equipaggioAcquistato)
 
 
   
elif scelta == "n":
    print("peccato, magari la prossima volta")
else:
    print("scelta non valida")