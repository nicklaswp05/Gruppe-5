print("Erling er leder for et designteam som skal lage en ny medborgerportal for kommunen. \nI teamet har det oppstått noen konflikter.")
poengsum = 0


print("\nFørste konflikt er mellom Silje og Elias. De er uenige om teknologivalg, og det har utviklet seg fra en sakskonflikt til en personkonflikt.")
konflikt_1 = input(" Velg hvilken løsning Erling skal ta:" \
    "\n1) Hold en avstemning over hvilket design som skal brukes" \
    "\n2) Hold individuelle samtaler med hver av de konfliktende partene " \
    "\n3) Hold en anonym avstemning over hvilket design som skal brukes " \
    "\n4) Hold et møte med hele teamet"
    "\n5) Gi dem kjeft \n ")
while konflikt_1 not in ["1", "2", "3", "4", "5"]:
    print("\nUgyldig valg. Vennligst velg 1, 2, 3, 4, eller 5.")
    konflikt_1 = input(" Velg hvilken løsning Erling skal ta: \n ")
if konflikt_1 == "1":
    print("\nDet blir høy risiko for polarisering i teamer og svekket relasjonstillit, men en beslutning er tatt og det er fremdrift i prosjektet")
    poengsum += 0
elif konflikt_1 == "2":
    print("\nErling viser empati og lytter aktivt. Han lover å redusere spenning med relasjonsbygging, men det kan være at det blir tidkrevende for prosjektet")
    poengsum += 1
elif konflikt_1 == "3":
    print("\nSosialt stress er redusert, en rask løsning er gitt, men teamet opplever løsningen som lite dialogbasert")
    poengsum += 1
elif konflikt_1 == "4":
    print("\nErlig minner gruppen på fellesmålene og skaper rom for dialog, en kollektive refleksjon oppstår, men noen mener at møtet for hele teamet var unædvendig")
    poengsum += 1
else:
    print("\nTeamet mister tillit til Erling og jobber dårligere")
    poengsum -= 1


print("\nAndre konflikt er mellom Hamdi og Hallgeir. De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter og kommer med to ganske forskjellige alternativer")
konflikt_2 = input(" Velg hvilken løsning Erling skal ta:" \
    "\n1) Sjefsavgjørelse. Erling velger hvilket design de går for" \
    "\n2) Erling holder møte med Hamdi og Hallgeir for å finne en løsning " \
    "\n3) Erling venter på at Hamdi og Hallgeir løser problemet selv"
    "\n4) Gi dem kjeft \n ")
while konflikt_2 not in ["1", "2", "3", "4"]:
    print("\nUgyldig valg. Vennligst velg 1, 2, 3, eller 4.")
    konflikt_2 = input(" Velg hvilken løsning Erling skal ta: \n ")
if konflikt_2 == "1":
    print("\nEn av partene er misfornøyde med at Erling ikke valgte dem, men prosjektet går videre med tydelig framdriftsplan")
    poengsum += 1
elif konflikt_2 == "2":
    print("\nMålet med designet avklares, og Hamdi og Hallgeir forenes under en felles framdriftsplan")
    poengsum += 2
elif konflikt_2 == "3":
    print("\nFremdrift er svekket og prosjektet forsinkes, kvaliteten på det endelige designet påvirkes negativt")
    poengsum += 0
else:
    print("\nTeamet mister tillit til Erling og jobber dårligere")
    poengsum -= 1


print("\nTredje konflikt gjelder hele teamet. Motivasjonen i teamet har svekket over tid. Fristen nermer seg og energien synker")
konflikt_3 = input(" Velg hvilken løsning Erling skal ta:" \
    "\n1) Ta hele teamet ut til felles middag" \
    "\n2) Ta en prat med hvert medlem individuelt" \
    "\n3) Gi dem kjeft \n ")
while konflikt_3 not in ["1", "2", "3"]:
    print("\nUgyldig valg. Vennligst velg 1, 2, eller 3.")
    konflikt_3 = input(" Velg hvilken løsning Erling skal ta: \n ")
if konflikt_3 == "1":
    print("\nSpenninga svekkes og teamet får en velfortjent feiring av hvor langt de har kommet")
    poengsum += 2
elif konflikt_3 == "2":
    print("\nMedlemmene forstår at de er verdsatt og at de snart er i mål med et verdifult produkt")
    poengsum += 1
else:
    print("\nTeamet mister tillit til Erling og jobber dårligere")
    poengsum -= 1

print("\nErling har nå løst de tre konfliktene.")
if poengsum >= 5:
    print("Hans konflikthåndetring har ført til at teamet jobbet sterkere. Produktet er levert innen fristen og er av høy kvalitet")
elif poengsum < 0:
    print("Produktet blir ikke levert og Erling får sparken")
elif poengsum <= 2:
    print("Hans konflikthåndtering har ført til at teamet jobbet dårligere. Produktet er ikke levert innen fristen")
else:
    print("Hans konflikthåndtering har ført til at teamet jobbet greit. Produktet er levert innen fristen, men kvaliteten kunne vært bedre")
