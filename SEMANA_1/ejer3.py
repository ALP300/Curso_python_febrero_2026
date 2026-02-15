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
#usuario: Leo1234  contraseña= 1234
usuario= input("Usuario: ")
contra= input("Contraseña: ")
rol= input("Rol (admin/editor/visitante): ").lower()
#Admin - admin/ editor / visitante
#VISITANTE - visitante

if usuario=="Leo1234" and contra=="1234":
    if rol=="admin":
        print("Acceso total!")
    elif rol == "editor":
        print("Acesso a editar")
    elif rol== "visitante":
        print("Acceso de visitante")
    else:
        print("Rol no válido")
else:
    print("Credenciales incorrectas")
    