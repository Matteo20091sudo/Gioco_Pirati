import random
import os
import json
from time import sleep

tutto = {
    "monete": 2000,

    "equipaggio": [],
    "equipaggioIngaggiato": [],
    "costoEquipaggio": 0,

    "scorte": {
        "verdura": {"quantita": 0, "unita": "kg"},
        "frutta":  {"quantita": 0, "unita": "kg"},
        "carne":   {"quantita": 0, "unita": "kg"},
        "acqua":   {"quantita": 0, "unita": "barili"}
    },

    "merci": {
        "medicinali": {"quantita": 0},
        "armi":       {"quantita": 0},
        "sale":       {"quantita": 0},
        "stoffa":     {"quantita": 0},
        "coltelli":   {"quantita": 0},
        "diamanti":   {"quantita": 0}
    },

    "merciNuovoMondo": {"perle": 0, "manufatti": 0, "spezie": 0},

    "settimana": 1,
    "setViaggio": 8,

    "avvistamentiAlbatro": 0,
    "sfortuna": 0,

    "gameover": False,

    "MoltVerdure": 1,
    "MoltFrutta":  1,
    "MoltCarne":   1,
    "MoltAcqua":   1,

    "deltaMorale": 0
}

SALVATAGGIO_FILE = ".\dati_partita.txt"

# Salva e Carica

def carica():
    try:
        with open(SALVATAGGIO_FILE, "r", encoding="utf-8") as f:
            s = f.read()
            if s.strip():
                return json.loads(s)
            else:
                return tutto
    except:
        return tutto
def salva():
    with open(SALVATAGGIO_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(tutto))


def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')


def Decisione(stringa):
    while True:
        d = input(stringa).replace(" ", "").lower()
        if d == "si":
            return True
        if d == "no":
            return False


def UomoBordo(ruolo):
    for membro in tutto["equipaggio"]:
        if membro["ruolo"].lower() == ruolo.lower():
            return True
    return False


def rimuovi_membro_random():
    if len(tutto["equipaggio"]) > 0:
        i = random.randint(0, len(tutto["equipaggio"]) - 1)
        perso = tutto["equipaggio"][i]
        tutto["equipaggio"].pop(i)
        return perso
    return None


def aggiungi_membro(ruolo, morale):
    tutto["equipaggio"].append({"ruolo": ruolo, "morale": morale})


def get_scorta(nome):
    return tutto["scorte"][nome]["quantita"]


def set_scorta(nome, valore):
    tutto["scorte"][nome]["quantita"] = max(0, valore)


def get_merce(nome):
    return tutto["merci"][nome]["quantita"]


def set_merce(nome, valore):
    tutto["merci"][nome]["quantita"] = max(0, valore)


# Fase iniziale 

def benvenuto():
    pulisci_schermo()
    print("=== BENVENUTO NEL GIOCO DEL VIAGGIO NEL NUOVO MONDO ===\n")
    print("1) Nuova partita")
    print("2) Carica partita salvata")
    print("3) Esci")
    while True:
        scelta = input("\nScelta: ").strip()
        if scelta == "1":
            return "nuova"
        elif scelta == "2":
            return "carica"
        elif scelta == "3":
            return "esci"
        else:
            print("Inserisci 1, 2 o 3.")


def ingaggioEquipaggio():
    pulisci_schermo()
    print("=== FASE DI INGAGGIO DELLA CIURMA ===")
    print("Devi ingaggiare almeno 1 persona per ogni ruolo (minimo 5, massimo 16 totali).")
    print("Le monete verranno pagate a fine viaggio (anche ai defunti).\n")

    ruoli = [
        {"ruolo": "marinaio",   "costo": 10},
        {"ruolo": "cuoco",      "costo": 15},
        {"ruolo": "meccanico",  "costo": 15},
        {"ruolo": "navigatore", "costo": 20},
        {"ruolo": "medico",     "costo": 25}
    ]

    valido = False
    while not valido:
        tutto["equipaggio"] = []
        tutto["equipaggioIngaggiato"] = []

        for r in ruoli:
            ingaggiato = False
            while not ingaggiato:
                try:
                    q = int(input(f"Quanti {r['ruolo']} vuoi ingaggiare? (min 1, costo {r['costo']} monete/sett): "))
                    if q < 1:
                        print("Devi ingaggiare almeno 1 persona per questo ruolo.")
                    else:
                        ingaggiato = True
                except ValueError:
                    print("Inserisci un numero valido.")

            for _ in range(q):
                membro = {"ruolo": r["ruolo"], "morale": 100}
                tutto["equipaggio"].append(membro)
                tutto["equipaggioIngaggiato"].append({"ruolo": r["ruolo"]})

        totale = len(tutto["equipaggio"])
        if totale > 16:
            print(f"\nHai ingaggiato {totale} persone ma il massimo e' 16. Ricomincia.\n")
        else:
            valido = True

    print(f"\nEquipaggio ingaggiato: {len(tutto['equipaggio'])} persone.")
    sleep(1.5)


def acquistoScorte():
    pulisci_schermo()
    print("=== FASE DI ACQUISTO DELLE SCORTE DI CIBO ===\n")
    print("Ogni membro consuma a settimana: 0.5 kg verdura, 1 kg frutta, 1 kg carne, 0.5 barili acqua.")
    print(f"Monete disponibili: {tutto['monete']}\n")

    scorteAcquistabili = [
        {"nome": "verdura", "prezzo": 0.5, "unita": "kg"},
        {"nome": "frutta",  "prezzo": 1.0, "unita": "kg"},
        {"nome": "carne",   "prezzo": 2.0, "unita": "kg"},
        {"nome": "acqua",   "prezzo": 0.5, "unita": "barili"}
    ]

    for s in scorteAcquistabili:
        valido = False
        while not valido:
            try:
                q = float(input(f"Quanta {s['nome']} vuoi acquistare ({s['unita']})? Prezzo {s['prezzo']} monete/{s['unita']}: "))
                if q < 0:
                    print("La quantita' non puo' essere negativa.")
                else:
                    valido = True
            except ValueError:
                print("Inserisci un numero valido.")

        costo = q * s["prezzo"]
        if costo > tutto["monete"]:
            print("Non hai abbastanza monete. Acquisto annullato.")
            q = 0
            costo = 0

        tutto["monete"] -= costo
        set_scorta(s["nome"], get_scorta(s["nome"]) + q)

    print(f"\nAcquisto scorte completato. Monete rimaste: {tutto['monete']:.1f}")
    sleep(1.5)


def acquistoMerci():
    pulisci_schermo()
    print("=== FASE DI ACQUISTO DELLE MERCI DA BARATTARE ===\n")
    print("Nel nuovo mondo potrai barattare sale, stoffa, coltelli e diamanti.")
    print(f"Monete disponibili: {tutto['monete']}\n")

    merciAcquistabili = [
        {"nome": "medicinali", "prezzo": 1.0, "unita": "bottiglie"},
        {"nome": "armi",       "prezzo": 5.0, "unita": "armi"},
        {"nome": "sale",       "prezzo": 0.5, "unita": "sacchi"},
        {"nome": "stoffa",     "prezzo": 2.0, "unita": "teli"},
        {"nome": "coltelli",   "prezzo": 0.5, "unita": "pezzi"},
        {"nome": "diamanti",   "prezzo": 1.0, "unita": "pezzi"}
    ]

    for m in merciAcquistabili:
        valido = False
        while not valido:
            try:
                q = float(input(f"Quanti {m['nome']} vuoi acquistare ({m['unita']})? Prezzo {m['prezzo']} monete: "))
                if q < 0:
                    print("La quantita' non puo' essere negativa.")
                else:
                    valido = True
            except ValueError:
                print("Inserisci un numero valido.")

        costo = q * m["prezzo"]
        if costo > tutto["monete"]:
            print("Non hai abbastanza monete. Acquisto annullato.")
            q = 0
            costo = 0

        tutto["monete"] -= costo
        set_merce(m["nome"], get_merce(m["nome"]) + q)

    print(f"\nAcquisto merci completato. Monete rimaste: {tutto['monete']:.1f}")
    sleep(1.5)


# Step 1

eventi = [
    "Nessun imprevisto",
    "Avvistamento albatro",
    "Avvistamento albatro",
    "Avvistamento albatro",
    "Uomo in mare",
    "Verdura in mare",
    "Frutta in mare",
    "Carne in mare",
    "Acqua in mare",
    "Pesca miracolosa",
    "Tempesta miracolosa",
    "Venti favorevoli",
    "Cattivo tempo",
    "Ondata",
    "Infestazione ratti",
    "Avvistamento scialuppa",
    "Epidemia",
    "Attacco pirata",
    "Danni al timone",
    "Raffiche di vento",
    "Avvistamento isola"
]


def Step1():
    print(f"\n=== SETTIMANA {tutto['settimana']} di {tutto['setViaggio']} ===")

    indice = random.randint(0, len(eventi) - 1)
    nome = eventi[indice]
    print(f"Evento della settimana: {nome}\n")

    if nome == "Uomo in mare":
        UomoInMare()
    elif nome == "Verdura in mare":
        ScortaInMare("verdura", "kg")
    elif nome == "Frutta in mare":
        ScortaInMare("frutta", "kg")
    elif nome == "Carne in mare":
        ScortaInMare("carne", "kg")
    elif nome == "Acqua in mare":
        ScortaInMare("acqua", "barili")
    elif nome == "Pesca miracolosa":
        PescaMiracolosa()
    elif nome == "Tempesta miracolosa":
        TempestaMiracolosa()
    elif nome == "Venti favorevoli":
        VentiFavorevoli()
    elif nome == "Cattivo tempo":
        MerceInMare("medicinali", "bottiglie")
    elif nome == "Ondata":
        MerceInMare("armi", "armi")
    elif nome == "Infestazione ratti":
        MerceInMare("stoffa", "teli")
    elif nome == "Avvistamento albatro":
        tutto["avvistamentiAlbatro"] += 1
        AvvistamentoAlbatro()
    elif nome == "Avvistamento scialuppa":
        AvvistamentoScialuppa()
    elif nome == "Epidemia":
        Epidemia()
    elif nome == "Attacco pirata":
        AttaccoPirata()
    elif nome == "Danni al timone":
        DanniAlTimone()
    elif nome == "Raffiche di vento":
        RafficheDiVento()
    elif nome == "Avvistamento isola":
        AvvistamentoIsola()
    elif nome == "Nessun imprevisto":
        print("Questa settimana non e' successo nulla.")

    if nome != "Nessun imprevisto":
        eventi.pop(indice)


def UomoInMare():
    perso = rimuovi_membro_random()
    if perso:
        print(f"Un {perso['ruolo']} e' caduto in mare e muore!")
        if len(tutto["equipaggio"]) == 0:
            print("Non hai piu' nessuno a bordo!")
            tutto["gameover"] = True
    else:
        print("Non ci sono membri da perdere.")


def ScortaInMare(nome, unita):
    q = get_scorta(nome)
    perc = random.choice([0.5, 1/3, 0.25, 0.2])
    if q > 0:
        persa = q * perc
        set_scorta(nome, q - persa)
        print(f"E' caduto in mare il {perc*100:.0f}% di {nome} ({persa:.1f} {unita}).")
    else:
        print(f"Tempesta in mare, fortunatamente non avevi {nome}.")
    print(f"{nome.capitalize()} rimasta/o: {get_scorta(nome):.1f} {unita}")


def MerceInMare(nome, unita):
    q = get_merce(nome)
    perc = random.choice([0.5, 1/3, 0.25, 0.2])
    if q > 0:
        persa = q * perc
        set_merce(nome, q - persa)
        print(f"Perso il {perc*100:.0f}% di {nome} ({persa:.1f} {unita}).")
    else:
        print(f"Evento senza danno: non avevi {nome}.")
    print(f"{nome.capitalize()} rimasto/a: {get_merce(nome):.1f}")


def PescaMiracolosa():
    aggiunta = random.randint(11, 20)
    set_scorta("carne", get_scorta("carne") + aggiunta)
    print(f"Settimana tranquilla: l'equipaggio pesca! Aggiunti {aggiunta} kg di carne.")


def TempestaMiracolosa():
    aggiunta = random.randint(11, 20)
    set_scorta("acqua", get_scorta("acqua") + aggiunta)
    print(f"Durante la tempesta raccogli acqua nei barili. Aggiunti {aggiunta} barili.")


def VentiFavorevoli():
    aumento = random.randint(5, 15)
    tutto["setViaggio"] -= 1
    tutto["deltaMorale"] += aumento
    print(f"Venti favorevoli! Il viaggio si accorcia di 1 settimana.")
    print(f"Il morale aumenta di {aumento} punti permanenti.")


def AvvistamentoAlbatro():
    print("Hai avvistato un albatro! Segno di buon presagio tra i marinai.")
    tentativi = min(int(get_merce("armi")), len(tutto["equipaggio"]))

    if tentativi <= 0:
        print("Non hai armi per tentare di colpirlo. L'albatro se ne va.")
        return

    print(f"Puoi tentare di abbatterlo (hai {tentativi} tentativo/i).")

    while tentativi > 0:
        if Decisione(f"Vuoi provare a colpirlo? Tentativi rimasti {tentativi} (si/no): "):
            tentativi -= 1
            set_merce("armi", get_merce("armi") - 1)
            if random.randint(1, 2) == 1:
                aggiunta = random.randint(10, 15)
                set_scorta("carne", get_scorta("carne") + aggiunta)
                tutto["sfortuna"] += 1
                print(f"Hai ucciso l'albatro. Aggiunti {aggiunta} kg di carne.")
                return
            else:
                print("Hai mancato il colpo.")
        else:
            print("Hai deciso di lasciarlo stare.")
            return


def AvvistamentoScialuppa():
    print("Una scialuppa con 4 uomini e una cassa si avvicina.")
    if Decisione("Vuoi accoglierli? (si/no): "):
        for _ in range(4):
            ruolo = random.choice(["marinaio", "cuoco", "meccanico", "medico", "navigatore"])
            morale = random.randint(25, 75)
            aggiungi_membro(ruolo, morale)
            print(f"Aggiunto un {ruolo} con morale {morale}.")

        for nome_merce in ["medicinali", "armi", "sale", "stoffa", "coltelli", "diamanti"]:
            bonus = random.randint(10, 20)
            set_merce(nome_merce, get_merce(nome_merce) + bonus)
            print(f"Dalla cassa: +{bonus} {nome_merce}.")
    else:
        print("Hai rifiutato. La scialuppa si allontana.")


def Epidemia():
    print("Un'epidemia si abbatte sull'equipaggio!")
    malati_indici = []

    for i, membro in enumerate(tutto["equipaggio"]):
        if membro["ruolo"] != "medico":
            if random.randint(1, 100) <= 70:
                malati_indici.append(i)

    curati = 0
    morti_indici = []

    if UomoBordo("medico"):
        for i in malati_indici:
            if get_merce("medicinali") > 0:
                set_merce("medicinali", get_merce("medicinali") - 1)
                curati += 1
            else:
                morti_indici.append(i)
    else:
        morti_indici = list(malati_indici)

    for i in sorted(morti_indici, reverse=True):
        tutto["equipaggio"].pop(i)

    morti = len(morti_indici)
    print(f"Malati: {len(malati_indici)}, Curati: {curati}, Morti: {morti}")
    print(f"Medicinali rimasti: {get_merce('medicinali'):.0f}")

    if len(tutto["equipaggio"]) == 0:
        print("Tutti i membri sono morti!")
        tutto["gameover"] = True


def AttaccoPirata():
    pirati = random.randint(3, 10)
    print(f"Una nave pirata con {pirati} uomini ti attacca!")

    if get_merce("armi") <= 0:
        print("Non hai armi. Non puoi difenderti.")
        perdite = min(pirati, len(tutto["equipaggio"]))
        for _ in range(perdite):
            perso = rimuovi_membro_random()
            if perso:
                print(f"Hai perso un {perso['ruolo']}.")
        if len(tutto["equipaggio"]) == 0:
            tutto["gameover"] = True
        return

    if Decisione("Vuoi difenderti? (si/no): "):
        difensori = min(int(get_merce("armi")), len(tutto["equipaggio"]))
        perdite = min(pirati - difensori, len(tutto["equipaggio"]))
        armi_usate = min(pirati, int(get_merce("armi")))
        set_merce("armi", get_merce("armi") - armi_usate)

        if perdite <= 0:
            print("Hai respinto i pirati senza perdite!")
        else:
            print(f"I pirati hanno avuto la meglio. Perdi {perdite} uomini.")
            for _ in range(perdite):
                perso = rimuovi_membro_random()
                if perso:
                    print(f"Hai perso un {perso['ruolo']}.")
            if len(tutto["equipaggio"]) == 0:
                tutto["gameover"] = True
    else:
        print("Hai deciso di non difenderti. I pirati saccheggiano e se ne vanno.")


def DanniAlTimone():
    print("Uno scoglio danneggia il timone!")
    if UomoBordo("meccanico"):
        tutto["setViaggio"] += 1
        print("Il meccanico ripara il danno. Il viaggio si allunga di 1 settimana.")
    else:
        allungo = random.randint(2, 4)
        tutto["setViaggio"] += allungo
        print(f"Senza meccanico il viaggio si allunga di {allungo} settimane.")


def RafficheDiVento():
    print("Raffiche di vento ti allontanano dalla rotta!")
    if UomoBordo("navigatore"):
        tutto["setViaggio"] += 1
        print("Il navigatore corregge la rotta. Il viaggio si allunga di 1 settimana.")
    else:
        allungo = random.randint(2, 4)
        tutto["setViaggio"] += allungo
        print(f"Senza navigatore il viaggio si allunga di {allungo} settimane.")


def AvvistamentoIsola():
    print("Hai avvistato un'isola!")
    if not Decisione("Vuoi approdare per un'ispezione? (si/no): "):
        print("Hai deciso di non fermarti.")
        return

    allungo = random.randint(1, 2)
    tutto["setViaggio"] += allungo
    print(f"L'ispezione allunga il viaggio di {allungo} settimana/e.")

    if random.randint(1, 2) == 1:
        print("L'isola e' disabitata. Non succede nulla di particolare.")
    else:
        if random.randint(1, 2) == 1:
            print("Gli abitanti sono ostili e vi mettono in fuga. Nessuna perdita pero'.")
        else:
            print("Gli abitanti sono amichevoli e vi donano merci!")
            if tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] == 0:
                bonus = (20, 40)
            else:
                bonus = (5, 20)
            for nome_merce in ["medicinali", "armi", "sale", "stoffa", "coltelli", "diamanti"]:
                q = random.randint(*bonus)
                set_merce(nome_merce, get_merce(nome_merce) + q)
                print(f"+{q} {nome_merce}")

#  Step 2

def QuantitaScorte(scorta_nome, molt_corrente, consumo_base, nome_print, unita):
    equip = len(tutto["equipaggio"])
    setRimaste = tutto["setViaggio"] - tutto["settimana"]
    variazione_delta = 0

    q = get_scorta(scorta_nome)

    if q <= 0:
        print(f"Le scorte di {nome_print} sono ESAURITE! Il morale cala di 10 punti a settimana.")
        variazione_delta -= 10
        return molt_corrente, variazione_delta

    necessaria_totale = consumo_base * equip * molt_corrente * setRimaste
    print(f"{nome_print.capitalize()}: rimasti {q:.1f} {unita}, necessari {necessaria_totale:.1f} per le {setRimaste} sett. restanti.")

    if setRimaste <= 0:
        return molt_corrente, variazione_delta

    if q >= 2 * necessaria_totale:
        if Decisione(f"Hai il doppio delle scorte di {nome_print}. Vuoi raddoppiare le razioni? (+5 morale/sett) (si/no): "):
            molt_corrente *= 2
            variazione_delta += 5
            print(f"Razioni di {nome_print} raddoppiate.")
    elif q < necessaria_totale:
        if Decisione(f"Le scorte di {nome_print} non bastano. Vuoi dimezzare le razioni? (-5 morale/sett) (si/no): "):
            molt_corrente *= 0.5
            variazione_delta -= 5
            print(f"Razioni di {nome_print} dimezzate.")

    return molt_corrente, variazione_delta


def step2():
    equip = len(tutto["equipaggio"])

    consumi = {"verdura": 0.5, "frutta": 1.0, "carne": 1.0, "acqua": 0.5}

    set_scorta("verdura", get_scorta("verdura") - consumi["verdura"] * equip * tutto["MoltVerdure"])
    set_scorta("frutta",  get_scorta("frutta")  - consumi["frutta"]  * equip * tutto["MoltFrutta"])
    set_scorta("carne",   get_scorta("carne")   - consumi["carne"]   * equip * tutto["MoltCarne"])
    set_scorta("acqua",   get_scorta("acqua")   - consumi["acqua"]   * equip * tutto["MoltAcqua"])

    tutto["MoltVerdure"], dv = QuantitaScorte("verdura", tutto["MoltVerdure"], consumi["verdura"], "verdura", "kg")
    tutto["MoltFrutta"],  df = QuantitaScorte("frutta",  tutto["MoltFrutta"],  consumi["frutta"],  "frutta",  "kg")
    tutto["MoltCarne"],   dc = QuantitaScorte("carne",   tutto["MoltCarne"],   consumi["carne"],   "carne",   "kg")
    tutto["MoltAcqua"],   da = QuantitaScorte("acqua",   tutto["MoltAcqua"],   consumi["acqua"],   "acqua",   "barili")

    tutto["deltaMorale"] += dv + df + dc + da

    print(f"\nDelta morale corrente: {tutto['deltaMorale']:+.0f} punti per membro.")
    for i in range(len(tutto["equipaggio"]) - 1, -1, -1):
        tutto["equipaggio"][i]["morale"] += tutto["deltaMorale"]
        if tutto["equipaggio"][i]["morale"] <= 0:
            morto = tutto["equipaggio"][i]
            tutto["equipaggio"].pop(i)
            print(f"Un {morto['ruolo']} muore per morale a zero!")

    if len(tutto["equipaggio"]) == 0:
        print("Non hai piu' equipaggio!")
        tutto["gameover"] = True


#  Step 4 

def step4():
    print("\n=== RIEPILOGO FINE SETTIMANA ===")
    print(f"Equipaggio residuo: {len(tutto['equipaggio'])} persone")
    for m in tutto["equipaggio"]:
        print(f"  - {m['ruolo']} | Morale: {m['morale']:.0f}")

    print("\nScorte:")
    print(f"  Verdura:  {get_scorta('verdura'):.1f} kg")
    print(f"  Frutta:   {get_scorta('frutta'):.1f} kg")
    print(f"  Carne:    {get_scorta('carne'):.1f} kg")
    print(f"  Acqua:    {get_scorta('acqua'):.1f} barili")

    print("\nMerci:")
    for nome in tutto["merci"]:
        print(f"  {nome.capitalize()}: {get_merce(nome):.0f}")


# Step 5 

def Step5():
    punteggio = 0
    cause = []

    if (tutto["MoltVerdure"] < 1 or tutto["MoltFrutta"] < 1 or
            tutto["MoltCarne"] < 1 or tutto["MoltAcqua"] < 1):
        punteggio += 30
        cause.append("Razioni cibo ridotte (+30)")

    if not UomoBordo("cuoco"):
        punteggio += 30
        cause.append("Nessun cuoco a bordo (+30)")

    if tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] > 0:
        punteggio += 30
        cause.append("Presagio di sfiga: albatro ucciso (+30)")
    elif tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] == 0:
        punteggio -= 20
        cause.append("Ottimismo: albatro avvistato e non ucciso (-20)")

    if len(tutto["equipaggio"]) > 12:
        punteggio += 30
        cause.append("Nave troppo affollata (+30)")

    diff = tutto["setViaggio"] - 8
    if diff > 0:
        punteggio += diff * 10
        cause.append(f"Viaggio troppo lungo: +{diff} sett. (+{diff*10})")
    elif diff < 0:
        punteggio += diff * 10
        cause.append(f"Viaggio accorciato: {diff} sett. ({diff*10})")

    if punteggio > 100:
        print("\n!!! AMMUTINAMENTO !!! La ciurma ti ha abbandonato.")
        for c in cause:
            print(f"  - {c}")
        tutto["gameover"] = True
    elif 1 <= punteggio <= 100:
        print(f"\nATTENZIONE: rischi l'ammutinamento! Punteggio: {punteggio}/100")
        for c in cause:
            print(f"  - {c}")


# Step 6 

def Step6():
    vivi = len(tutto["equipaggio"])
    if vivi == 0:
        return
    morale_basso = sum(1 for m in tutto["equipaggio"] if m["morale"] <= 30)
    if morale_basso > vivi / 2:
        tutto["setViaggio"] += 1
        print("L'equipaggio e' demoralizzato: il viaggio si allunga di 1 settimana.")


# Fase nuovo mondo

def arrivoNuovoMondo():
    print("\n=== ARRIVO NEL NUOVO MONDO ===")
    print("La nave si avvicina alla costa. Indigeni armati vi osservano.")

    if get_merce("armi") > 0:
        if Decisione("L'equipaggio chiede se vuoi aprire il fuoco sugli indigeni. Vuoi sparare? (si/no): "):
            print("Hai aperto il fuoco. Gli indigeni reagiscono con furia. La spedizione finisce tragicamente.")
            tutto["gameover"] = True
            return

    print("Sbarcate nel nuovo mondo. Gli indigeni vi accolgono con entusiasmo!")
    sleep(1.5)


def calcolaOfferte(nomeMerce, quantita):
    tassi = {
        "sale":     {"perle": 0.5, "manufatti": 0.5, "spezie": 1},
        "stoffa":   {"perle": 5,   "manufatti": 7,   "spezie": 3},
        "coltelli": {"perle": 1,   "manufatti": 3,   "spezie": 6},
        "diamanti": {"perle": 2,   "manufatti": 4,   "spezie": 4},
    }
    valori = {"perle": 2, "manufatti": 2, "spezie": 1}

    offerte = []
    for tipo in ["perle", "manufatti", "spezie"]:
        tasso = tassi[nomeMerce][tipo]
        qtaOttenuta = int(quantita / tasso)
        profitto = qtaOttenuta * valori[tipo]
        offerte.append({"tipo": tipo, "quantita": qtaOttenuta, "profittoStimato": profitto})
    return offerte


def barattaSingolaM(nomeMerce):
    quantita = get_merce(nomeMerce)
    if quantita <= 0:
        print(f"Non hai {nomeMerce}, si passa oltre.")
        return

    print(f"\n--- Baratto: {nomeMerce} (hai {quantita:.0f} unita') ---")
    offerte = calcolaOfferte(nomeMerce, quantita)

    for i, o in enumerate(offerte):
        print(f"  {i+1}) {o['quantita']} {o['tipo']} (profitto stimato: {o['profittoStimato']} monete)")

    sceltaValida = False
    while not sceltaValida:
        try:
            s = int(input("Scegli un'opzione (1/2/3): "))
            if s in [1, 2, 3]:
                sceltaValida = True
            else:
                print("Inserisci 1, 2 o 3.")
        except ValueError:
            print("Inserisci un numero valido.")

    scelta = offerte[s - 1]
    set_merce(nomeMerce, 0)
    tutto["merciNuovoMondo"][scelta["tipo"]] = (
        tutto["merciNuovoMondo"].get(scelta["tipo"], 0) + scelta["quantita"]
    )
    print(f"Hai ottenuto {scelta['quantita']} {scelta['tipo']}!")


def baratto():
    print("\n=== FASE DI BARATTO ===")
    print("Il capo tribu' non vuole armi ne' medicinali.")
    print("Si barattano: sale, stoffa, coltelli, diamanti.\n")

    for nomeMerce in ["sale", "stoffa", "coltelli", "diamanti"]:
        barattaSingolaM(nomeMerce)

    sleep(1.5)


def ilTradimento():
    armiResidue = get_merce("armi")
    if armiResidue <= 0:
        return

    print("\n=== IL TRADIMENTO ===")
    perleOfferte = 30 * int(armiResidue)
    print(f"Un rivale del capo tribu' ti offre {perleOfferte} perle per tutte le tue armi.")
    print("Le sue intenzioni non sembrano buone...")

    if Decisione("Accetti l'offerta? (si/no): "):
        tutto["merciNuovoMondo"]["perle"] = tutto["merciNuovoMondo"].get("perle", 0) + perleOfferte
        set_merce("armi", 0)
        print(f"Hai accettato. Carichi {perleOfferte} perle sulla nave.")

        if tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] > 0:
            print("Il capo tribu' scopre il tradimento! L'intero equipaggio viene ucciso.")
            tutto["gameover"] = True
        elif tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] == 0:
            print("La buona sorte dell'albatro ti protegge. Non vieni scoperto!")
        else:
            if random.randint(1, 2) == 1:
                print("Il capo tribu' scopre il tradimento! L'intero equipaggio viene ucciso.")
                tutto["gameover"] = True
            else:
                print("Per fortuna non vieni scoperto. Il viaggio continua.")
    else:
        if tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] > 0:
            perleBonus = random.randint(5, 20)
        else:
            perleBonus = random.randint(30, 50)
        tutto["merciNuovoMondo"]["perle"] = tutto["merciNuovoMondo"].get("perle", 0) + perleBonus
        print(f"Il capo tribu' ti ringrazia per la lealta' e ti dona {perleBonus} perle.")


def calcolaSettimaneTornoRitorno():
    settimane = 1 if UomoBordo("navigatore") else 2
    if tutto["avvistamentiAlbatro"] >= 1 and tutto["sfortuna"] > 0:
        settimane += 1
    return settimane


def epilogo():
    print("\n=== EPILOGO - VIAGGIO DI RITORNO ===")
    print("Il capo tribu' vi rifornisce di scorte per 3 settimane di viaggio.")
    settimaneRitorno = calcolaSettimaneTornoRitorno()
    tutto["setViaggio"] += settimaneRitorno
    print(f"Il viaggio di ritorno durera' {settimaneRitorno} settimana/e.")


def calcolaPagaEquipaggio():
    costiSettimanali = {
        "marinaio":   10,
        "cuoco":      15,
        "meccanico":  15,
        "medico":     25,
        "navigatore": 20
    }
    totale = 0
    for membro in tutto["equipaggioIngaggiato"]:
        ruolo = membro["ruolo"]
        totale += costiSettimanali.get(ruolo, 0) * tutto["setViaggio"]
    return totale


def asta(moneteDisponibili):
    print("\nLa nave viene messa all'asta per coprire le spese.")

    offertePossibili = [50, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 1200]
    sempriRiproponibili = {50, 300, 400, 450}
    offerteUsate = {}

    while True:
        random.shuffle(offertePossibili)
        for importo in list(offertePossibili):
            volteVisto = offerteUsate.get(importo, 0)
            if volteVisto < 2 or importo in sempriRiproponibili:
                print(f"Offerta: {importo} monete.")
                if Decisione("Accetti questa offerta? (si/no): "):
                    moneteAsta = importo
                    print(f"Nave venduta per {moneteAsta} monete.")
                    return moneteDisponibili + moneteAsta
                offerteUsate[importo] = volteVisto + 1


def mostraFinale():
    print("\n=== FINE DEL VIAGGIO ===")

    fattore = random.choice([0.5, 1, 2])
    valoriBase = {"perle": 2, "manufatti": 2, "spezie": 1}

    perle     = tutto["merciNuovoMondo"].get("perle", 0)
    manufatti = tutto["merciNuovoMondo"].get("manufatti", 0)
    spezie    = tutto["merciNuovoMondo"].get("spezie", 0)

    profitto = (
        perle     * valoriBase["perle"]     * fattore +
        manufatti * valoriBase["manufatti"] * fattore +
        spezie    * valoriBase["spezie"]    * fattore
    )

    print(f"Fattore di mercato: x{fattore}")
    print(f"Perle: {perle}  |  Manufatti: {manufatti}  |  Spezie: {spezie}")
    print(f"Profitto dalla vendita merci: {profitto:.0f} monete")

    moneteResidue = tutto["monete"]
    print(f"Monete residue (al netto degli acquisti iniziali): {moneteResidue:.0f}")

    totaleMerce = profitto + moneteResidue
    pagaEquipaggio = calcolaPagaEquipaggio()
    print(f"Totale da pagare all'equipaggio: {pagaEquipaggio:.0f} monete")

    saldo = totaleMerce - pagaEquipaggio

    if saldo < 0:
        print(f"Non hai abbastanza monete per pagare l'equipaggio (mancano {abs(saldo):.0f}).")
        if Decisione("Vuoi mettere all'asta la nave? (si/no): "):
            totaleMerce = asta(totaleMerce)
            saldo = totaleMerce - pagaEquipaggio

    if saldo > 0:
        print(f"\n=== RISULTATO POSITIVO === Hai pagato l'equipaggio e ti avanzano {saldo:.0f} monete!")
    elif saldo == 0:
        print("\n=== RISULTATO NULLO === Hai pagato l'equipaggio esattamente. Tanta fatica per niente...")
    else:
        print(f"\n=== RISULTATO NEGATIVO === Non sei riuscito a pagare l'equipaggio. Devi ancora {abs(saldo):.0f} monete.")

    print("\nIl gioco e' davvero finito!")


def faseNuovoMondo():
    arrivoNuovoMondo()

    if not tutto["gameover"]:
        baratto()
        ilTradimento()

    if not tutto["gameover"]:
        epilogo()
        mostraFinale()


# Main

scelta = benvenuto()

if scelta == "esci":
    print("Alla prossima avventura!")

elif scelta == "carica":

    if not os.path.exists(SALVATAGGIO_FILE):
        print("Nessun salvataggio trovato. Avvio una nuova partita.")
        caricato = False
    else:
        dati = carica()

        if isinstance(dati, dict) and "settimana" in dati:
            tutto = dati
            caricato = True
        else:
            print("Salvataggio non valido. Avvio una nuova partita.")
            caricato = False

    if not caricato:
        ingaggioEquipaggio()
        acquistoScorte()
        acquistoMerci()

    # CICLO DI GIOCO
    while tutto["settimana"] <= tutto["setViaggio"] and not tutto["gameover"]:
        pulisci_schermo()
        Step1()
        input("Premi INVIO per continuare...")

        if not tutto["gameover"]:
            pulisci_schermo()
            step2()
            input("Premi INVIO per continuare...")

            if not tutto["gameover"]:
                pulisci_schermo()
                step4()
                Step5()

                if not tutto["gameover"]:
                    if Decisione("Vuoi salvare la partita? (si/no): "):
                        tutto["settimana"] += 1
                        salva()
                        Step6()

                input("Premi INVIO per continuare...")

    pulisci_schermo()
    if tutto["gameover"]:
        print("=== GAME OVER ===")
        print("Statistiche finali:")
        step4()
    else:
        faseNuovoMondo()

else:  # nuova partita

    ingaggioEquipaggio()
    acquistoScorte()
    acquistoMerci()

    while tutto["settimana"] <= tutto["setViaggio"] and not tutto["gameover"]:
        pulisci_schermo()
        Step1()
        input("Premi INVIO per continuare...")

        if not tutto["gameover"]:
            pulisci_schermo()
            step2()
            input("Premi INVIO per continuare...")

            if not tutto["gameover"]:
                pulisci_schermo()
                step4()
                Step5()

                if not tutto["gameover"]:
                    if Decisione("Vuoi salvare la partita? (si/no): "):
                        tutto["settimana"] += 1
                        salva()
                        Step6()

                input("Premi INVIO per continuare...")

    pulisci_schermo()
    if tutto["gameover"]:
        print("=== GAME OVER ===")
        print("Statistiche finali:")
        step4()
    else:
        faseNuovoMondo()
