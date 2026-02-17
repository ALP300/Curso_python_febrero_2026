'''
Contador de dígitos pares e impares:
Solicita un número entero largo, y con un bucle determina cuántos dígitos son pares y 
cuántos impares
'''
numero= input("Ingresa un número: ") #"hs2838332sdhd7437384"
pares=0
impares=0
#"777777777"
for digito in numero:
    if digito.isdigit():
        if int(digito)%2==0:
            pares+=1
        else:
            impares+=1
print("Dígitos pares: ", pares)
print("Dígitos impares: ", impares)
            