# Projeto 3 / Módulo 1 / Matéria 1

Autor: Jonathas Carneiro

## Observação

O projeto será feito com base na linguagem de programação C++, exclusivamente por afinidade pessoal com a linguagem. Neste arquivo segue encluisivamente a descrição do proposição e da sua resolução, em paralelo, na pasta deste projeto, segue outro documento próprio do C++ para ser executado no DevC++ ou outras IDEs que suportem a linguagem.

## Intrução do projeto

Em uma inscrição, o usuário informou os seguintes dados:

- Nome: José Almeida da Silva
- CPF: 12345678900
- RG: 9517530
- Altura: 1,78
- Endereço: Rua A, 380 – Centro – Recife/PE

No algoritmo, descreva como será:
1. A proposta das variáveis;
2. Elaborada a declaração das variáveis;
3. Utilizado o comando de atribuição.

## Resolução

#include <iostream>

using namespace std;

int main()
{
    string name, adress;
    int cpf, rg;
    float height;
    
    cout << "Digite seu nome: ";
    cin >> name;
    cout << "Digite seu endereço: ";
    cin >> adress;
    cout << "Digite seu cpf (apenas os digitos): ";
    cin >> cpf;
    cout << "Digite seu rg (apenas os digitos): ";
    cin >> rg;
    cout << "Digite sua altura(em metros): ";
    cin >> height;
    
    cout << "Confira os dados informados: ";
    cout << "Nome: " << name << ", Endereço: " << adress << ", Cpf: " << cpf << ", Rg: " << rg << ", Altura: " << height;
}