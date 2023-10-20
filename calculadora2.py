# Caulculadora a prueba de errores

import math

while True:
    print("-----------------")
    print("-------MENÚ-------")
    print(" 1- SUMA")
    print(" 2- RESTA")
    print(" 3- MULTIPICACIÓN")
    print(" 4- DIVISIÓN")
    print(" 5- POTENCIA")
    print(" 6- RAÍZ")
    print(" 7- SALIR")
    print("-----------------")

    entrada = int(input("Qué opción deseas seleccionar?"))

    #DIVISIÓN
    if entrada == 4:
        #Exepciones
        try:
            print("Selecionaste División")
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            resultado = num1 / num2
            print("El resultado es ", resultado)
        except ZeroDivisionError:
            print("Error matemático: no se puede dividir entre cero")
        except ValueError:
            print("Debes ingresar un número")
    
    elif entrada == 5:
        print("Seleccionaste Potencia")
        num1 = int(input("Ingresa el número: "))
        num2 = int(input("Ingresa la potencia: "))
        resultado = num1 ** num2
        print("El resultado de elevar", num1 , "elevado a la" , num2 , "potencia", "es", resultado)
        
        if ValueError:
            print("Debes ingresar un número")

    elif entrada == 6:
         print("Seleccionaste Raíz")
         num1 = int(input("Ingresa el número"))
         resultado = math.sqrt(num1)


    elif entrada == 7:
        print("Saliendo")
        break

print("FIN")