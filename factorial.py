from io import open

archivo_texto=open("factorial.txt","a")

seguir = True
while seguir == True:
    try:
        def factorial(n):
            if n==0:
                return 1
            else:
                return n * factorial(n-1)
        n = int(input("Ingrese un numero: "))
        print("El factorial de " + str(n) + " es: " + str(factorial(n)))
        archivo_texto.write("El factorial de " + str(n) + " es: " + str(factorial(n)) + "\n")

        op = int(input("Desea continuar? 1.Si 2.No \n"))
        if (op == 1):
            seguir=True
        else:
            seguir=False
            print("Programa terminado")
    except ValueError as i:
        print("Caracter no permitido")

archivo_texto.close()

