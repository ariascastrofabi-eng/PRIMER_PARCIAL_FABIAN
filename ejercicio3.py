numero_entero=int(input("INGRESA UN NUMERO ENTERO: "))

if numero_entero < 11 or numero_entero < 0:
    for x in range(1,numero_entero+1):
        print(f"===========TABLA: {x}==========")
        suma=0
        for i in range(1,13):
            resultado=x*i
            print(f"{x} x {i} = {resultado}")

            suma+=resultado
        print(f"suma total de esa tabla {suma}")
else:
    print("debe ser de ese rango")