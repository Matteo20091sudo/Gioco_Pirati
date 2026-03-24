from time import sleep
import os
import json
from random import randint

NOME_TUTTO = "./tutto.txt"

# --- LISTE ACQUISTABILI (INVARIATE) ---
attrezzatureAcquistabili = [
    {"nome": "Corde robuste", "prezzo": 45},
    {"nome": "Barili per acqua", "prezzo": 30},
    {"nome": "Kit da fuoco (pietra focaia)", "prezzo": 15},
    {"nome": "Lanterna a olio", "prezzo": 25},
    {"nome": "Kit medico base", "prezzo": 80},
    {"nome": "Telo impermeabile", "prezzo": 55},
    {"nome": "Attrezzi base (coltello, piccola sega)", "prezzo": 40}
]

ciurmaAcquistabile = [
    {"nome": "Capitano", "prezzo": 180},
    {"nome": "Timoniere", "prezzo": 95},
    {"nome": "Medico di bordo", "prezzo": 150},
    {"nome": "Cuoco", "prezzo": 70},
    {"nome": "Mercante/Contabile", "prezzo": 110},
    {"nome": "Marinaio semplice", "prezzo": 45},
    {"nome": "Guardia armata", "prezzo": 85},
    {"nome": "Interprete", "prezzo": 110}
]

ciboAcquistabile = [
    {"nome": "Gallette dure", "prezzo": 40},
    {"nome": "Carne salata", "prezzo": 55},
    {"nome": "Pesce essiccato", "prezzo": 35},
    {"nome": "Formaggio stagionato", "prezzo": 30},
    {"nome": "Legumi secchi", "prezzo": 25},
    {"nome": "Riso", "prezzo": 20},
    {"nome": "Frutta secca", "prezzo": 28},
    {"nome": "Verdure in salamoia", "prezzo": 22},
    {"nome": "Acqua potabile", "prezzo": 60},
    {"nome": "Birra leggera o sidro (per disinfettare l’acqua)", "prezzo": 35},
    {"nome": "Olio e grassi da cucina", "prezzo": 18},
    {"nome": "Spezie e sale", "prezzo": 12}
]

# --- DIZIONARIO UNICO (come richiesto) ---
caratt = {
    "ciurma": [],
    "scorteCibo": [],
    "attrezzatura": [],
    "monete": 2000,
    "settimana": 1
}

# --- IMPREVISTI (INVARIATI) ---
imprevisti = [
    {"nome": "Tempesta improvvisa", "descrizione": "Una tempesta danneggia parte delle scorte.", "monete": -50, "scorte": -2, "ciurma": 0},
    {"nome": "Incontro con mercante", "descrizione": "Un mercante amichevole ti regala provviste.", "monete": 0, "scorte": +2, "ciurma": 0},
    {"nome": "Rissa tra marinai", "descrizione": "Due membri litigano e uno abbandona la nave.", "monete": 0, "scorte": 0, "ciurma": -1},
    {"nome": "Tesoro alla deriva", "descrizione": "Trovi un piccolo forziere galleggiante.", "monete": +120, "scorte": 0, "ciurma": 0}
]

# --- FUNZIONI DI SISTEMA (INVARIATE) ---
def pulisciSchermo():
    os.system("cls")

def caricaTutto():
    try:
        with open(NOME_TUTTO, "r") as f:
            s = f.read()
            if s.strip() == "":
                return caratt
            return json.loads(s)
    except:
        return caratt

def salvaTutto(l):
    with open(NOME_TUTTO, "w") as f:
        f.write(json.dumps(l))

# --- MENU (INVARIATO) ---
def menuIniziale(m):
    print("-------IL-GIOCO-DEI-PIRATI-------")
    print(f"Monete a disposizione: {m}")
    print("1. Acquista membri della ciurma")
    print("2. Acquista scorte di cibo")
    print("3. Acquista attrezzatura")
    print("4. Avanza di una settimana")
    print("0. Esci")
    return int(input("Inserisci la tua scelta: "))

# --- VISUALIZZAZIONI (INVARIATE) ---
def visualizzaCiurmaAcquistabile(l,m):
    print("----------------MONETE-----------------")
    print(m)
    print("---------CIURMA-RAGGRUPPABILE----------")
    for c,i in enumerate(l):
        print(f"{c+1}. Membro: {i['nome']}, prezzo di ingaggio: {i['prezzo']} monete")
    print("---------------------------------------")

def visualizzaScorteAcquistabili(l,m):
    print("----------------MONETE-----------------")
    print(m)
    print("-----------NEGOZIO-SCORTE-CIBO-----------")
    for c,i in enumerate(l):
        print(f"{c+1}. nome: {i['nome']}, prezzo: {i['prezzo']}")
    print("----------------------------------------")

def visualizzaAttrezzaturaAcquistabile(l,m):
    print("----------------MONETE-----------------")
    print(m)
    print("----------NEGOZIO-ATTREZZATURA---------")
    for c,i in enumerate(l):
        print(f"{c+1}. nome: {i['nome']}, prezzo: {i['prezzo']}")
    print("---------------------------------------")

# --- ACQUISTI (MODIFICATI SOLO PER USARE caratt) ---
def acquistoCiurma(l, m):
    ins = "s"
    while ins != "n":
        pulisciSchermo()
        visualizzaCiurmaAcquistabile(l, m)

        ins = input("Vuoi acquistare un nuovo membro della ciurma?(s/n) ").lower()
        if ins == "s":
            s = input("Inserisci chi vuoi acquistare: ")

            for i in l:
                if s == i["nome"]:
                    if m < i["prezzo"]:
                        print("Non hai abbastanza monete!")
                        sleep(1)
                        break

                    caratt["ciurma"].append(i["nome"])
                    m -= i["prezzo"]
                    l.remove(i)
                    print("Membro aggiunto con successo!")
                    break
            else:
                print("Membro non acquistabile o non presente")

        elif ins not in ["s","n"]:
            print("Scelta non valida")

        sleep(1)

    return m

def acquistoScorteCibo(l, m):
    ins = "s"
    while ins != "n":
        pulisciSchermo()
        visualizzaScorteAcquistabili(l, m)

        ins = input("Vuoi acquistare nuove scorte?(s/n) ").lower()
        if ins == "s":
            try:
                e = int(input("Inserisci il numero della scorta: "))
                if e <= 0 or e > len(l):
                    print("Numero non valido")
                else:
                    nome = l[e-1]["nome"]
                    prezzo = l[e-1]["prezzo"]

                    if m < prezzo:
                        print("Non hai abbastanza monete!")
                    else:
                        caratt["scorteCibo"].append(nome)
                        m -= prezzo
                        l.pop(e-1)
                        print("Scorte aggiunte con successo")
            except:
                print("Formato non valido")

        elif ins not in ["s","n"]:
            print("Scelta non valida")

        sleep(1)

    return m

def acquistaAttrezzatura(l, m):
    ins = "s"
    while ins != "n":
        pulisciSchermo()
        visualizzaAttrezzaturaAcquistabile(l, m)

        ins = input("Vuoi acquistare nuova attrezzatura?(s/n) ").lower()
        if ins == "s":
            try:
                e = int(input("Inserisci il numero dell'attrezzo: "))
                if e <= 0 or e > len(l):
                    print("Numero non valido")
                else:
                    nome = l[e-1]["nome"]
                    prezzo = l[e-1]["prezzo"]

                    if m < prezzo:
                        print("Non hai abbastanza monete!")
                    else:
                        caratt["attrezzatura"].append(nome)
                        m -= prezzo
                        l.pop(e-1)
                        print("Attrezzo aggiunto con successo")
            except:
                print("Formato non valido")

        elif ins not in ["s","n"]:
            print("Scelta non valida")

        sleep(1)

    return m

# --- IMPREVISTO (CORRETTO) ---
def applicazioneImprevisto(imp, m):
    print("------IMPREVISTO-SETTIMANALE------")
    print(imp["nome"])
    print(imp["descrizione"])
    print("----------------------------------")

    # Monete
    m += imp["monete"]

    # Scorte
    if imp["scorte"] < 0:
        for _ in range(abs(imp["scorte"])):
            if caratt["scorteCibo"]:
                caratt["scorteCibo"].pop()

    elif imp["scorte"] > 0:
        for _ in range(imp["scorte"]):
            if ciboAcquistabile:
                n1 = randint(0, len(ciboAcquistabile)-1)
                caratt["scorteCibo"].append(ciboAcquistabile[n1]["nome"])

    # Ciurma
    if imp["ciurma"] < 0:
        if caratt["ciurma"]:
            caratt["ciurma"].pop()

    elif imp["ciurma"] > 0:
        for _ in range(imp["ciurma"]):
            if ciurmaAcquistabile:
                n2 = randint(0, len(ciurmaAcquistabile)-1)
                caratt["ciurma"].append(ciurmaAcquistabile[n2]["nome"])

    caratt["settimana"] += 1
    sleep(3)
    return m


fine = False

while not fine:
    pulisciSchermo()
    scelta = int(input("1. Nuova partita\n2. Continua\n0. Esci\nScelta: "))

    if scelta == 1:
        caratt = {
            "ciurma": [],
            "scorteCibo": [],
            "attrezzatura": [],
            "monete": 2000,
            "settimana": 1
        }

    elif scelta == 2:
        caratt = caricaTutto()

    elif scelta == 0:
        print("BYE BYE")
        break

    monete = caratt["monete"]
    settimana = caratt["settimana"]

    esci = False
    while not esci and settimana < 8:
        pulisciSchermo()
        scelta = menuIniziale(monete)

        if scelta == 1:
            monete = acquistoCiurma(ciurmaAcquistabile, monete)
        elif scelta == 2:
            monete = acquistoScorteCibo(ciboAcquistabile, monete)
        elif scelta == 3:
            monete = acquistaAttrezzatura(attrezzatureAcquistabili, monete)
        elif scelta == 4:
            imp = imprevisti[randint(0, len(imprevisti)-1)]
            monete = applicazioneImprevisto(imp, monete)
            settimana += 1
        elif scelta == 0:
            esci = True

        caratt["monete"] = monete
        caratt["settimana"] = settimana
        salvaTutto(caratt)