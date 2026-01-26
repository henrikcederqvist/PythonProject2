"""

5 Miniräknare
1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)

2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.

3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)

För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

t1
t2
t3
Störst
Två lika?
Tre lika?
Mellerst?
1
2
3
3
nej
nej
2



"""
"""
tal1 = input("Ge mig tal 1: ")
tal1_int = int(tal1)

tal2 = input("Ge mig tal 2: ")
tal2_int = int(tal2)

tal3 = input("Ge mig tal 3: ")
tal3_int = int(tal3)


sum_tal123 = (tal1_int + tal2_int + tal3_int)

print("Summan av talen blir: " + str(sum_tal123))

if tal1 >= tal2 and tal1 >= tal3:
    storsta = tal1
elif tal2 >= tal1 and tal2 >= tal3:
    storsta = tal2
else:
    storsta = tal3

print("Det största talet är: ", storsta)


if tal1 == tal2 == tal3:
    print("Alla tre talen är lika!")

# Kolla om två av talen är lika
elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
    print("Två av talen är lika!")

else:
    print("Inga tal är lika.")



# Alla tre är olika
elif tal1 != tal2 and tal1 != tal3 and tal2 != tal3:

    # Det mellersta talet är det som inte är störst eller minst
    storsta = tal1
    minsta = tal1

    # Hitta största
    if tal2 > storsta:
        storsta = tal2
    if tal3 > storsta:
        storsta = tal3

    # Hitta minsta
    if tal2 < minsta:
        minsta = tal2
    if tal3 < minsta:
        minsta = tal3

    # Det mellersta = summan av alla - största - minsta
    mellersta = tal1 + tal2 + tal3 - storsta - minsta
    print(f"Det mellersta talet är {mellersta}.")

# Annars finns inget mellersta
else:
    print("Det finns inget mellersta tal enligt uppgiftens regler.")


"""

# Läs in tre tal
tal1 = int(input("Ge mig tal 1: "))
tal2 = int(input("Ge mig tal 2: "))
tal3 = int(input("Ge mig tal 3: "))

# 1. Summan
summa = tal1 + tal2 + tal3
print(f"Summan av talen blir: {summa}")

# 2. Största talet
if tal1 >= tal2 and tal1 >= tal3:
    storsta = tal1
elif tal2 >= tal1 and tal2 >= tal3:
    storsta = tal2
else:
    storsta = tal3
print(f"Det största talet är: {storsta}")

# 3. Kolla lika tal
if tal1 == tal2 == tal3:
    print("Alla tre talen är lika!")
elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
    print("Två av talen är lika!")
else:
    print("Inga tal är lika.")

# 4. Mellersta talet
if tal1 == tal2 == tal3:
    print(f"Det mellersta talet är {tal1}.")
elif tal1 != tal2 and tal1 != tal3 and tal2 != tal3:
    # Hitta största och minsta
    storsta = tal1
    minsta = tal1
    if tal2 > storsta:
        storsta = tal2
    if tal3 > storsta:
        storsta = tal3
    if tal2 < minsta:
        minsta = tal2
    if tal3 < minsta:
        minsta = tal3
    # Mellersta = summan - största - minsta
    mellersta = tal1 + tal2 + tal3 - storsta - minsta
    print(f"Det mellersta talet är {mellersta}.")
else:
    print("Det finns inget mellersta tal enligt uppgiftens regler.")