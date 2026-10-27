def introduksjon():
    print("========================================")
    print("      VELKOMMEN TIL PROSJEKTLEDERSPILLET")
    print("========================================\n")

    print("I dette spillet skal du være prosjektleder Erling og lede prosjektet gjennom konflikter.")
    print("Prosjektet ditt er inne i stormingfasen, og du kommer til å møte tre utfordringer.")
    print("Du kommer til å møte 3 hovedutfordringer som du må ta valg i.")
    print("Disse valgene vil påvirke prosjektets sluttresultat og teamets trivsel.")
    print("\nLykke til!\n")


def besluttningspunkt_1():

    print("\n========================================")
    print("         BESLUTNINGSPUNKT 1")
    print("========================================\n")

    print("Det har oppstått en uenighet mellom Silje som er UX/UI-designer.")
    print("Hun er fokusert på brukervennlighet og visuell kvalitet.")
    print("Elias er IT-rådgiver fra kommunens IT-avdeling og er opptatt av teknisk sikkerhet og kostnadskontroll.")
    print("Denne konflikten har utviklet seg fra en sakskonflikt til en personkonflikt.\n")

    print("SOM PROSJEKTLEDER VELGER DU Å:\n")
    print("A. Fasilitere et felles møte med hele teamet.")
    print("B. Fasilitere et arbeidsmøte med bare Silje og Elias.\n")

    valg = input("Velg A eller B: ").strip().upper()

    if valg == "A":
        print("\nErling samler hele teamet.")
        return 0
    else:
        print("\nErling velger individuelle samtaler.")
        return 1


def besluttningspunkt_2():

    print("\n========================================")
    print("         BESLUTNINGSPUNKT 2")
    print("========================================\n")

    print("Det er en ulmende konflikt mellom Hamdi fra kulturavdelingen og Hallgeir som er brukerrepresentant.")
    print("De har uenighet om hvordan innbyggerne skal kunne delta i digitale folkemøter.\n")

    print("SOM PROSJEKTLEDER VELGER DU Å:\n")
    print("A. Holde et møte mellom begge parter og deg som prosjektleder.")
    print("B. Vente til de løser konflikten selv.\n")

    valg = input("Velg A eller B: ").strip().upper()

    if valg == "A":
        print("\nMøte mellom begge parter og prosjektleder.")
        return 1
    else:
        print("\nVenter til de løser konflikten selv.")
        return 0


def besluttningspunkt_3():

    print("\n========================================")
    print("         BESLUTNINGSPUNKT 3")
    print("========================================\n")

    print("Motivasjonen i teamet er synkende.")
    print("Hvordan vil du som prosjektleder bevare motivasjonen til teamet?\n")

    print("SOM PROSJEKTLEDER VELGER DU Å:\n")
    print("A. Ta alle ut til en felles middag.")
    print("B. Ha en individuell prat med alle teammedlemmene for å motivere dem.\n")

    valg = input("Velg A eller B: ").strip().upper()

    if valg == "A":
        print("\nTar alle ut til en felles middag.")
        return 1
    else:
        print("\nHar individuelle samtaler med teammedlemmene.")
        return 0


def avslutning(poeng):

    print("\n========================================")
    print("            SLUTTRESULTAT")
    print("========================================\n")

    print("Takk for at du spilte prosjektlederspillet!\n")

    if poeng == 3:
        print("Gratulerer!")
        print("Du har håndtert konfliktene på en utmerket måte.")
        print("Prosjektet ble levert i tide og alle var fornøyde.")

    elif poeng == 2:
        print("Bra jobbet!")
        print("Du har håndtert konfliktene godt.")
        print("Prosjektet ble ferdig i tide, men møtte ikke alle forventningene.")

    else:
        print("Konfliktene eskalerte.")
        print("Prosjektet ble ikke ferdig i tide.")


poeng = 0

introduksjon()

poeng += besluttningspunkt_1()
poeng += besluttningspunkt_2()
poeng += besluttningspunkt_3()

avslutning(poeng)
