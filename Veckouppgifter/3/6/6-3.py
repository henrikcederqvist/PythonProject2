todo_list = []
done_list = []

print("** Todo list extravaganza **")

while True:
    print("1. Se innehållet i din todo-lista")
    print("2. Lägg till ny punkt")
    print("3. Markera som klar")
    print("4. Se avklarade grejer")
    print("5. Lägg tillbaka grej till todo-listan")

    choice = input("Välj ett alternativ: ")

    # 1. Visa todolistan
    if choice == "1":
        if len(todo_list) == 0:
            print("Din lista är tom")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
        print(".")

    # 2. Lägg till
    elif choice == "2":
        new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        todo_list.append(new_item)
        print(f'Ok, lade till "{new_item}" i listan.')
        print(".")

    # 3. Markera som klar (flytta till done_list)
    elif choice == "3":
        if len(todo_list) == 0:
            print("Inga grejer att markera som klara.")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")

            done = int(input("Vilken grej är klar? (nummer): "))
            finished = todo_list.pop(done - 1)
            done_list.append(finished)
            print(f'Bra jobbat! "{finished}" är nu klar.')
        print(".")

    # 4. Visa avklarade grejer
    elif choice == "4":
        if len(done_list) == 0:
            print("Inga avklarade grejer ännu.")
        else:
            for i, item in enumerate(done_list, start=1):
                print(f"{i}. {item}")
        print(".")

    # 5. Lägg tillbaka till todolistan
    elif choice == "5":
        if len(done_list) == 0:
            print("Inga grejer att lägga tillbaka.")
        else:
            for i, item in enumerate(done_list, start=1):
                print(f"{i}. {item}")

            back = int(input("Vilken grej vill du lägga tillbaka? (nummer): "))
            item_back = done_list.pop(back - 1)
            todo_list.append(item_back)
            print(f'"{item_back}" är tillbaka i todo-listan.')
        print(".")

    else:
        print("Välj ett alternativ mellan 1 och 5.")