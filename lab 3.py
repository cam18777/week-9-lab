# camryn echevarria
# 12/6/2022

# problem 3 is to L loop to show the loop of the numbers that increase by 1

L = []

# sum of values
total = 0

while total < 100:
    # ask the user for a value that will be added to the list
    number = int(input('what number do you want to use?'))
    L.append(number)
    total = sum(L)

print(L)

print(total)
