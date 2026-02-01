todo_list = []

print("** Todo list extravaganza **")

while True:
    print("1. Se innehållet i din lista")
    print("2. Lägga till nya punkter i din lista")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        if len(todo_list) == 0:
            print("Din lista är tom")
        else:
            for item in todo_list:
                print("+", item.capitalize())
        print(".")

    elif choice == "2":
        new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        todo_list.append(new_item)
        print(f'Ok, lade till "{new_item}" i listan.')
        print(".")

    else:
        print("Välj 1 eller 2.")