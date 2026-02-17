'''
Suma condicional de múltiplos:
Pide un número N y suma solo los múltiplos de 3 o 5 hasta N. Muestra la suma y los
múltiplos encontrados.
'''
n= int(input("Ingresa el valor de N: ")) #
sumaTotal=0
multiplos=[]

for i in range(1,n+1):
    if i%3==0 or i%5==0:
        sumaTotal+=i
        multiplos.append(i)
    
    
print("Múltiplos encontrados: ", multiplos)
print("Suma total: ", sumaTotal)
    
    