todo_list = []

print("** Todo list extravaganza **")

while True:
    print("1. Se innehållet i din lista")
    print("2. Lägga till nya punkter i din lista")
    print("3. Markera som klar")

    choice = input("Välj ett alternativ: ")

    # 1. Visa listan
    if choice == "1":
        if len(todo_list) == 0:
            print("Din lista är tom")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
        print(".")

    # 2. Lägg till punkt
    elif choice == "2":
        new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        todo_list.append(new_item)
        print(f'Ok, lade till "{new_item}" i listan.')
        print(".")

    # 3. Markera som klar (ta bort)
    elif choice == "3":
        if len(todo_list) == 0:
            print("Listan är tom, inget att markera som klart.")
        else:
            print("Vilken grej är du färdig med?")
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")

            done = int(input("Skriv numret: "))
            finished = todo_list.pop(done - 1)
            print(f'Bra jobbat! Tog bort "{finished}" från listan.')
        print(".")

    else:
        print("Välj 1, 2 eller 3.")