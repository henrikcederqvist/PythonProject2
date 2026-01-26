"""

4 Temperaturomvandling
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:

Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.

Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. Använd sedan if + else.

Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

Formel för konvertering mellan temperaturenheter:
C = (F - 32) / 1.8
F = 1.8 * C + 32

Förslag på värden att testa med:

° Celsius
° Fahrenheit
0
32
-17.777…
0
37.777…
100
100
212
"""
celsius = float(input("Skriv in en temperatur i grader Celsius:"))
fahrenheit = (celsius * 1.8) + 32

print("Det blir",fahrenheit,"grader Fahrenheit.")

--------------------------------------------------

gradtyp = str(input("Skriv in vilken gradtyp i Celsius (C) eller F (F) du vill ha gradantalet:"))

if gradtyp == "F":
    print("Du har angett Fahrenheit")

elif gradtyp == "C":
    print("Du har angett Celsius")

celsius = float(input("Skriv in en temperatur i grader Celsius:"))
fahrenheit = (celsius * 1.8) + 32

if gradtyp == "F":
    print("Det blir",fahrenheit,"grader Fahrenheit.")

elif gradtyp == "C":
    print("Det blir", celsius, "grader Celsius.")


if celsius < 10:
    print("Ta på dig vinterkläder!")
elif celsius >= 20:
    print("Packa badkläder!️")
else:
    print("Lagom temperatur!")