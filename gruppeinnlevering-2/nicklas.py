#Total verdien som skal hentes til slutt, vil bli populert av poengene beregnet av funksjonen over
score = 0

#Introduksjons meldinger
print()
print ("Hei og velkommen til valg mulighet spillet. Som du vet er det noen konflikter i prosjektet ditt som er nødt til å ryddes opp i før dere kan gå videre.")
print ("Det er det dette programmet er her for å hjelpe deg med!")
print()
print ("Du har 3 forskjellige situasjoner du er nødt til å ta stilling til:")
print ("1. Hvordan skal du håndtere konflikten mellom Silje og Elias?")
print ("2. Hvordan skal du håndtere uenigheten mellom Hamdi og Hallgeir?")
print ("3. Hvordan skal du klare å bevare motivasjonen i teamet ditt?")
print()

#Første valg oppgave
print("Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindreinnovasjon. Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.")
print()
print("Velg én av alternativene, tast 1 eller 2 for valg:")
print("1. Ta et møte med hele teamet.")
print("2. Ta en indviduell samtale med hver av dem.")

#Utregning basert på valg
choice = input("Hvilken velger du?: ")
print()
if choice == ("1"):
    score += 0
    print("Konsekvens: Dette fører til større polarisering innenfor teamet.")
elif choice == ("2"):
    score += 1
    print("Konsekvens: Dette valget åpner dialog og skaper rom for forståelse og empati!")

print()

#Andre valg
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print()
print("Velg én av alternativene, tast 1 eller 2 for valg:")
print("1. Ta et møte med begge partene individuelt.")
print("2. Vente for å se om de løser det på egen hånd.")

choice = input("Hvilken velger du?: ")
print()
if choice == ("1"):
    score += 1
    print("Konsekvens: Målet med designet avklares og Hamdi og Halgeir forenes under en felles framdriftsplan!")
elif choice == ("2"):
    score += 0
    print("Konsekvens: Fremdrift er svekket og prosjektet forsinkes, kvaliteten på det endelige designet påvirkes negativt.")

print()

#Tredje valg
print("Hvordan skal du bevare motivasjonen i teamet som helhet?")
print()
print("Velg én av alternativene, tast 1 eller 2 for valg:")
print("1. Ta med alle i teamet ut på en felles middag.")
print("2. Medarbeider samtale med alle på teamet.")

choice = input("Hvilken velger du?: ")
print()
if choice == ("1"):
    score += 1
    print("Konsekvens: Spenninga svekkes og teamet får en velfortjent feiring av hvor langt de har kommet!")
elif choice == ("2"):
    score += 0
    print("Konsekvens: Bruker for mye tid, og prosjektet forsinkes.")

print()
print("Din totale peongsum ble:", score)
print()

#Forskjellige utfall basert på total poengsum
if score == 3:
    print("Konfliktene ble løst, prosjektet ble levert i tide og alle var fornøyd!")

elif score == 2:
    print("Prosjektet ble ferdig, men møtte ikke forventningene!")

elif score == 1 or score == 0:
    print("Konfliktene eskalerte, og prosjektet ble ikke ferdig i tide!")