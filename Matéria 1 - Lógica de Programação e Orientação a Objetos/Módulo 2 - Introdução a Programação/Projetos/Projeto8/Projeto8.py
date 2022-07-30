import pandas as pd

df = pd.read_csv("./assets/notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"]) / 2
df["media"] = media

faltas = df["faltas"]

situacao = "Aprovado"
df["situacao"] = situacao
df.loc[df["media"] < 7, "situacao"] = "Reprovado"
df.loc[df["faltas"] > 5, "situacao"] = "Reprovado"

df.to_csv("./assets/alunos_situacao.csv")

mais_faltas = df["faltas"].max()
media_geral = df["media"].mean()
maior_media = df["media"].max()

print("Olá, seja bem vindo ao programa de leitura e alteração de arquivos .csv com python!\nEspero que goste da experiência, estou ansioso pelo seu feedback\n")
print("O maior número de faltas foi de: " + str(mais_faltas))
print("A média geral da dos alunos avaliado foi de: " + str(media_geral))
print("A maior média dentre os alunos avaliados foi de: " + str(maior_media))

print("\nAgora que o que foi pedido na instrução do projeto foi concluído irei também imprimir o estado final da tabela, para que seja possível conferir visualmente se meu tratamento da mesma foi correto\n")
print(df)
