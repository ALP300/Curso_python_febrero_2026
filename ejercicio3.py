

anio = int(input("Ingresa tu año de nacimiento: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Tu año de nacimiento es bisiesto.")
else:
    print("Tu año de nacimiento no es bisiesto.")


anio_actual = 2026
edad = anio_actual - anio
print("Tu edad es:", edad)

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
