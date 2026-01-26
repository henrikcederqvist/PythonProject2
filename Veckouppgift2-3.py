"""3 Sportresultat
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:

Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

Kom ihåg att göra code review!

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

"""

print("Matchen är över, nu ska vi räkna ut resultatet!")

tottenham = int(input("Hur många mål gjorde Tottenham?: "))
liverpool = int(input("Hur många mål gjorde Liverpool?: "))

if tottenham > liverpool:
    diff = tottenham - liverpool
    print("Tottenham vann med ", diff, "mål")

elif tottenham < liverpool:
    diff = liverpool - tottenham
    print("Liverpool vann med", diff, "mål")

else:
    print("Det blev lika!")