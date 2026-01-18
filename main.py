#Veckouppgift 1

#Uppgift 1

username = "Henrik"

print("Hello world")
print("This program was made by " + username)


#Uppgift 2

biljettpriset = input("Ge mig biljettpriset: ")
fickpengarpriset = input("Ge mig fickpengarpriset: ")
biljettpriset_int = int(biljettpriset)
fickpengarpriset_int = int(fickpengarpriset)
pengar_kvar = (fickpengarpriset_int -biljettpriset_int)
pengar_kvar_att_dela_på = pengar_kvar/2

print("Det blir " + str(pengar_kvar) + " kronor över.")
print("Varje person får " + str(pengar_kvar_att_dela_på))


x = 100 # biljettpris
y = 200 # pengar på fickan
print("Det blir " + str(y - x) + " kronor över.")
z = (y - x)/ 2
print("Varje person får " + str(z))

#Uppgift 3

#1a

tal = input("Ge mig ett tal: ")
tal_int = int(tal)
print("Du skrev detta tal: " + str(tal_int))

#1b

tal2 = input("Ge mig ett annat tal: ")
tal2_int = int(tal2)

sum_tal_tal2 = (tal_int + tal2_int)

print("Summan av talen blir: " + str(sum_tal_tal2))

#2a-b

pris_jacka = input("Ge mig pris för jackan: ")
rea_jacka = input("Ge mig reapriset på jackan: ")
pris_jacka_int = int(pris_jacka)
rea_jacka_float = float(rea_jacka)
rabatt = (pris_jacka_int * rea_jacka_float) / 100
slutpris = pris_jacka_int - rabatt

print("Rabatten är: " + str(rabatt))

print("Slutpriset blir: " + str(slutpris))

#Uppgift 4
#1a

#1a Det är ca 470 km mellan Stockholm och Göteborg.
#Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
#Du behöver fråga användaren hur fort man ska köra, i km/h.
#Svara i timmar.
