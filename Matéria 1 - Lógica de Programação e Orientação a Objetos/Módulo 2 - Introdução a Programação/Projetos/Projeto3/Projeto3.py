import time

print("Olá, seja bem vindo(a) ao código bomba!")
ativacao_bomba = input("Você deseja ativar a bomba? ")

if (ativacao_bomba == "sim" or ativacao_bomba == "Sim"):
    print("Contagem regressiva iniciada!")
    print("Segundos restantes até a explosão: ")
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("BUM!")
else:
    print("Você decidiu não ativar a bomba!")
