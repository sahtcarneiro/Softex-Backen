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