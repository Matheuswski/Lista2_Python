#Escreva um programa que pergunte quantos pedaço o bolo tem, em seguida pergunte ao usuario quantos pedaço ele comeu, calcule quantos pedaços ainda tem e exiba o resultado com uma mensagem de livre escolha.
bolo = int (input("quantos pedaços tem o bolo? "))
pedaços = int (input("quantos pedaços voce comeu? "))

resultado = bolo - pedaços
print("dos" , bolo, "pedaços voce comeu" , pedaços, "pedaços, sobrou no total:", resultado,"pedaços")