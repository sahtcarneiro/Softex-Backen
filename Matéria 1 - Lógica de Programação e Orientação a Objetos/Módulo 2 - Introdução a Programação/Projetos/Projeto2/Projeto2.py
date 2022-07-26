qnt_rodas = int(input("Quantas rodas tem o veículo? "))
peso = float(input("Quantos quilogramas tem o veículo? "))
qnt_pessoas = int(input("Quantas pessoas cabem no veículo? "))
categoria = "Categoria do Veículo"

if (qnt_rodas < 4):
    categoria = "A"
elif (qnt_rodas == 4 and qnt_pessoas <= 8 and peso <= 3500):
    categoria = "B"
elif (qnt_rodas >= 4 and peso > 3500 and peso < 6000):
    categoria = "C"
elif (qnt_rodas >= 4 and qnt_pessoas > 8):
    categoria = "D"
else:
    categoria: "E"

print("A categoria do veículo é " + categoria)
