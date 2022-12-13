# camryn echevarria
# 12/6/2022

# problem 4 is the loop that stop at 50

tens = []

# make a while loop that stops at 50
while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
        # add 1 to counter
        counter += 1

    else:

        counter += 1

# print the values of the list
print(tens)
