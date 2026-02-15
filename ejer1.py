'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y su asistencia (%).
Si la nota es mayor o igual a 11 y 
la asistencia es mayor o igual al 70%, se aprueba. De 
lo contrario, se desaprueba. 
Además, otorga menciones especiales para notas mayores 
a 17 con asistencia completa. 
'''

nota = float(input("Ingrese nota: "))
asistencia = float(input("Ingrese asistencia: "))

if nota >= 0 and nota <= 20:
    if nota>=11 and asistencia>=70:
        print("Aprobaste")
        if nota >17 and asistencia == 100:
            print("Eres pro")
    else:
        print("Desaprobaste")
else:
    print("Nota invalida")
    

