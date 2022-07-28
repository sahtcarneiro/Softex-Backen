# Projeto 8 / Módulo 2 / Matéria 1

Autor: Jonathas Carneiro

## Instrução do Projeto

Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:

- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

Veja em anexo um exemplo do arquivo <a href="https://drive.google.com/file/d/1DBjw0RuLmmu9D9E15jxnbmX8kkHuyYvO/view">“alunos_situacao.csv”</a> ou abaixo:

<img src="https://user-images.githubusercontent.com/97403639/181507058-d950ecc4-a62a-4705-aedc-b92860e28659.png" width="700px">

## Resolução

Segue em um arquivo .py nesta pasta.

## Estrutura do Projeto

- /Projeto8
  - READ ME
  - Projeto8.py
  - /assets
    - notas_alunos.csv
    - alunos_situacao.csv
  - /img
    - tabela de exemplo
