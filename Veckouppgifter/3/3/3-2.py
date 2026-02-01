print("Välkommen till Kvittokompis! Avsluta genom att skriva: q")

total = 0  # variabel för summan

while True:
    belopp = input("Skriv in ett belopp: ")

    if belopp.lower() == "q":  # avslutar loopen om användaren skriver quit
        break

    # Konvertera input till ett heltal och lägg till totalen
    total += int(belopp)

print(f"Det blir {total} kr totalt. Välkommen åter!")

antal = int(input("Hur många är ni?: "))
print("Ni är " + str(antal) + " st.")

kr_person = total / antal

print("Det blir " + str(total) + " kr totalt, alltså " + str(kr_person) + " kr per person. Välkommen åter!")

#Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

