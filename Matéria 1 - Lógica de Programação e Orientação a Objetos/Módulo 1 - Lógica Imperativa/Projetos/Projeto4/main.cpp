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