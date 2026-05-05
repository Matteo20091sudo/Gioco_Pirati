from time import sleep
import os
import json
from random import randint

tutto = {
    "monete": 2000,
    "equipaggio": [],
    "scorte di cibo": [],
    "merci": [],
    "settimana": 0
}

settimanePreviste = 8

equipaggioAcquistabile = [
    {"nome": "cuoco", "prezzo": 15, "quantita": 0},
    {"nome": "marinaio", "prezzo": 10, "quantita": 0},
    {"nome": "meccanico", "prezzo": 15, "quantita": 0},
    {"nome": "medico", "prezzo": 25, "quantita": 0},
    {"nome": "navigatore", "prezzo": 20, "quantita": 0}
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
    os.system("cls" if os.name == "nt" else "clear")

def benvenuto():
    pulisci_schermo()
    print("Benvenuto nel gioco del nuovo mondo!!\n"
          "All'interno di questo gioco l'obiettivo è di raggiungere il nuovo mondo\n"
          "alla ricerca di nuove merci non presenti nella tua parte di globo.\n"
          "Disporrai di una nave nuova di zecca e 2000 monete, il gioco si compone di 6 fasi:\n"
          " - fase di acquisto dell'equipaggio\n"
          " - fase di acquisto delle scorte di cibo\n"
          " - fase di acquisto di merci da barattare all’arrivo nel nuovo mondo\n"
          " - viaggio (tempo previsto: 8 settimane)\n"
          " - commercio nel nuovo mondo\n"
          " - rientro nella propria terra con calcolo di guadagni o perdite\n"
          "Durante il tuo viaggio potranno esserci vari imprevisti.\n")
    scelta = input("Sei pronto a iniziare il tuo viaggio? (s/n) ").lower().strip()
    return scelta

def visualizzaEquipaggioAquistabile():
    print("----------- EQUIPAGGIO ACQUISTABILE ----------")
    for i, c in enumerate(equipaggioAcquistabile):
        print(f"{i+1}. {c['nome']}, {c['prezzo']} monete d'oro a settimana")
    print("----------------------------------------------")

def ingaggioEquipaggio():
    pulisci_schermo()
    print("Benvenuto nella prima fase del gioco, l'ingaggio dell'equipaggio!!!\n"
          "In questa fase avrai la possibilità di ingaggiare tutti i membri della tua ciurma.\n"
          "Puoi ingaggiare al massimo 16 persone, e devi averne almeno 1 per ogni ruolo.\n"
          "I soldi verranno sottratti alla fine del viaggio.\n")
    sleep(2)

    totale = 0
    indice = 0

    while indice < len(equipaggioAcquistabile) and totale < 16:

        pulisci_schermo()
        visualizzaEquipaggioAquistabile()

        ruolo = equipaggioAcquistabile[indice]["nome"]
        prezzo = equipaggioAcquistabile[indice]["prezzo"]

        print(f"Categoria attuale: {ruolo} ({prezzo} monete a settimana)")
        print(f"Membri totali attuali: {totale}/16")

        # input quantità valido
        quantita_valida = False
        while not quantita_valida:
            try:
                q = int(input(f"Quanti {ruolo} vuoi ingaggiare? "))

                if q <= 0:
                    print("La quantità non può essere negativa o pari a 0.")
                else:
                    # controllo limite massimo
                    if totale + q > 16:
                        print("Supereresti il limite massimo di 16 membri.")
                        print(f"Puoi aggiungerne al massimo {16 - totale}.")
                    else:
                        quantita_valida = True

            except:
                print("Formato non valido.")

        # aggiorno quantità
        equipaggioAcquistabile[indice]["quantita"] = q
        totale += q

        indice += 1  


    minimo_ok = True
    for e in equipaggioAcquistabile:
        if e["quantita"] == 0:
            minimo_ok = False

    if not minimo_ok:
        print("ERRORE: devi avere almeno 1 persona per ogni ruolo!")
        print("Ricomincia la fase di ingaggio...")
        sleep(3)

        # reset
        for e in equipaggioAcquistabile:
            e["quantita"] = 0

        return ingaggioEquipaggio()

    # CREAZIONE LISTA MEMBRI REALI
    tutto["equipaggio"] = []

    for e in equipaggioAcquistabile:
        ruolo = e["nome"]
        quantita = e["quantita"]

        i = 0
        while i < quantita:
            membro = [ruolo, 100]   # come vuoi tu
            tutto["equipaggio"].append(membro)
            i += 1

    print("\nEquipaggio registrato correttamente!")
    print("Membri totali:", len(tutto["equipaggio"]))
    sleep(2)

        
def calcolaPagaEquipaggio(settimane):
    totale = 0

    # per ogni membro dell'equipaggio
    for membro in tutto["equipaggio"]:
        ruolo = membro[0]  # es: "cuoco"

        # cerco il prezzo settimanale del ruolo
        i = 0
        while i < len(equipaggioAcquistabile):
            if equipaggioAcquistabile[i]["nome"] == ruolo:
                prezzo = equipaggioAcquistabile[i]["prezzo"]
                totale += prezzo * settimane
            i += 1

    tutto["paga_equipaggio"] = totale

def acquistoScorte():
    pulisci_schermo()
    print("FASE DI ACQUISTO DELLE SCORTE DI CIBO")
    print(f"Monete disponibili: {tutto['monete']}")

    tutto["scorte di cibo"] = []

    for scorta in scorteAcquistabili:
        nome = scorta["nome"]
        unita = scorta["unita"]
        prezzo = scorta["prezzo"]

        print(f"Tipo di scorta: {nome} ({unita})")
        print(f"Prezzo per unità: {prezzo} monete")

        corretto = False
        while not corretto:
            try:
                quantita = float(input(f"Inserisci quanta {nome.upper()} vuoi acquistare: "))
                if quantita < 0:
                    print("La quantità non può essere negativa.")
                else:
                    corretto = True
            except:
                print("Formato non valido.")

        costo = quantita * prezzo

        # controllo monete
        if costo > tutto["monete"]:
            print(f"Non hai abbastanza monete! Puoi spendere al massimo {tutto['monete']}.")
            print("Questa scorta verrà impostata a 0.")
            quantita = 0
            costo = 0

        # aggiorno monete
        tutto["monete"] -= costo

        # salvo la scorta acquistata
        tutto["scorte di cibo"].append([nome, quantita])

        print(f"Hai acquistato {quantita} {unita} di {nome} per {costo} monete.")
        print(f"Monete residue: {tutto['monete']}")

    print("ACQUISTO SCORTE TERMINATO")
    print("Scorte finali:")
    for s in tutto["scorte di cibo"]:
        print(f"- {s[0]}: {s[1]}")

    sleep(2)

scelta = benvenuto()

if scelta == "s":
    ingaggioEquipaggio()          
    acquistoScorte()              
    calcolaPagaEquipaggio(settimanePreviste)

elif scelta == "n":
    print("Hai scelto di non iniziare il viaggio.")

else:
    print("Scelta non valida.")
