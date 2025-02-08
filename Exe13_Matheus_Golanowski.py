#Escreva um programa que solicite um determinado número de dias, em seguida exiba o quanto esses dias equivalem emm horas, minutos, e segundos
dias = int (input("Quantos dias deseja? "))
horas = dias * 24
minutos = dias * 1440
segundos = dias * 86400
print("em horas: ",horas,"\nem minutos:\n",minutos,"em segundos\n",segundos)