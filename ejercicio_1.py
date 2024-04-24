#1.	Realizar un programa que lea los tiempos en los que de 10 corredores han acabado una carrera. El programa debe determinar qué corredores tienen el primer, segundo y último puesto, así como cuál es el tiempo medio en que se ha corrido la carrera.

tiempos = []
for i in range(0,10,1):
    tiempo = float(input(f"Ingrese el tiempo del corredor {i+1}: "))
    tiempos.append(tiempo)

tiempos.sort()

primer_lugar = tiempos[0]
segundo_lugar = tiempos[1]
ultimo_lugar = tiempos[-1]


promedio = sum(tiempos)/len(tiempos)


print(f"El primer lugar es para el corredor con tiempo de {primer_lugar}") 
print(f"El segundo lugar es para el corredor con tiempo de {segundo_lugar}")
print(f"El último lugar es para el corredor con tiempo de {ultimo_lugar}") 
print(f"El tiempo promedio de la carrera es de {promedio}") 