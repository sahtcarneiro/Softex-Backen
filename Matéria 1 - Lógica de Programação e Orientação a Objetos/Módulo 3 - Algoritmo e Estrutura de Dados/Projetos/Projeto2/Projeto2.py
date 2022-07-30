def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while (j >= 0 and key < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        print(array)


numbers = [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
           57, 59, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
print("Olá, bem vindo ao algoritmo de Insertion Sort com python\nSegue o array em sua forma original:")
print(numbers)
print("\nSegue agora todo o processo, passo a passo, do funcionamento do algoritmo:")
insertion_sort(numbers)
print("\nE por fim segue apenas o resultado final:")
print(numbers)
