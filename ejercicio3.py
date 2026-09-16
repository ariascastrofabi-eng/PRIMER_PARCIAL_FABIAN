numero_entero=int(input("INGRESA UN NUMERO ENTERO: "))

if numero_entero < 11 or numero_entero < 0:
    for x in range(1,numero_entero+1):
        print(f"===========TABLA: {x}==========")
        for i in range(1,13):
            print(f"{x} x {i} = {x*i}")
else:
    print("debe ser de ese rango")