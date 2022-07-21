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