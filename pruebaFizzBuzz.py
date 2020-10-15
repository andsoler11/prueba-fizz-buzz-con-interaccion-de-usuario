numeroMax = int(input("escribe la cantidad de numeros que quieres que se impriman, los divisbles en 3 saldran fizz y los divisibles en 5 saldran buzz, y si son divisibles entre 3 y 5 saldran fizz, buzz. "))
numeros = 0

while numeros < numeroMax:
    numeros += 1
    if numeros % 3 == 0 and numeros % 5 == 0:
        print('fizz, buzz')
    elif numeros % 3 == 0:
        print("fizz")
    elif numeros % 5 == 0:
        print('buzz')
    else:
        print(numeros)

 



