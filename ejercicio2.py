
'''
Validación de acceso: 
Solicita usuario, contraseña y rol (admin, editor, visitante). 
Verifica si las credenciales 
son válidas y muestra los permisos disponibles según el rol. 
Usa múltiples condicionales 
y lógica anidada. 

Leonardo== LEONARDO

.lower()
'''
usu = input("Ingrese su usuario: ").lower()
contra = input("Ingrese su contraseña: ")


if usu == "pinina" and contra == "123":
    rol = input("Ingrese su rol: ").lower()
    if rol == "admin":
        print("Acceso completo")
    elif rol == "editor":
        print("Permisos de editor")
    elif rol == "visitante":
        print("Peermisos de visitante")
    else:
        print("Rol incorrecto")
else:
    print("credenciales erroneas")