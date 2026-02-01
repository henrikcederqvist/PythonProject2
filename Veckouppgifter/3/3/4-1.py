figurer = ["a","b","c","d","e","f","g","h","i","j"]

for figur in figurer:
    print("\nFigur", figur)

    for y in range(6):
        s = ""
        for x in range(8):

            # a: lodrät linje till vänster
            if figur == "a":
                if x == 0:
                    s += "#"
                else:
                    s += "."

            # b: diagonal
            elif figur == "b":
                if x == y:
                    s += "#"
                else:
                    s += "."

            # c: block i mitten
            elif figur == "c":
                if 2 <= x <= 4:
                    s += "#"
                else:
                    s += "."

            # d: kors
            elif figur == "d":
                if x == 3 or y == 2:
                    s += "#"
                else:
                    s += "."

            # e: zig-zag
            elif figur == "e":
                if (x + y) % 2 == 0:
                    s += "#"
                else:
                    s += "."

            # f: två lodräta linjer
            elif figur == "f":
                if x == 0 or x == 4:
                    s += "#"
                else:
                    s += "."

            # g–j (exempel – samma princip)
            elif figur == "g":
                if x % 2 == 0:
                    s += "#"
                else:
                    s += "."

            elif figur == "h":
                if y == 0 or y == 5 or x == 0 or x == 7:
                    s += "#"
                else:
                    s += "."

            elif figur == "i":
                if x == 3:
                    s += "#"
                else:
                    s += "."

            elif figur == "j":
                if y == 5 or x == 4:
                    s += "#"
                else:
                    s += "."

        print(s)