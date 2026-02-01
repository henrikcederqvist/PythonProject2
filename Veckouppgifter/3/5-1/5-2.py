import random

secret = random.randint(1, 100)

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

guesses = 0

while True:
    guess = int(input("Gissa: "))
    guesses += 1

    if guess == secret:
        print(f"Det är rätt!! Du gjorde det på {guesses} gissningar.")
        break

    # nära-kontroll (max 5 ifrån)
    if abs(guess - secret) <= 5:
        print("🔥 Nu börjar det brännas!")

    if guess < secret:
        print("Nej, det är för lågt!")
    else:
        print("Nej, det är för högt!")