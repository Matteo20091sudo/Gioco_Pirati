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
<<<<<<< HEAD
    os.system("cls" if os.name == "nt" else "clear")

=======
    os.system("cls")
 
>>>>>>> 02edb589ad2208ad39efe1afd78e1583f4a43cf9
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
<<<<<<< HEAD
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

=======
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
 
 
>>>>>>> 02edb589ad2208ad39efe1afd78e1583f4a43cf9
scelta = benvenuto()

if scelta == "s":
<<<<<<< HEAD
    ingaggioEquipaggio()          
    acquistoScorte()              
    calcolaPagaEquipaggio(settimanePreviste)

elif scelta == "n":
    print("Hai scelto di non iniziare il viaggio.")

=======
    sceltaEquipaggio(membri)
    print(equipaggioAcquistato)
 
 
   
elif scelta == "n":
    print("peccato, magari la prossima volta")
>>>>>>> 02edb589ad2208ad39efe1afd78e1583f4a43cf9
else:
    print("Scelta non valida.")
