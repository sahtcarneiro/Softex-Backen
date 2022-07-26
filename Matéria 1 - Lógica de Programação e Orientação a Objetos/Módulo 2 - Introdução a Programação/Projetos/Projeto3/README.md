# Projeto 3 / Módulo 2 / Matéria 1

Autor: Jonathas Carneiro

## Instrução do Projeto

Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.

Não é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, você pode usar a função time.sleep() que existe na Python (acesse o link em anexo). No entanto, é preciso adicionar uma biblioteca antes de executá-la.

<a href="https://realpython.com/python-sleep/"> Link em Anexo </a>

## Resolução do Projeto

Além de seguir abaixo também se encontra num arquivo .py nesta mesma pasta.

import time <br> <br>

print("Olá, seja bem vindo(a) ao código bomba!") <br>
ativacao_bomba = input("Você deseja ativar a bomba? ") <br> <br>

if (ativacao_bomba == "sim" or ativacao_bomba == "Sim"): <br>
print("Contagem regressiva iniciada!") <br>
print("Segundos restantes até a explosão: ") <br>
for i in range(10, 0, -1): <br>
print(i) <br>
time.sleep(1) <br>
print("BUM!") <br>
else: <br>
print("Você decidiu não ativar a bomba!")
