class number_complex:
    def __init__(real, img, self):
        self.real = real
        self.img = img*1j
        self.complex = self.real + self.img
        print(
            f'Parte real: {self.real}; Parte imaginária: {(self.img*-1j).real}')

    def soma(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        return A+B+C

    def subtracao(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        return (A-B)-C

    def multiplicacao(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        return (A*B)*C

    def divisao(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        return (A/B)/C


real_frist_number_complex = print(
    int(input("Qual a parte real do primeiro número complexo?")))
img_frist_number_complex = print(
    int(input("Qual a parte imaginária do primeiro número complexo?")))
frist_number_complex = number_complex(
    real_frist_number_complex, img_frist_number_complex)

real_sec_number_complex = print(
    int(input("Qual a parte real do segundo número complexo?")))
img_sec_number_complex = print(
    int(input("Qual a parte imaginária do segundo número complexo?")))
frist_number_complex = number_complex(
    real_sec_number_complex, img_sec_number_complex)

real_third_number_complex = print(
    int(input("Qual a parte real do terceiro número complexo?")))
img_third_number_complex = print(
    int(input("Qual a parte imaginária do terceiro número complexo?")))
third_number_complex = number_complex(
    real_third_number_complex, img_third_number_complex)
