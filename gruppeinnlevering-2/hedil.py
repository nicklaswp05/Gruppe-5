print("Hei, Erling! Du har fått i oppgave å lede et team."
      " De har forskjellige meninger om hvordan prosjektet \n" 
      "skal gjennomføres, og det er din jobb å finne en løsning \n"
      "som fungerer for alle parter.")
print("Du har tre problemstillinger hvor du har flere valg å velge mellom for å løse dem.")

score_liste = []

print("Første problem: Silje og Elias er uenige. Du må velge mellom å samle hele teamet eller snakke med dem individuelt")
print("1. Samle hele teamet")
print("2. Snakke med dem individuelt")
valg = input("Hva velger du? (1 eller 2): ")

if valg == "1":
    print("Du har valgt å samle hele teamet. Dette kan føre til større polarisering innenfor teamet.")
    score_liste.append(0)
elif valg == "2":
    print("Du har valgt å snakke med dem individuelt. Dette åpner dialog og skaper rom for forståelse og empati.")
    score_liste.append(1)
else:
    print("Ugyldig valg. Vennligst velg 1 eller 2.")
    score_liste.append(0)

print("\nAndre problem: To andre medlemmer er uenige, Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("1. Møte mellom begge parter")
print("2. Vente til de løser det selv")

valg2 = input("Hva velger du? (1 eller 2): ")

if valg2 == "1": 
    print ("Målet med designet avklares og Hamdi og Halgeir forenes under en felles framdriftsplan.")
    score_liste.append(1)
elif valg2 == "2":
    print(" Fremdrift er svekket og prosjektet forsinkes, kvaliteten på det endelige designet påvirkes negativt.") 
    score_liste.append(0)
else:
    print("Ugyldig valg. Vennligst velg 1 eller 2.")
    score_liste.append(0)   


print("\nTredje problem: Motivasjonen blant hele teamet er svekket.")
print("1.Ta alle ut til felles middag.")
print("2. Individuell prat med alle teammedlemmene.")

valg3 = input("Hva velger du? (1 eller 2): ")

if valg3 == "1":
    print("Spenninga svekkes og teamet får en velfortjent feiring av hvor langt de har kommet")
    score_liste.append(1)
elif valg3 == "2":
    print("Bruker for mye tid, og prosjektet forsinkes.")
    score_liste.append(0)
else:
    print("Ugyldig valg. Vennligst velg 1 eller 2.")
    score_liste.append(0)

total_score = sum(score_liste)

print(f"\n--- SLUTTRESULTAT ---")
print(f"Poengliste: {score_liste}")
print(f"Totalt antall poeng: {total_score}")

