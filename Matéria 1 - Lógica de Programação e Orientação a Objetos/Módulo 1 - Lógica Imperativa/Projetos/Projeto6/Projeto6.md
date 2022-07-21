# Projeto 6 / Módulo 1 / Matéria 1

Autor: Jonathas Carneiro da Silva

## Observação

- O projeto será feito com base em pseudocógico, pois para desenvolvê-lo em uma linguagem de programação seria preciso desenvolver assuntos que ainda não foram abordados.

## Intrução do projeto

Após uma prova de vestibular, uma escola quer identificar quantos dos seus alunos foram aprovados em cada turma de formandos. Ela quer saber qual aluno teve a maior nota e de qual turma ele é. Nessa escola, há quatro turmas (A, B, C e D) com vinte e cinco alunos cada.

Elabore um algoritmo que solicite o nome e a nota do vestibular aos alunos. Depois, informe quantos deles foram aprovados, de que turma são, qual a maior nota em cada turma e qual aluno teve a maior nota de todas.

Para que o aluno seja aprovado no vestibular, ele deverá obter nota maior ou igual a 7.

ATENÇÃO: As notas por turma não podem se repetir.

## Resolução

Var

Q, contador, qtd_aprovados: inteiro
A, MA: caractere
Nota, Melhor_Nota: Real
Resposta: caractere

Inicio

escreval("Digite Qual a Turma ")
Leia (resposta)
Se (resposta = "A") entao
Escreval ("Vamos cadastrar as notas dos alunos da turma A")

      contador <- 1
      Melhor_Nota <- 0
      qtd_aprovados <- 0

      Para contador de 1 ate 2 faca

         Escreval("Aluno", contador)
         Escreval("Nome do(a) aluno(a): ")
         Leia (A)
         Escreval("Nota de " , A , ": ")
         Leia (Nota)

         Se (Nota > Melhor_nota) entao
            Melhor_nota <- Nota
            Ma <- A

            Se(Nota >= 7) entao
               Escreval("Aluno foi aprovado")
               qtd_aprovados <- qtd_aprovados + 1
            Senao
               Escreval("Aluno foi reprovado")

            Fimse
         Fimse
      Fimse

Fimpara

Escreval("O maior aproveitamento foi do(a) aluno(a) ",MA, " com nota", Melhor_Nota)

Escreval("A quantidade de aprovados foi " ,qtd_aprovados)

Fimalgoritmo
