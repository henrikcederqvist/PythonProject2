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

#2a

2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea och kostar 75% av originalpriset. Skriv ett program som räknar ut hur mycket du behöver betala. Använd variabeln:  rea_procent = 75.0
Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.


