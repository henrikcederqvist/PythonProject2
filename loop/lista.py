user_name = "Frodo"
friends = ["Sam", "Merry", "Pippin"]


print(user_name)
print(friends)

friend_count = len(friends)
print("Antal vänner: " + str(friend_count))

friends.append("Sméagol")
print(friends)

print(friends[-1])
print(friends[3])
print(friends[len(friends)-1])

friends[3] = "Gollum"
print(friends)

friends.remove("Gollum")

print(friends)

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

print( alfabet[0:5:1] )
print( alfabet[:5] )

print( alfabet[::2] )
print( alfabet[12:17] )

data = "10, 12, 22, 8, 15"
print(data)
token_list = data.split(",")
print(data)

sum_so_far = 0
for token in token_list:
    token_number = int( token.strip() )
    sum_so_far = sum_so_far + token_number
print(sum_so_far)

print(data)