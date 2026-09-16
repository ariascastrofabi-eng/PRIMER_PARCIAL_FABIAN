def verificar_acceso(usuario,clave):
    if usuario == "estudiante" and clave == "pem2026":
        print(True)
        print("ACCESO CONCEDIDO")
    else:
        print(False)
        print("CREDENCIALES INCORRECTAS")