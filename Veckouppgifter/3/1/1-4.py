x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y   #Tips: sätt en brytpunkt här
        break
    else:
        x += y * y  # och här
        break
    y += 1