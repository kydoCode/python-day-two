endNumber = int(input("Saisissez un nb entier : "))
startNumber = 1

print("Les nb pairs jusqu'à", endNumber, "sont : ")

while  startNumber <= endNumber:
    startNumber += 1
    if startNumber % 2 != 0:
        continue
    print(startNumber)