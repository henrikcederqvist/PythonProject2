#1a
answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

#1b
answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))
# Svaret ska bli 5050

#1c
answer = 0
i = 1

while i <= 100:
    answer = answer + i
    i = i + 1

print("Summan av talen 1 till 100 är: " + str(answer))