data = "1, -2, 3, -2, 4, -3"
print(data)
token_list = data.split(",")
print(data)

sum_so_far = 0
for token in token_list:
    token_number = int( token.strip() )
    sum_so_far = sum_so_far + token_number
print(sum_so_far)

