def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print(alist)


print("Olá, seja bem vindo ao programa de ordenação utilizando o metódo bubble sort!\nEspero que goste da experiência e fico no aguardo do seu feeback.\n")
print("Irei imprimir a principio os valores utilizados no vetor em questão e preparei o programa pra imprimir a ordem do vetor após cada passada do programa, sendo possível assim acompanhar cada modificação feita e conferir se a resolução foia adequada\n")

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 3]
print("Segue abaixo o vetor em seu estado inicial:")
print(alist)
print("\nSegue agora o vetor após utilização do algoritmo desenvolvido(estando o resultado final na ultima linha do que será impresso abaixo:")
bubbleSort(alist)
