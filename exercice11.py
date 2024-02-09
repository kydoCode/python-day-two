inputUser = input("Saisir un nombre entier positif : ")

def somme_chiffres(number):
   # number_str = str(number)
    number_sum = 0
    for i in number:
        number_sum += int(i)
    print(number_sum)

somme_chiffres(inputUser)
# computeInput = somme_chiffres(inputUser)
# print(computeInput)