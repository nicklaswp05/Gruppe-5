# Interaktiv historie: Erling og stormen i prosjektteamet
# IS-118, Gruppeoppgave 2, del 2
# Kjør med: python mahoor.py


def les_valg(spørsmål):
    """Spør til brukeren svarer A eller B, og returnerer valget."""
    while True:
        svar = input(spørsmål).strip().upper()
        if svar in ("A", "B"):
            return svar
        print("Ugyldig valg. Skriv A eller B.\n")


# Variabler som lagrer valgene og poengsummen
valg1 = ""
valg2 = ""
valg3 = ""
poeng = 0

# ----------------------------------------------------
# Introduksjon
# ----------------------------------------------------
print("=" * 60)
print(" ERLING OG STORMEN")
print("=" * 60)
print("""
Du er Erling, prosjektleder i et team som utvikler en digital 
medborgerportal. Teamet er midt i storming fasen, og flere 
konflikter truer med å stoppe prosjektet.

Hva bør Erling gjøre?
""")

# ----------------------------------------------------
# Beslutningspunkt 1: Silje og Elias sin uenighet
# ----------------------------------------------------
print("-" * 60)
print("DEL 1: Silje og Elias sin uenighet")
print("-" * 60)
print("""
A) Ta et møte med hele teamet.
B) Ta en individuell samtale med begge parter og prosjektleder.
""")
valg1 = les_valg("Hva velger Erling? (A/B): ")

if valg1 == "A":
    # 0 poeng
    print("\nKonsekvens: Det blir større polarisering innenfor teamet.")
else:
    poeng += 1
    print("\nKonsekvens: Det åpner dialog og skaper rom for forståelse og empati.")

# ----------------------------------------------------
# Beslutningspunkt 2: Hamdi og Hallgeir
# ----------------------------------------------------
print()
print("-" * 60)
print("DEL 2: Det ulmer en konflikt mellom Hamdi og Hallgeir")
print("-" * 60)
print("""
A) Ta et møte mellom begge parter og Erling.
B) Vente til de løser det selv.
""")
valg2 = les_valg("Hva velger Erling? (A/B): ")

if valg2 == "A":
    poeng += 1
    print("\nKonsekvens: Målet med designet avklares, og Hamdi og Hallgeir")
    print("forenes under en felles framdriftsplan.")
else:
    poeng += 0
    print("\nKonsekvens: Framdriften reduseres og prosjektet forsinkes.")
    print("Kvaliteten på det endelige designet påvirkes negativt.")

# ----------------------------------------------------
# Beslutningspunkt 3: Motivasjon
# ----------------------------------------------------
print()
print("-" * 60)
print("DEL 3: Motivasjonen i teamet")
print("-" * 60)
print("""
A) Ta alle ut til felles middag.
B) Ta en individuell samtale med alle teammedlemmene.
""")
valg3 = les_valg("Hva velger Erling? (A/B): ")

if valg3 == "A":
    poeng += 1
    print("\nKonsekvens: Spenningen reduseres, og teamet får en velfortjent")
    print("feiring av hvor langt de har kommet.")
else:
    poeng += 0
    print("\nKonsekvens: Det går med for mye tid, og prosjektet forsinkes.")

# ----------------------------------------------------
# Utfall basert på samlet poengsum
# ----------------------------------------------------
print()
print("=" * 60)
print(" UTFALL")
print("=" * 60)

if poeng == 3:
    print("\nKonfliktene ble løst, prosjektet ble levert i tide")
    print("og alle var fornøyd.")
elif poeng == 2:
    print("\nProsjektet ble ferdig, men møtte ikke forventningene.")
else:
    print("\nKonflikten eskalerte, og prosjektet ble ikke ferdig i tide.")

print("\nDine valg: " + valg1 + ", " + valg2 + ", " + valg3)
print("Samlet poengsum: " + str(poeng))
print("\nTakk for at du spilte!")  
