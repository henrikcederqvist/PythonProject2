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


#Uppgift 3