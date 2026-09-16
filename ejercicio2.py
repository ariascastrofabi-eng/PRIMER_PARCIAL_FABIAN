while True:
    print("=============Selecciona un auto===========")
    print("1.Auto")
    print("2.Moto")
    print("3.Camión")
    try:
        opcion=int(input("INGRESA UN NUMERO: "))
        match opcion:
            case 1:
                vehiculo="Auto"
                Tarija_base_por_ahora=10
            case 2:
                vehiculo="Moto"
                Tarija_base_por_ahora=5
            case 3:
                vehiculo="Camión"
                Tarija_base_por_ahora=20
            case _:
                print("no hay mas opcion que 1,2 y 3")
    except ValueError:
        print("INTENTA DENUEVO SIN LETRAS")
        continue
    try:
        horas=int(input("INGRESA CUANTAS HORAS SUPERO: "))

        if horas < 0:
            print("DEBE SUPERAR A 0 HORAS")
        else:    
            if horas > 4:
                print("TIENES RECARGO DE 15%")
                Tarija=Tarija_base_por_ahora * horas
                recargo=Tarija*0.15
                total_pagar=Tarija+recargo
                print(f"Vehiculo: {vehiculo}")
                print(f"TARIJA DE HORAS: {Tarija}BS")
                print(f"TIENE UN RECARGO {recargo} BS")
                print(f"TOTAL A PAGAR {total_pagar}")
            else:
                print("NO TIENE RECARGO")
                Tarija=Tarija_base_por_ahora * horas
                print(f"Vehiculo: {vehiculo}")
                print(f"TARIJA DE HORAS: {Tarija}BS")
                print(f"TOTAL A PAGAR {Tarija} BS")
    except ValueError:
        print("INTENTA DENUEVO SIN LETRAS")
        continue
