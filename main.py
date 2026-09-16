from validador import verificar_acceso
try:
    usuario=input("INGRESA EL USUARIO CORRECTO: ").strip()
    clave=input("INGRESA LA CLAVE CORRECTA: ").strip()
    verificar_acceso(usuario,clave)
except ValueError:
    print("INTENTA DENUEVO")
