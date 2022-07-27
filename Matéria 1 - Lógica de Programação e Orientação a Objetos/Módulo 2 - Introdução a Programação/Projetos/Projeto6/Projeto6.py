name = input("Olá, qual o seu nome? ")
while (True):
    try:
        year = int(
            input("Em que ano você nasceu? "))
        age = 2022 - year
        if (year >= 1922 and year <= 2021):
            print(name + " a sua idade é " + str(age))
            break
        else:
            raise Exception(
                "O valor digitado no campo ano é inválido, tente um valor entre 1922 e 2021!")
    except Exception as err:
        print("Ocorreu um erro.")
        print(err)
