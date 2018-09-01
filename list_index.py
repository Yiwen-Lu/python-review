squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(squares[::2])    # [0, 4, 16, 36, 64]
print(squares[1::4])   # [1, 25, 81]
print(squares[::-1])   # reverse the list !!!
print(squares[2:8:3])  # [4, 25]
print(squares[7:5:-1]) # [49, 36]
