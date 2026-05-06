import random , os

NESSUN_IMPREVISTO = "Nessun imprevisto"
AVVISTAMENTO_ALBATRO = "Avvistamento albatro"



eventi = [
    "Nessun imprevisto",
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




Ciurma=[["Marinaio",00],
        ["Cuoco",00],
        ["Meccanico",00],
        ["Navigatore",00],
        ["Medico",00],
        ["Marinaio",00],
        ["Cuoco",00],
        ["Meccanico",00],
        ["Navigatore",00],
        ["Medico",00]]

Verdure=100
Frutta=100
Carne=100
Acqua=100
Morale=100
Medicinali=100
Armi=100
Stoffa=100
Coltelli=100
Diamanti=100

Sfortuna=0
setViaggio=8
setCor=1
setRimaste=setViaggio-setCor
avvAlbatro=0

MoltVerdure=1
MoltFrutta=1
MoltCarne=1
MoltAcqua=1

GameOver=False

def UomoBordo(Professione):
    global Ciurma
    for i in range(len(Ciurma)):
        if Ciurma[i][0] == Professione:
            return True

    return False

def Decisione(stringa):
    fine=False
    while not fine:
        Decisione=input(f"{stringa}").replace(" ","").lower()
        if Decisione=="si":
            return True
        elif Decisione=="no":
            return False
                   
def clear_screen():
    os.system('cls')
#eventi

#region Step1

def Step1():
    global eventi ,avvAlbatro
    print(f"settimana numero {setCor} di {setViaggio} settimane previste")
    # evento=random.randint(0,len(eventi))
    evento=random.randint(0,len(eventi)-1)

    print(f"evento della settimane : {eventi[evento]}" )


    
    if eventi[evento]=="Uomo in mare":
        UomoInMare()
        
    if eventi[evento]=="Verdura in mare":
        VerduraInMare()

    if eventi[evento]=="Frutta in mare":
        FruttaInMare()

    if eventi[evento]=="Carne in mare":
        CarneInMare()

    if eventi[evento]=="Acqua in mare":
        AcquaInMare() 

    if eventi[evento]=="Pesca miracolosa":
        PescaMiracolosa() 

    if eventi[evento]=="Tempesta miracolosa":
        TempestaMiracolosa()   
    if eventi[evento]=="Venti favorevoli":
        VentiFavorevoli()

    if eventi[evento]=="Cattivo tempo":
        CattivoTempo()
    
    if eventi[evento]=="Ondata":
        Ondata()

    if eventi[evento]=="Infestazione ratti":
        InfestazioneRatti()

    if eventi[evento]=="Avvistamento albatro"  :
        avvAlbatro+=1
        AvvistamentoAlbatro()
    
    if eventi[evento]=="Avvistamento scialuppa":
        AvvistamentoScialuppa()

    if eventi[evento]=="Epidemia":
        Epidemia()
    
    if eventi[evento]=="Attacco pirata":
        AttaccoPirata()
    
    if eventi[evento]=="Danni al timone":
        DanniAlTimone()
    
    if eventi[evento]=="Raffiche di vento":
        RafficheDiVento()

    if eventi[evento]=="Avvistamento isola":
        AvvistamentoIsola()

    if eventi[evento]=="Nessun imprevisto":
        print("Questa settimana non  c'è stato alcun imprevisto")


    if evento==0 or (eventi[evento]=="Avvistamento albatro" and avvAlbatro < 3):
        pass
    else:
        eventi.pop(evento) 







def UomoInMare():
    global Ciurma

    if len(Ciurma)>0:

        uomo = random.randint(0,len(Ciurma) - 1)
        print(f"Un {Ciurma[uomo][0]} è finito in mare ")
        Ciurma.pop(uomo)
    else:
        print("Nessun Uomo rimasto per cadere in mare")

def VerduraInMare():
    global Verdure
    if Verdure>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% delle verdure")
        Verdure-=Verdure*percentuale
        print(f"Sono rimasti {Verdure:.1f} Kg di verdure ")
    else:
        print("Non avendo verdura nulla è caduto in mare")
        Verdure=0

def FruttaInMare():
    global Frutta
    if Frutta>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% della frutta")
        Frutta-=Frutta*percentuale
        print(f"Sono rimasti {Frutta:.1f} Kg di Frutta ")
    else:
        print("Non avendo Frutta nulla è caduto in mare")
        Frutta=0

def CarneInMare():
    global Carne
    if Carne>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% della carne")
        Carne-=Carne*percentuale
        print(f"Sono rimasti {Carne:.1f} Kg di carne ")
    else:
        print("Non avendo carne nulla è caduto in mare")
        Carne=0

def AcquaInMare():
    global Acqua
    if Acqua>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% della acqua")
        Acqua-=Acqua*percentuale
        print(f"Sono rimasti {Acqua:.1f} barili di acqua ")
    else:
        print("Non avendo acqua nulla è caduto in mare")
        Acqua=0

def PescaMiracolosa():

    global Carne
    print("Durante una settimana di quiete l’equipaggio ne approfitta per pescare.")
    Pesca=random.randint(11,20)
    Carne+=Pesca
    print(f"Siete riusciti a pescare {Pesca} Kg di Carne di pesce")
    print(f"La carne totale ora è di {Carne} Kg")

def TempestaMiracolosa():
    global Acqua
    print("Durante una tempesta alcuni uomini coraggiosi raccolgono acqua nei barili vuoti")
    Raccolta=random.randint(11,20)
    Acqua+=Raccolta
    print(f"Siete riusciti a Raccogliere {Raccolta} Barili di Acqua ")
    print(f"L'acqua totale ora è di {Acqua} Barili")

def VentiFavorevoli():

    global Morale,setViaggio
    print("Un vento favorevole accorcia il viaggio di una settimana.")  
    Aumento=random.randint(5,15)
    for i in range(len(Ciurma)):
        Ciurma[i][1]+=Aumento
    
    print("Grazie a questo vento riuscite a saltare una settimana")
    setViaggio-=1
    print(f"Il viaggio si accorcia di una settimana, il morale della ciurma è aumentato di {Aumento}")

def CattivoTempo():
    global Medicinali
    if Medicinali>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% della bottiglie di medicinali ")
        Medicinali-=Medicinali*percentuale
        print(f"Sono rimaste {Medicinali:.1f} bottiglie di medicinali ")
    else:
        print("Non avendo medicinali nulla è rovesciato in mare")
        Medicinali=0

def Ondata():
    global Armi
    if Armi>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Un onda altissima rovescia via i l {percentuale*100:.0f}% della armi ")
        Armi-=Armi*percentuale
        print(f"Sono rimaste {Armi:.1f} armi ")
    else:
        print("Non avendo armi nulla è stato rovesciato in mare")
        Armi=0

def InfestazioneRatti():
    global Stoffa
    if Stoffa>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Un infestazione di ratti rovina il  {percentuale*100:.0f}% della stoffa ")
        Stoffa-=Stoffa*percentuale
        print(f"Sono rimasti {Stoffa:.1f} pezzi di stoffa ")
    else:
        print("Non avendo Stoffa nulla è stato rovinato")
        Stoffa=0

def AvvistamentoAlbatro():
    fine=False
    global Armi,Ciurma,Carne,Sfortuna

    print("Hai avvistato un albatro")

    if Armi<len(Ciurma):
        tentativi=Armi
    else:
        tentativi=len(Ciurma)


    if tentativi<=0:
        print("Pultruppo non hai abbastanza tentativi per provare a far fuori l'albatro")
        print("Questa settimana non succede niente ")
    else:   
        while tentativi > 0:

            if Decisione(f"vuoi provare a farlo fuori?, hai {tentativi} tentativi rimasti "):
                Ucciso=random.randint(1,2)
                tentativi -= 1
                Armi -= 1
                if Ucciso == 1:
                    Aggiunta=random.randint(10,20)
                    Carne+=Aggiunta
                    Sfortuna+=1
                    print(f"Hai ucciso l' albatro, si aggiungono {Aggiunta} Kg di carne alle tue scorte, Ti rimangono {Carne} Kg di carne")
                    return 
                else:
                    print("Sfortunamente il colpo non è andato a segno ")
            else:
                print("Hai deciso di lasciare stare l 'alabro , la fortuna sarà dalla tua parte ")
                return

def AvvistamentoScialuppa():
    global Ciurma,Verdure,Frutta,Carne,Acqua,Medicinali,Stoffa,Armi,Coltelli,Diamanti
    Scelta=False
    print("Una scialuppa con 4 uomini a bordo e un grande forziere si avvicina ")
    while not Scelta:
        Decisione=input("Vuoi accogliere questi naufraghi e riceve in cambio il loro forziere ? ").replace(" ","").lower()
        
        if Decisione not in ("si","no"):
            print("Scelta non valida")
            Scelta=False
        else:
            if Decisione=="si":
                for i in range(4): 
                    Professione=random.choice(["Marinaio","Cuoco","Meccanico","Medico","Navigatore"])
                    MorIniziale=random.randint(25,75)
                    Ciurma.append([Professione,MorIniziale])
                    print(f"Alla tua ciurma è stato aggiunto un {Professione} , con {MorIniziale} di morale")

                print("Le risorse della cassa sono state aggiunte al tuo inventario")

                Verdure+=random.randint(10,20)
                Frutta+=random.randint(10,20)
                Carne+=random.randint(10,20)
                Acqua+=random.randint(10,20)
                
                Medicinali+=random.randint(10,20)
                Armi+=random.randint(10,20)
                Stoffa+=random.randint(10,20)
                Coltelli+=random.randint(10,20)
                Diamanti+=random.randint(10,20)
                return
                    
            else:
                print("Peccato avresti potuto ricevere tante riconpense...")
                print("questa settimana non succede niente")
                return

def Epidemia():
    global Medicinali,Ciurma
    NumeroCurati=0
    PosMalati=[]
    print("Un epidemia si sta spargendo tra i membri della nave ")
    for i in range(len(Ciurma)):
        if Ciurma[i][0]=="Medico":
            pass
        else:
            Infetto=random.randint(1,100)
            if  Infetto<=70:
                PosMalati.append(i)

    print(PosMalati)
    NumeroMalati=len(PosMalati)

           
    if UomoBordo("Medico"):
        print("fortunamente c'e un Medico a bordo .")
        while Medicinali > 0 and len(PosMalati) > 0:
            Medicinali-=1
            NumeroCurati+=1
            print(f"Sei riuscito a salvare un {Ciurma[PosMalati[0]][0]}")
            PosMalati.pop(0)

    morti=len(PosMalati)
    if len(PosMalati)>0:
        for i in range( len(PosMalati) -1, -1, -1):
            Ciurma.pop(PosMalati[i])
    
    print(f"Persone malete : {NumeroMalati},Persone curate : {NumeroCurati} ,Persone Morte : {morti}")

def AttaccoPirata():    
    global Armi, Ciurma
    Pirati=random.randint(3,10)
    
    
    if Decisione(f"Una nave di formata da {Pirati} pirati sferra un attacco, Vuoi provare a difenderti ?"):

        if Armi < len(Ciurma):
            Difensori = Armi
        else:
            Difensori = len(Ciurma)
        
        #Difensori = min(Armi, len(Ciurma))

        Perdite = min(Pirati - Difensori, len(Ciurma))
        if Perdite<=0:
            print("Hai avuto la meglio sui pirati , non perdendo nessun uomo ")
            print(f"Hai consumato {Pirati} armi")
        else:
            print("I pirati hanno avuto la meglio ...")
            for i in range(Perdite):
                print(Ciurma)
                Posizione=random.randint(0,len(Ciurma)-1)
                print(Posizione)
                print(f"Hai perso un {Ciurma[Posizione][0]} ")

                Ciurma.pop(Posizione)
            print(f"Hai anche consumato {Perdite} Armi")
    else:
        pass

def DanniAlTimone():

    global setViaggio
    print("L’urto con uno scoglio danneggia il timone ci butta fuori rotta")

    if UomoBordo("Meccanico"):
        print("Per fortuna c'è un meccanico a bordo e il viaggio si allunga di una sola settimana. ")
        setViaggio+=1

    else:
        print("Sfortunatamente non ci sono meccanici a bordo , la tua ciurma a provato comunque a risolvere")
        SetAllunga=random.randint(2,4)
        setViaggio+=SetAllunga
        print(f"Il viaggio si allunga di {SetAllunga} settimante")

def RafficheDiVento():
    global setViaggio
    print("Forti raffiche di vento allontanano la nave dalla rotta corretta.")

    if UomoBordo("Navigatore"):
        print("Per fortuna c'è un Navigatore a bordo e il viaggio si allunga di una sola settimana. ")
        setViaggio+=1

    else:
        print("Sfortunatamente non ci sono Navigatoria a bordo , la tua ciurma a provato comunque a risolvere...")
        SetAllunga=random.randint(2,4)
        setViaggio+=SetAllunga
        print(f"Il viaggio si allunga di {SetAllunga} settimante")

def AvvistamentoIsola():
    global Sfortuna,Medicinali,Armi,Coltelli,Diamanti,Stoffa,avvAlbatro
    if Decisione("è stata avvistata un isola in lontanzanza , vuoi provare ad approdarci? "):
        Arrivi=random.randint(1,2)
        if Arrivi==1:
            print("Fortunatamente sei riuscito ad approdare sull l'isola , ci sono anche altre persone!")
            Ostili=random.randint(1,2)
            if Ostili==1:
                print("Queste persone sembrano ostili, meglio allontanarsi per questa volta ...")
                print("Questa settimana non succede nient'altro")
            else:
                print("Queste persone sembrano pacifiche proviamo a parlargli")
                print("Hanno deciso di regalarti un tesore , Hai trovato un sacco di risorse in esso: ")
                if avvAlbatro>=1 and Sfortuna==0:
                    print("Avendo lasciato stare l Albatro la fortuna è dalla tua parte ! ")
                    Medicinali+=random.randint(20,40)
                    Armi+=random.randint(20,40)
                    Stoffa+=random.randint(20,40)
                    Coltelli+=random.randint(20,40)
                    Diamanti+=random.randint(20,40)
                else:
                    Medicinali+=random.randint(10,20)
                    Armi+=random.randint(10,20)
                    Stoffa+=random.randint(10,20)
                    Coltelli+=random.randint(10,20)
                    Diamanti+=random.randint(10,20)
        else:
            print("Sfortunatamente non sei riuscito ad approdare sull 'isola , andarà meglio la prossima volta")
    else:
        print("Hai deciso di non andare sul l'isola , non saprai mai cosa ti sei perso ")
#endregion


#region Step 2/3
VariazioneMorale=0
    
def QuantitaScorte(Scorta, MoltScorta, ScortaNecessaria,NomeScorta,UnitaScorta, VariazioneMorale):
    global setRimaste,GameOver
    if Scorta<=0:
        print(f"Non ci sono {NomeScorta} a sufficenza, il morale della ciurma si abbassa di 10 ")
        VariazioneMorale -= 2
    else:
        print(f"La quantità necessaria di {NomeScorta} è {ScortaNecessaria:.1f} {UnitaScorta} a settimana (totale necessario {(ScortaNecessaria * setRimaste)} {UnitaScorta}) e per il resto del viaggio ti restano {Scorta:.1f} {UnitaScorta}.")
        if Scorta > 2 * ScortaNecessaria * setRimaste:
            print(f"Hai a disposizione più del doppio di {NomeScorta} necessario per il viaggio, {Scorta} {UnitaScorta}")
            if Decisione("Vuoi raddoppiare le razioni e incremenatre il morale della ciurma di 5 unità?   "):
                MoltScorta *= 2
                VariazioneMorale += 1
            
        elif Scorta < ScortaNecessaria * setRimaste:
            print(f"Non hai abbastanza {NomeScorta}  per le prossime settimante, ti restano solo {Scorta} {UnitaScorta}")
            if Decisione(f"Vuoi dimezzare le razioni di {NomeScorta}, salverai gli uomini facendogli perdere solo 5 di morale?   "):
                MoltScorta *= 0.5
                VariazioneMorale -= 1

    return MoltScorta, VariazioneMorale
                
def step2():
    
    global Verdure,Frutta,Carne,Acqua,Ciurma,setRimaste,MoltVerdure,MoltAcqua,MoltCarne,MoltFrutta,VariazioneMorale, GameOver

    VerduraNecessaria=len(Ciurma) * 0.5 * MoltVerdure
    FruttaNecessaria=len(Ciurma) * MoltFrutta
    CarneNecessaria=len(Ciurma) * MoltCarne
    AcquaNecessaria=len(Ciurma) * 0.5 * MoltAcqua
    
    Verdure -= VerduraNecessaria
    Frutta -= FruttaNecessaria
    Carne -= CarneNecessaria
    Acqua -= AcquaNecessaria

    #verdura

    MoltVerdure, VariazioneMorale = QuantitaScorte(Verdure,MoltVerdure,VerduraNecessaria,"Verdura","Kg",VariazioneMorale)
    MoltFrutta, VariazioneMorale = QuantitaScorte(Frutta,MoltFrutta,FruttaNecessaria,"Frutta","Kg",VariazioneMorale)
    MoltCarne, VariazioneMorale = QuantitaScorte(Carne,MoltCarne,CarneNecessaria,"Carne","Kg",VariazioneMorale)
    MoltAcqua, VariazioneMorale = QuantitaScorte(Acqua,MoltAcqua,AcquaNecessaria,"Acqua","Barili",VariazioneMorale)
    #frutta

    #Step 3

    for i in range(len(Ciurma)-1,-1,-1):
        Ciurma[i][1] += 5*VariazioneMorale
        if Ciurma[i][1]<=0:
            print(f"Purtroppo è morto un {Ciurma[i][0]} a causa del suo morale troppo basso ...")
            Ciurma.pop(i)

    if len(Ciurma)==0:
        print("AMMUTINAMENTO !! I TUOI UOMINI TI HANNO ABBANDONATO ,(trattali meglio la prossima volta )")
        GameOver = True





    #endregion


#region Step4

def step4_Ciurma():
    global Ciurma ,Morale
    print(f"Equipaggio residuo {len(Ciurma)}")
    for i in range(len(Ciurma)):
        print(f"- {Ciurma[i][0]} | Morale : {Ciurma[i][1]}")
    
def step4_Scorte():
    global Verdure,Frutta,Carne,Acqua

    if Verdure<=0:
        Verdure=0

    if Frutta<=0:
        Frutta=0

    if Carne<=0:
        Carne=0

    if Acqua<=0:
        Acqua=0

    print("Risorse rimaste : ")
    print(f"-Verdura : {Verdure:.1f} Kg")
    print(f"-Frutta : {Frutta:.1f} Kg")
    print(f"-Carne : {Carne:.1f} Kg")
    print(f"-Acqua : {Acqua:.1f} Barili")

def step4_Merci():
    global Medicinali
    print("Merci residue : ")
    print(f"- Bottiglie di Medicinali : {Medicinali:.1f}")
    print(f"- Armi : {Armi:.1f}")
    print(f"- Stoffa : {Stoffa:.1f}")
    print(f"- Coltelli : {Coltelli:.1f}")
    print(f"- Diamanti : {Diamanti:.1f}")

def step4():
    step4_Ciurma()
    step4_Scorte()
    step4_Merci()


#endregion

#region Step5
def Step5():
    global VariazioneMorale,Ciurma,setViaggio,GameOver,MoltVerdure,MoltFrutta,MoltCarne,MoltAcqua
    PunteggioAmmutinamento=0

    if MoltVerdure <1 or  MoltFrutta<1 or MoltCarne<1 or MoltCarne<1:
        PunteggioAmmutinamento+=30
        print("Razioni cibo ridotte, rischi l'ammutinamento per aver dimezzato le razioni di cibo")

    if not(UomoBordo("Cuoco")):
        PunteggioAmmutinamento+=30
        print("Cuoco Assente, rischi l'ammutinamento non avendo un cuoco a bordo ")

    if avvAlbatro>=1 and Sfortuna>0:
        PunteggioAmmutinamento+=30
        print("Hai voluto uccidere l 'albatro, ora la sfortuna ti perseguita. rischi l ' ammutinamento")
    elif avvAlbatro>=1 and Sfortuna==0:
        PunteggioAmmutinamento-=20
    
    if len(Ciurma)>12:
        PunteggioAmmutinamento+=30
        print("Nave Sovraffollata , rischi l' ammutinamento ")
    
    PunteggioAmmutinamento+=(setViaggio-8) * 10
    if setViaggio>8:
        print("La ciurma è scontenta a causa delle troppe settimane di viaggio , rischi l 'ammutinamento ")
    if PunteggioAmmutinamento<1:
        pass
    elif PunteggioAmmutinamento>100:
        print("AMMUTINAMENTO !! I TUOI UOMINI TI HANNO ABBANDONATO ,(trattali meglio la prossima volta )")
        GameOver=True
        

    
#endregion


#region Step6
def Step6():
    global Ciurma,setViaggio
    UominiMoraleBasso=0
    for i in range(len(Ciurma)):
        if Ciurma[i][1]<=30:
            UominiMoraleBasso+=1

    if UominiMoraleBasso>len(Ciurma)/2:
        print("l’equipaggio lavora di malumore e il viaggio si allunga di una settimana. ")
        setViaggio+=1

#endregion
while setCor < setViaggio and not GameOver: 
    Step1()
    input("Premi invio per continuare")
    step2()
    input("Premi invio per continuare")
    
    setCor+=1
    if GameOver:
        pass
    else:
        step4()
        input("Premi invio per continuare") 
        Step5()

        Step6()
        


