films = ["Interstellar", "Gudfadern", "Forrest Gump", "Inception"]
print(films)

films.append("Fellowship of the ring")
print(films)

films.insert(0, "The two towers")
print(films)

position = films.index("Fellowship of the ring")
print("Index för 'Fellowship of the ring' är:", position)

films.remove("Gudfadern")
position = films.index("Fellowship of the ring")
print("Index för 'Fellowship of the ring' är:", position)

films_count = len(films)
print("Antal filmer: " + str(films_count))

reversed_films = films[::-1]
print(reversed_films)

films.sort()
print(films)