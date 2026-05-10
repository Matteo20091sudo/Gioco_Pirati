import random , os



def UomoBordo(Professione,Ciurma):
    
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

def Step1(eventi,Ciurma,Scorte,Merci,avvAlbatro,setCor,setViaggio,Sfortuna):
    
    print(f"settimana numero {setCor} di {setViaggio} settimane previste")
    # evento=random.randint(0,len(eventi))
    evento=random.randint(0,len(eventi)-1)

    print(f"evento della settimane : {eventi[evento]}" )
    
    if eventi[evento]=="Uomo in mare":
        UomoInMare(Ciurma)
        
    if eventi[evento]=="Verdura in mare":
        ScorteInMare(Scorte,"Verdura","Kg")

    if eventi[evento]=="Frutta in mare":
        ScorteInMare(Scorte,"Frutta","Kg")

    if eventi[evento]=="Carne in mare":
        ScorteInMare(Scorte,"Carne","Kg")

    if eventi[evento]=="Acqua in mare":
        ScorteInMare(Scorte,"Acqua","Barili") 

    if eventi[evento]=="Pesca miracolosa":
        PescaMiracolosa(Scorte) 

    if eventi[evento]=="Tempesta miracolosa":
        TempestaMiracolosa(Scorte)   

    if eventi[evento]=="Venti favorevoli":
        setViaggio=VentiFavorevoli(Ciurma,setViaggio)

    if eventi[evento]=="Cattivo tempo":
        CattivoTempo(Merci)
    
    if eventi[evento]=="Ondata":
        Ondata(Merci)

    if eventi[evento]=="Infestazione ratti":
        InfestazioneRatti(Merci)

    if eventi[evento]=="Avvistamento albatro"  :
        avvAlbatro+=1
        Sfortuna=AvvistamentoAlbatro(Ciurma,Scorte,Merci,Sfortuna)
    
    if eventi[evento]=="Avvistamento scialuppa":
       AvvistamentoScialuppa(Ciurma,Scorte,Merci)

    if eventi[evento]=="Epidemia":
        Epidemia(Ciurma,Merci)
    
    if eventi[evento]=="Attacco pirata":
        AttaccoPirata(Ciurma, Merci)
    
    if eventi[evento]=="Danni al timone":
        setViaggio=DanniAlTimone(Ciurma,setViaggio)
    
    if eventi[evento]=="Raffiche di vento":
        setViaggio=RafficheDiVento(Ciurma,setViaggio)

    if eventi[evento]=="Avvistamento isola":
        AvvistamentoIsola(Merci,avvAlbatro,Sfortuna)

    if eventi[evento]=="Nessun imprevisto":
        print("Questa settimana non  c'è stato alcun imprevisto")

    if evento==0 or (eventi[evento]=="Avvistamento albatro" and avvAlbatro < 3):
        pass
    else:
        eventi.pop(evento)

    return avvAlbatro,setViaggio,Sfortuna

def UomoInMare(Ciurma):
    if len(Ciurma)>0:

        uomo = random.randint(0,len(Ciurma) - 1)
        print(f"Un {Ciurma[uomo][0]} è finito in mare ")
        Ciurma.pop(uomo)
    else:
        print("Nessun Uomo rimasto per cadere in mare")

def ScorteInMare(Scorte,NomeScorta,UnitaScorta):
    if Scorte[NomeScorta]>0:
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% di {NomeScorta}")
        Scorte[NomeScorta]-=Scorte[NomeScorta]*percentuale
        print(f"Sono rimasti {Scorte[NomeScorta]:.1f} {UnitaScorta} di {NomeScorta} ")
    else:
        print(f"Non avendo {NomeScorta} nulla è caduto in mare")
        Scorte[NomeScorta]=0
    
def PescaMiracolosa(Scorte):
    print("Durante una settimana di quiete l’equipaggio ne approfitta per pescare.")
    Pesca=random.randint(11,20)
    Scorte["Carne"]+=Pesca
    print(f"Siete riusciti a pescare {Pesca} Kg di Carne di pesce")
    print(f"La carne totale ora è di {Scorte["Carne"]} Kg")
   
def TempestaMiracolosa(Scorte):
    print("Durante una tempesta alcuni uomini coraggiosi raccolgono acqua nei barili vuoti")
    Raccolta=random.randint(11,20)
    Scorte["Acqua"]+=Raccolta
    print(f"Siete riusciti a Raccogliere {Raccolta} Barili di Acqua ")
    print(f"L'acqua totale ora è di {Scorte["Acqua"]} Barili")
    
def VentiFavorevoli(Ciurma,setViaggio):

    
    print("Un vento favorevole accorcia il viaggio di una settimana.")  
    Aumento=random.randint(5,15)
    for i in range(len(Ciurma)):
        Ciurma[i][1]+=Aumento
    
    print("Grazie a questo vento riuscite a saltare una settimana")
    setViaggio-=1
    print(f"Il viaggio si accorcia di una settimana, il morale della ciurma è aumentato di {Aumento}")
    return setViaggio

def CattivoTempo(Merci):
    
    if Merci["Medicinali"]>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Sono cadute in mare il {percentuale*100:.0f}% della bottiglie di medicinali ")
        Merci["Medicinali"]-=Merci["Medicinali"]*percentuale
        print(f"Sono rimaste {Merci["Medicinali"]:.1f} bottiglie di medicinali ")
    else:
        print("Non avendo medicinali nulla è rovesciato in mare")
        MedicMerci["Medicinali"]=0
    
def Ondata(Merci):
    
    if Merci["Armi"]>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Un onda altissima rovescia via i l {percentuale*100:.0f}% della armi ")
        Merci["Armi"]-=Merci["Armi"]*percentuale
        print(f"Sono rimaste {Merci["Armi"]:.1f} armi ")
    else:
        print("Non avendo armi nulla è stato rovesciato in mare")
        Merci["Armi"]=0
    
def InfestazioneRatti(Merci):
    if Merci["Stoffa"]>0:
        
        percentuale=random.choice([1/2,1/3,1/4,1/5])
        print(f"Un infestazione di ratti rovina il  {percentuale*100:.0f}% della stoffa ")
        Merci["Stoffa"]-=Merci["Stoffa"]*percentuale
        print(f"Sono rimasti {Merci["Stoffa"]:.1f} pezzi di stoffa ")
    else:
        print("Non avendo Stoffa nulla è stato rovinato")
        Merci["Stoffa"]=0
    
def AvvistamentoAlbatro(Ciurma,Scorte,Merci,Sfortuna):
    print("Hai avvistato un albatro")

    if Merci["Armi"]<len(Ciurma):
        tentativi=Merci["Armi"]
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
                Merci["Armi"] -= 1
                if Ucciso == 1:
                    Aggiunta=random.randint(10,20)
                    Scorte["Carne"]+=Aggiunta
                    Sfortuna+=1
                    print(f"Hai ucciso l' albatro, si aggiungono {Aggiunta} Kg di carne alle tue scorte, Ti rimangono {Scorte["Carne"]} Kg di carne")
                    return Sfortuna
                else:
                    print("Sfortunamente il colpo non è andato a segno ")
            else:
                print("Hai deciso di lasciare stare l 'alabro , la fortuna sarà dalla tua parte ")
                return Sfortuna
    return Sfortuna

def AvvistamentoScialuppa(Ciurma,Scorte,Merci):
    
    print("Una scialuppa con 4 uomini a bordo e un grande forziere si avvicina ")
    
    if Decisione("Vuoi accogliere questi naufraghi e riceve in cambio il loro forziere ?"):
        for i in range(4): 
            Professione=random.choice(["Marinaio","Cuoco","Meccanico","Medico","Navigatore"])
            MorIniziale=random.randint(25,75)
            Ciurma.append([Professione,MorIniziale])
            print(f"Alla tua ciurma è stato aggiunto un {Professione} , con {MorIniziale} di morale")

        print("Le risorse della cassa sono state aggiunte al tuo inventario")

        Scorte["Verdura"]+=random.randint(10,20)
        Scorte["Frutta"]+=random.randint(10,20)
        Scorte["Carne"]+=random.randint(10,20)
        Scorte["Acqua"]+=random.randint(10,20)
        
        Merci["Medicinali"]+=random.randint(10,20)
        Merci["Armi"]+=random.randint(10,20)
        Merci["Stoffa"]+=random.randint(10,20)
        Merci["Sale"]+=random.randint(10,20)
        Merci["Coltelli"]+=random.randint(10,20)
        Merci["Diamanti"]+=random.randint(10,20)
        
    else:
        print("Peccato avresti potuto ricevere tante riconpense...")
        print("questa settimana non succede niente")
         
def Epidemia(Ciurma,Merci):
    
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

    
    NumeroMalati=len(PosMalati)

           
    if UomoBordo("Medico",Ciurma):
        print("fortunamente c'e un Medico a bordo .")
        while Merci["Medicinali"] > 0 and len(PosMalati) > 0:
            Merci["Medicinali"]-=1
            NumeroCurati+=1
            print(f"Sei riuscito a salvare un {Ciurma[PosMalati[0]][0]}")
            PosMalati.pop(0)

    morti=len(PosMalati)
    if len(PosMalati)>0:
        for i in range( len(PosMalati) -1, -1, -1):
            Ciurma.pop(PosMalati[i])
    
    print(f"Persone malete : {NumeroMalati},Persone curate : {NumeroCurati} ,Persone Morte : {morti}")
   
def AttaccoPirata(Ciurma,Merci):    
   
    Pirati=random.randint(3,10)
    if Decisione(f"Una nave di formata da {Pirati} pirati sferra un attacco, Vuoi provare a difenderti ?"):

        if Merci["Armi"] < len(Ciurma):
            Difensori = Merci["Armi"]
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
            Merci["Armi"]-=Perdite
    
def DanniAlTimone(Ciurma,setViaggio):

    
    print("L’urto con uno scoglio danneggia il timone ci butta fuori rotta")

    if UomoBordo("Meccanico",Ciurma):
        print("Per fortuna c'è un meccanico a bordo e il viaggio si allunga di una sola settimana. ")
        setViaggio+=1

    else:
        print("Sfortunatamente non ci sono meccanici a bordo , la tua ciurma a provato comunque a risolvere")
        SetAllunga=random.randint(2,4)
        setViaggio+=SetAllunga
        print(f"Il viaggio si allunga di {SetAllunga} settimante")
    return setViaggio

def RafficheDiVento(Ciurma,setViaggio):
    
    print("Forti raffiche di vento allontanano la nave dalla rotta corretta.")

    if UomoBordo("Navigatore",Ciurma):
        print("Per fortuna c'è un Navigatore a bordo e il viaggio si allunga di una sola settimana. ")
        setViaggio+=1

    else:
        print("Sfortunatamente non ci sono Navigatoria a bordo , la tua ciurma a provato comunque a risolvere...")
        SetAllunga=random.randint(2,4)
        setViaggio+=SetAllunga
        print(f"Il viaggio si allunga di {SetAllunga} settimante")
    return setViaggio

def AvvistamentoIsola(Merci,avvAlbatro,Sfortuna):
    
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
                    Merci["Medicinali"]+=random.randint(20,40)
                    Merci["Armi"]+=random.randint(20,40)
                    Merci["Sale"]+=random.randint(20,40)
                    Merci["Stoffa"]+=random.randint(20,40)
                    Merci["Coltelli"]+=random.randint(20,40)
                    Merci["Diamanti"]+=random.randint(20,40)
                else:
                    Merci["Medicinali"]+=random.randint(10,20)
                    Merci["Armi"]+=random.randint(10,20)
                    Merci["Sale"]+=random.randint(10,20)
                    Merci["Stoffa"]+=random.randint(10,20)
                    Merci["Coltelli"]+=random.randint(10,20)
                    Merci["Diamanti"]+=random.randint(10,20)
        else:
            print("Sfortunatamente non sei riuscito ad approdare sull 'isola , andarà meglio la prossima volta")
    else:
        print("Hai deciso di non andare sul l'isola , non saprai mai cosa ti sei perso ")

#endregion


#region Step 2/3

def step2_3(Ciurma,Scorte,VariazioniPasto,setRimaste,GameOver):

    VerduraNecessaria = len(Ciurma) * 0.5 * VariazioniPasto["Moltiplicatore"]["Verdura"]
    FruttaNecessaria= len(Ciurma) * VariazioniPasto["Moltiplicatore"]["Frutta"]
    CarneNecessaria= len(Ciurma) * VariazioniPasto["Moltiplicatore"]["Carne"]
    AcquaNecessaria= len(Ciurma) * 0.5 * VariazioniPasto["Moltiplicatore"]["Acqua"]
    
    Scorte["Verdura"] -= VerduraNecessaria
    Scorte["Frutta"] -= FruttaNecessaria
    Scorte["Carne"] -= CarneNecessaria
    Scorte["Acqua"] -= AcquaNecessaria
    
    QuantitaScorte(Scorte["Verdura"], VariazioniPasto, VerduraNecessaria,"Verdura","Kg",setRimaste)
    print()
    QuantitaScorte(Scorte["Frutta"], VariazioniPasto, FruttaNecessaria,"Frutta","Kg",setRimaste)
    print()              
    QuantitaScorte(Scorte["Carne"], VariazioniPasto, CarneNecessaria,"Carne","Kg",setRimaste)
    print()              
    QuantitaScorte(Scorte["Acqua"], VariazioniPasto, AcquaNecessaria,"Acqua","Barili",setRimaste)
    print()              
   

    #Step 3
    
    VariazioneMorale=0
    for esaurito in VariazioniPasto["Esaurimento"].items():
        if esaurito[1]:
            VariazioneMorale-=10
            #print(f"Finite {esaurito[0]} - {VariazioneMorale}")
    for dimezzo in VariazioniPasto["Dimezzo"].items():
        if dimezzo[1]:
            VariazioneMorale-=5
            #print(f"dimezzo {dimezzo[0]} - {VariazioneMorale}")
    for raddoppio in VariazioniPasto["Raddoppio"].items():
        if raddoppio[1]:
            VariazioneMorale+=5
            #print(f"raddoppio {raddoppio[0]} - {VariazioneMorale}")

    

    for i in range(len(Ciurma)-1,-1,-1):
        Ciurma[i][1] += VariazioneMorale
        if Ciurma[i][1]<=0:
            print(f"Purtroppo è morto un {Ciurma[i][0]} a causa del suo morale troppo basso ...")
            Ciurma.pop(i)

    if len(Ciurma)==0:
        print("AMMUTINAMENTO !! I TUOI UOMINI TI HANNO ABBANDONATO ,(trattali meglio la prossima volta )")
        GameOver = True
    return GameOver
  
def QuantitaScorte(Scorta, VariazioniScorta, ScortaNecessaria,NomeScorta,UnitaScorta,setRimaste):
    TotaleNecessario=ScortaNecessaria * setRimaste
    if Scorta<=0:
        print(f"Non ci sono {NomeScorta} a sufficenza, il morale della ciurma si abbassa di 10 ")
        VariazioniScorta["Esaurimento"][NomeScorta] = True
    else:
        print(f"La quantità necessaria di {NomeScorta} è {ScortaNecessaria:.1f} {UnitaScorta} a settimana (totale necessario {TotaleNecessario:.1f} {UnitaScorta}) e per il resto del viaggio ti restano {Scorta:.1f} {UnitaScorta}.")
        if Scorta > 2 * TotaleNecessario:
            print(f"Hai a disposizione più del doppio di {NomeScorta} necessario per il viaggio, {Scorta} {UnitaScorta}")
            if Decisione("Vuoi raddoppiare le razioni e incremenatre il morale della ciurma di 5 unità?  "):
                VariazioniScorta["Moltiplicatore"][NomeScorta] *= 2
                VariazioniScorta["Raddoppio"][NomeScorta] = True
            
        elif Scorta < TotaleNecessario:
            print(f"Non hai abbastanza {NomeScorta}  per le prossime settimante, ti restano solo {Scorta} {UnitaScorta}")
            if Decisione(f"Vuoi dimezzare le razioni di {NomeScorta}, salverai gli uomini facendogli perdere solo 5 di morale?   "):
                VariazioniScorta["Moltiplicatore"][NomeScorta] *= 0.5
                VariazioniScorta["Dimezzo"][NomeScorta] = True

                



    #endregion


#region Step4

def step4_Ciurma(Ciurma):
    
    print(f"Equipaggio residuo {len(Ciurma)}")
    for i in range(len(Ciurma)):
        print(f"- {Ciurma[i][0]} | Morale : {Ciurma[i][1]}")
    
def step4_Scorte(Scorte):
    

    if Scorte["Verdura"]<=0:
        Scorte["Verdura"]=0

    if Scorte["Frutta"]<=0:
        Scorte["Frutta"]=0

    if Scorte["Carne"]<=0:
        Scorte["Carne"]=0

    if Scorte["Acqua"]<=0:
        Scorte["Acqua"]=0

    print("Risorse rimaste : ")
    print(f"-Verdura : {Scorte["Verdura"]:.1f} Kg")
    print(f"-Frutta : {Scorte["Frutta"]:.1f} Kg")
    print(f"-Carne : {Scorte["Carne"]:.1f} Kg")
    print(f"-Acqua : {Scorte["Acqua"]:.1f} Barili")

   

def step4_Merci(Merci):

    if Merci["Medicinali"]<=0:
        Merci["Medicinali"]=0

    if Merci["Armi"]<=0:
        Merci["Armi"]=0

    if Merci["Sale"]<=0:
        Merci["Sale"]=0

    if Merci["Stoffa"]<=0:
        Merci["Stoffa"]=0


    if Merci["Coltelli"]<=0:
        Merci["Coltelli"]=0

    if Merci["Diamanti"]<=0:
        Merci["Diamanti"]=0
    print("Merci residue : ")
    print(f"- Bottiglie di Medicinali : {Merci["Medicinali"]:.1f}")
    print(f"- Armi : {Merci["Armi"]:.1f}")
    print(f"- Sale : {Merci["Sale"]:.1f}")
    print(f"- Stoffa : {Merci["Stoffa"]:.1f}")
    print(f"- Coltelli : {Merci["Coltelli"]:.1f}")
    print(f"- Diamanti : {Merci["Diamanti"]:.1f}")

    
def step4(Ciurma,Scorte,Merci):
    
    step4_Ciurma(Ciurma)
    print()
    step4_Scorte(Scorte)
    print()
    step4_Merci(Merci)
    print()
    


#endregion

#region Step5
def Step5(Ciurma,setViaggio,GameOver,VariazioniPasto,avvAlbatro,Sfortuna):
     
    PunteggioAmmutinamento=0
    GameOver=False

    AvvisoGiocatore = ""

    if VariazioniPasto["Moltiplicatore"]["Verdura"] <1 or VariazioniPasto["Moltiplicatore"]["Frutta"]<1 or VariazioniPasto["Moltiplicatore"]["Carne"]<1 or VariazioniPasto["Moltiplicatore"]["Acqua"]<1:
        PunteggioAmmutinamento+=30
        AvvisoGiocatore += "Razioni cibo ridotte, rischi l'ammutinamento per aver dimezzato le razioni di cibo\n"

    if not(UomoBordo("Cuoco",Ciurma)):
        PunteggioAmmutinamento+=30
        AvvisoGiocatore +="Cuoco Assente, rischi l'ammutinamento non avendo un cuoco a bordo\n"

    if avvAlbatro>=1 and Sfortuna>0:
        PunteggioAmmutinamento+=30
        AvvisoGiocatore +="Hai voluto uccidere l 'albatro, ora la sfortuna ti perseguita. rischi l ' ammutinamento\n"
    elif avvAlbatro>=1 and Sfortuna==0:
        PunteggioAmmutinamento-=20
    
    if len(Ciurma)>12:
        PunteggioAmmutinamento+=30
        AvvisoGiocatore +="Nave Sovraffollata , rischi l' ammutinamento\n"
    
    PunteggioAmmutinamento+=(setViaggio-8) * 10
    if setViaggio>8:
        AvvisoGiocatore +="La ciurma è scontenta a causa delle troppe settimane di viaggio , rischi l 'ammutinamento\n"

    if PunteggioAmmutinamento<1 or PunteggioAmmutinamento==100:
        return False
    elif PunteggioAmmutinamento>100:
        AvvisoGiocatore +="AMMUTINAMENTO !! I TUOI UOMINI TI HANNO ABBANDONATO ,(trattali meglio la prossima volta )"
        GameOver = True
    else:
        print(AvvisoGiocatore)

    return GameOver

    
#endregion


#region Step6
def Step6(Ciurma,setViaggio):
    UominiMoraleBasso=0
    for i in range(len(Ciurma)):
        if Ciurma[i][1]<=30:
            UominiMoraleBasso+=1

    if UominiMoraleBasso>len(Ciurma)/2:
        print("l’equipaggio lavora di malumore e il viaggio si allunga di una settimana. ")
        setViaggio+=1
    return setViaggio

#endregion


#---------------------------------------------------------------------------------------------------------------------
def  main():
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




    Ciurma=[["Marinaio",100],
            ["Cuoco",100],
            ["Meccanico",100],
            ["Navigatore",100],
            ["Medico",100],
            ["Marinaio",100],
            ["Cuoco",100],
            ["Meccanico",100],
            ["Navigatore",100],
            ["Medico",100]]

    Scorte={"Verdura":100,
            "Frutta":100,
            "Carne":100,
            "Acqua":100}
        
    Merci={"Medicinali":100,
            "Armi":100,
            "Sale":100,
            "Stoffa":100,
            "Coltelli":100,
            "Diamanti":100}

    Sfortuna=0
    setViaggio=8
    setCor=1
    avvAlbatro=0


    VariazioniPasto={
        "Moltiplicatore":{
            "Verdura":1,
            "Frutta":1,
            "Carne":1,
            "Acqua":1},
        "Raddoppio":{
            "Verdure":False,
            "Frutta":False,
            "Carne":False,
            "Acqua":False
            },
        "Dimezzo":{
            "Verdure":False,
            "Frutta":False,
            "Carne":False,
            "Acqua":False
            },
        "Esaurimento":{
            "Verdure":False,
            "Frutta":False,
            "Carne":False,
            "Acqua":False
            }       
        }

    GameOver=False

    while setCor <= setViaggio and not GameOver:

        avvAlbatro, setViaggio,Sfortuna = Step1(eventi, Ciurma,Scorte,Merci, avvAlbatro, setCor, setViaggio,Sfortuna)
        input("Premi invio per continuare")
        print()              
        setRimaste = setViaggio-setCor
        GameOver=step2_3(Ciurma,Scorte,VariazioniPasto,setRimaste,GameOver)
        input("Premi invio per continuare")
        print()              
        
        setCor+=1
        if GameOver:
            pass
        else:
            step4(Ciurma,Scorte,Merci)
            input("Premi invio per continuare") 
            GameOver=Step5(Ciurma,setViaggio,GameOver,VariazioniPasto,avvAlbatro,Sfortuna)

            setViaggio=Step6(Ciurma,setViaggio)

        print()
        print("------------------------------------------------------------------------")
        print()

main()

