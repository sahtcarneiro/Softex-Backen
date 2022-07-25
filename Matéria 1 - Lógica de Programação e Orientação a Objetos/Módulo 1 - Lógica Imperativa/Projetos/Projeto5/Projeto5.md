# Projeto 5 / Módulo 1 / Matéria 1

Autor: Jonathas Carneiro

## Observação

- O projeto será feito com base na linguagem de programação C++, exclusivamente por afinidade pessoal com a linguagem. Neste arquivo segue encluisivamente a descrição do proposição e da sua resolução, em paralelo, na pasta deste projeto, segue outro documento próprio do C++ para ser executado no DevC++ ou outras IDEs que suportem a linguagem.
- Esse projeto também conta com um fluxograma que pode ser encontrado dentro da pasta do projeto ou abaixo, que serve para orientar a linha lógica que foi utilizada no programa. <br>

<img src="https://user-images.githubusercontent.com/97403639/180218929-ee11fb01-114b-4b19-a118-7ba4c669b0a0.png" width="500px">

## Instrução do projeto

Elabore um algoritmo que possa descobrir, através de perguntas e respostas, qual meio de transporte o usuário está pensando.
O usuário deverá escolher uma das seguintes opções:

- Trator
- Moto
- Bicicleta
- Trem
- Carro
- Caminhão
- Ônibus
- Paraquedas
- Balão
- Avião
- Helicóptero
- Submarino
- Barco
- Navio
- Lancha

Para chegar ao resultado, só devem ser usadas perguntas que retornem "Sim" ou "Não".

Exemplo:
É terrestre? Sim.
Cabe apenas uma pessoa? Sim.
É pesado? Não.
Tem pedal? Sim.
Então, o transporte escolhido foi a bicicleta.

Para chegar ao resultado de cada uma das opções, use o modelo ilustrado na imagem em anexo.

<a href = "https://drive.google.com/file/d/12JqHZfqXSmJmyTEDOoM1IG85kHwLhirT/view?usp=sharing"> Ilustração </a>

OBS.: No enunciado tem a opção paraquedas, na ilustração dada pelo problemas o mesmo não aparece mas tem a asa delta, como a escolha de qualquer um dos dois não intefere na resolução do problema eu optei por seguir o enunciado e utilizar o paraquedas.

## Resolução

#include <iostream>

using namespace std;

int main()
{

    string answer;

    cout << "Olá, a proposta deste programa é adivinha qual dentre os veículos dispoíveis você escolheu sem perguntar diretamente, para isso escolha um dos veículos abaixo e responda as perguntas seguinta com apenas sim ou nao.\n";
    cout << "Trator,\n Moto,\n Bicicleta,\n Trem,\n Carro,\n Caminhão,\n Ônibus,\n Paraquedas,\n Balão,\n Avião,\n Helicóptero,\n Submarino,\n Barco,\n Navio,\n Lancha.\n";

    cout << "O veículo escolhido é terrestre?\n";
    cin >> answer;

    if (answer == "sim") {
        cout << "Precisa usar capacete?\n";
        cin >> answer;

        if (answer == "sim") {
            cout << "Você escolheu a Moto.";
        }
        else {
            cout << "Cabe apenas uma pessoa?\n";
            cin >> answer;

            if (answer == "sim") {
                cout << "É um veículo pesado?\n";
                cin >> answer;

                if (answer == "sim") {
                    cout << "Você escolheu o Trator.";
                }
                else {
                    cout << "Você escolheu a Bicicleta.";
                }
            }
            else {
                cout << "Anda em trilhos?\n";
                cin >> answer;

                if (answer == "sim") {
                    cout << "Você escolheu o trem.";
                }
                else {
                    cout << "É um veículo leve?\n";
                    cin >> answer;

                    if (answer == "sim") {
                        cout << "Você escolher o Carro.";
                    }
                    else {
                        cout << "Ele tem carroceria?\n";
                        cin >> answer;

                        if (answer == "sim") {
                            cout << "Você escolheu o Caminhão.";
                        }
                        else {
                            cout << "Você escolheu o Ônibus.";
                        }
                    }
                }
            }
        }
    }
    else {
        cout << "Seu veículo é aéreo?\n";
        cin >> answer;

        if (answer == "sim") {
            cout << "Precisa pular?\n";
            cin >> answer;

            if (answer == "sim") {
                cout << "Você escolheu o Paraquedas.";
            }
            else {
                cout << "Ele é devagar?\n";
                cin >> answer;
                 if (answer == "sim") {
                     cout << "Você escolheu o Balão.";
                 }
                 else {
                     cout << "Ele possui asas fixas?\n";
                     cin >> answer;

                     if (answer == "sim") {
                         cout << "Você escolheu o Avião.";
                     }
                     else {
                         cout << "Você escolheu o Helicóptero.";
                     }
                 }
            }
        }
        else {
            cout << "Ele fica coberto de água?\n";
            cin >> answer;

            if (answer == "sim") {
                cout << "Você escolheu o Submarino.";
            }
            else {
                cout << "Ele possui velas?\n";
                cin >> answer;

                if (answer == "sim") {
                    cout << "Você escolheu o Barco.";
                }
                else {
                    cout << "Ele é alto?\n";
                    cin >> answer;

                    if (answer == "sim") {
                        cout << "Você escolheu o Navio.";
                    }
                    else {
                        cout << "Você escolheu a Lancha.";
                    }
                }
            }
        }
    }

}
