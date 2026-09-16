while True:
    numero=int(input("INGRESA UN NUMERO: "))
    a=0
    b=1
    if numero <= 0:
        print("error")
    else:
        for i in range(numero):
            print(a)
            c=a+b
            a=b
            b=c
        break
