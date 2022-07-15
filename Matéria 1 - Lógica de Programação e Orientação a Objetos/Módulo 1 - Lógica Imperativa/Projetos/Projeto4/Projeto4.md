# Projeto 4 / Módulo 1 / Matéria 1

Autor: Jonathas Carneiro

## Observação

O projeto será feito com base na linguagem de programação C++, exclusivamente por afinidade pessoal com a linguagem. Neste arquivo segue encluisivamente a descrição do proposição e da sua resolução, em paralelo, na pasta deste projeto, segue outro documento próprio do C++ para ser executado no DevC++ ou outras IDEs que suportem a linguagem.

## Intrução do projeto

Elabore um algoritmo que representa um cadastro. Ele deve ler os seguintes dados fornecidos pelo usuário:

- Nome
- Endereço
- Cidade
- CPF
- RG
- Idade
- Nome do pai
- Nome da mãe
- Peso
- Renda bruta

Apresente as informações solicitadas no final do cadastro.

## Resolução

#include <iostream>

using namespace std;

int main()
{
    string name, adress, city, fathersname, mothersname;
    int cpf, rg;
    float height, weight, income;
    
    cout << "Digite seu nome: ";
    cin >> name;
    cout << "Digite o nome do seu Pai: ";
    cin >> fathersname;
    cout << "Digite o nome da sua Mãe: ";
    cin >> mothersname;
    cout << "Digite seu endereço: ";
    cin >> adress;
    cout << "Em qual cidade você mora? ";
    cin >> city;
    cout << "Digite seu cpf (apenas os digitos): ";
    cin >> cpf;
    cout << "Digite seu rg (apenas os digitos): ";
    cin >> rg;
    cout << "Digite sua altura(em metros): ";
    cin >> height;
    cout << "Digite seu peso(em Kg): ";
    cin >> weight;
    cout << "Digite sua renda bruta(em reais): ";
    cin >> income;
    
    cout << "Confira os dados informados: ";
    cout << "Nome: " << name << "/ Nome do Pai: " << fathersname << "/ Nome da Mãe: " << mothersname << "/ Endereço: " << adress << "/ Cidade: " << city << "/ Cpf: " << cpf << "/ Rg: " << rg << "/ Altura: " << height << "/ Peso: " << weight << "/ Renda Bruta: " << income ;
}