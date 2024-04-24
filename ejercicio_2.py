#2.	Realiza un programa que vaya pidiendo números enteros mientras que no se introduzca el cero y rellene dos vectores, uno con los números pares, y otro con los números impares. Al final, se debe mostrar por pantalla tanto el vector de números pares como el de impares.

par = []
impar = []

while True:
    numero = int(input("Ingrese un número entero: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
        
print(f"Los números pares son: {par}")
print(f"Los números impares son: {impar}") 
