print("Olá, bem vindo ao programa de votação, aqui você poderá votar várias vezes em diferentes candidatos ou em branco, caso digite um número diferente das opções este contará como voto nulo!\nAo final de cada votação você poderá escolher continuar votando ou encerrar a votação, caso opte por encerrar será apresentado o resultado final da votação, com o vencedor e quantos votos cada um recebeu.\nEspero que goste da experiência\n")

candidato_x = 0
candidato_y = 0
candidato_z = 0
branco = 0
nulo = 0
votar = "sim"

while (votar == "sim" or votar == "Sim" or votar == "SIM"):

    try:
        voto = int(input("Para votar no candidato X digite 889\nPara votar no candidato Y digite 847\nPara votar no candito Z digite 515\nPara votar em Branco digite 0\nDigite o seu voto: "))
        if (type(voto) == int):
            if (voto == 889):
                candidato_x += 1
            elif (voto == 847):
                candidato_y += 1
            elif (voto == 515):
                candidato_z += 1
            elif (voto == 0):
                branco += 1
            else:
                nulo += 1
        votar = input("Você deseja continuar votando? ")

    except Exception as err:
        print("Ocorreu um erro:\nTente digitar apenas números para contabilizar um voto válido!")
        votar = input("Você deseja tentar votar mais um vez? ")

    if (votar == "sim" or votar == "Sim" or votar == "SIM"):
        continue
    else:
        print("Você decidiu encerrar a votação!\nVeja o resultado:\n")
        break

if (candidato_x > candidato_y and candidato_x > candidato_z):
    print("O vencedor desta votação foi o candidato X")
elif (candidato_y > candidato_x and candidato_y > candidato_z):
    print("O vencedor desta votação foi o candidato Y")
elif (candidato_z > candidato_x and candidato_z > candidato_y):
    print("O vencedor desta votação foi o candidato Z")
else:
    print("Nesta votação não houve vencedores.")

print("O candidato X teve " + str(candidato_x) + " votos.")
print("O candidato Y teve " + str(candidato_y) + " votos.")
print("O candidato Z teve " + str(candidato_z) + " votos.")
print("Houveram " + str(branco) + " votos em branco.")
print("Houveram " + str(nulo) + " votos nulos.")
