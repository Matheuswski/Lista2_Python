#Escreva um programa que peça ao usuario para inserir TRÊS numeros inteiros, some os DOIS primeiros e multiplique esse total pelo TERCEIRO. Exiba pm resutado da operação com a seguinte mensagem: "O total é:[?]".
num1 = int (input("Insira o primeiro numero: "))
num2 = int (input("Insira o segundo numero: "))
num3 = int (input("Insira o terceiro numero: "))
cont = num3 * (num1 + num2)
print("o total deu: ", cont)