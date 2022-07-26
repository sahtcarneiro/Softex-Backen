def funcao_calculadora(numero_1, numero_2, operador):
    if (operador == 1):
        resultado = numero_1 + numero_2
    elif (operador == 2):
        resultado = numero_1 - numero_2
    elif (operador == 3):
        resultado = numero_1 * numero_2
    elif (operador == 4):
        resultado = numero_1 / numero_2
    return resultado


print("Bem vindo ao programa Função Calculadora em Loop Infinito!")
print("Quando solicitado digite os valores que deseja calcular")
print("Quando solicitado a operação que deseja fazer, digite:\n 1 para somar\n 2 para subtrarir\n 3 para multiplicar\n 4 para dividir\n 0 para sair")

str_operador = (int(input("Qual operação você deseja fazer? ")))

while (str_operador != 0):
    str_numero_1 = (
        int(input("Digite o primeiro valor a ser usado no calculo: ")))
    str_numero_2 = (
        int(input("Digite o segundo valor a ser usado no calculo: ")))

    resultado_final = funcao_calculadora(
        str_numero_1, str_numero_2, str_operador)

    print("O resultado da sua operação foi: " + str(resultado_final) + "\n")
    str_operador = (int(input("Qual operação você deseja fazer agora? ")))
else:
    print("Você saiu do porgrama!")
