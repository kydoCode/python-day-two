# nombre de termes
iterateAmount = int(input("Combien de termes ? :"))
# firstNumber = int(input("Valeur de départ ?"))

def fibonacci(n): #, startValue
    # n = n-2 + n-1
    # startValue = (startValue-2) + (startValue-1)
    firstTerms = "0, 1"
    n_output: str = ""


    for element in range(2, n+2, 1):
            n = n-1 + n-2
            n_output += str(n) + ", "                                      #, startValue
    print(n)
    print(n_output)
        # print(startValue)
        # startValue += (startValue-2) + (startValue-1)
    
# fibonacci(iterateAmount, firstNumber)

fibonacci(iterateAmount)    

