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

#programmet ska fråga hur många procent dricks man vill lägga på.
# Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

dricks_input = input("Hur många procent dricks vill ni lägga på? (tryck Enter för 10%): ")

if dricks_input == "":
    dricks_procent = 10
else:
    dricks_procent = int(dricks_input)

dricks = total * (dricks_procent / 100)
total_med_dricks = total + dricks
kr_person = total_med_dricks / antal

print(f"Dricks: {dricks} kr")
print(f"Totalt med dricks: {total_med_dricks} kr")
print(f"Det blir {kr_person} kr per person. Välkommen åter!")