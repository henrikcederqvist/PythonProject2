"""Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 25
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Det blir 75 kr totalt. Välkommen åter!
"""

print("Välkommen till Kvittokompis! Avsluta genom att skriva: q")

total = 0  # variabel för summan

while True:
    belopp = input("Skriv in ett belopp: ")

    if belopp.lower() == "q":  # avslutar loopen om användaren skriver quit
        break

    # Konvertera input till ett heltal och lägg till totalen
    total += int(belopp)

print(f"Det blir {total} kr totalt. Välkommen åter!")