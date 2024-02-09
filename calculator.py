# EXERCICE 10

a = int(input("Première valeur : "))
b = int(input("Seconde valeur : "))
computeRequest = str(input("Opération ? +: Addition | -: Soustraction | *: Multiplication |/: Division | %: Reste "))
print("Choix utilisateur est", computeRequest)

# Addition
def add_values(firstValue, secondValue):
    print(firstValue + secondValue)

# Soustraction
def sub_values(firstValue, secondValue):
    print(firstValue - secondValue)

# Multiplication
def multiply_values(firstValue, secondValue):
    print(firstValue * secondValue)

# Division
def divide_values(firstValue, secondValue):
    print(firstValue / secondValue)

# Reste
def modulo_values(firstValue, secondValue):
    print(firstValue % secondValue)


if computeRequest == "+":
    compute_user = add_values(a, b)
elif computeRequest == "-":
    compute_user= sub_values(a, b)
elif computeRequest == "*":
    compute_user = multiply_values(a, b)
elif computeRequest == "/":
    compute_user = divide_values(a, b)
elif computeRequest == "%":
    compute_user = modulo_values(a, b)
else:
    print("Error occured, check your input")
