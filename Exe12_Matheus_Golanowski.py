#Escreva um programa que pergunta o valor da conta em seguida pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem("cada cliente deve pagar: x valor")

conta = int (input ("Qual o valor total da conta? "))
pessoa = int (input ("Quantos clientes no total " ))
print ("Cada cliete deve pagar: ",conta/pessoa,"R$")