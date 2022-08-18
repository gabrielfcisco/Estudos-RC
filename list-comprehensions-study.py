a = ["pin-pan" if el % 2 == 0 and el % 3 == 0 
     else "pin" if el % 2 == 0 
     else "pan" if el % 3 == 0 
     else el for el in range(1, 101)]

print(a)