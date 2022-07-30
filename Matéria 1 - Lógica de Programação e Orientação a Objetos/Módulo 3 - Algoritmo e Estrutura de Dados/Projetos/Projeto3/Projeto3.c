#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
  float *v;
  int i, num_componentes;
  printf("Olá, seja bem vindo ao programa de alocação, realocação e liberação de memória.\n\nApesar da proposta ser apenas a criação de um vetor por ponteiro e modificar seu tamanho e após isso liberar seu espaço de memória, eu escolhi por permitir o usuario escolher qual tamanho do vetor deseja e que o mesmo digite todos os valores do vetores, e depois possa fazer o mesmo no processo de realocação, sendo assim o requisito de ter um vetor com tamanho 22 vai ficar nas mãos do usuário que executar o programa!\nEspero que goste da experiência e aguardo seu feecback!\n\n");
  printf("Informe o numero de componentes do vetor\n");
  scanf("%d", &num_componentes);
  
  
  v = (float *) malloc(num_componentes * sizeof(float));
  
  for (i = 0; i < num_componentes; i++)
  {
    printf("\nDigite o valor para a posicao %d do vetor: ", i+1);
    scanf("%f",&v[i]);
    }
  
  printf("\nValores do vetor dinamico:\n\n");
  
  for (i = 0;i < num_componentes; i++)
  {
    printf("%.2f\n",v[i]);
  }
  
  printf("\nAgora vamos mudar o tamanho do vetor?\n");
  v = (float *)realloc (v, i *sizeof(float));
  printf("Informe o novo numero de componentes do vetor\n");
  scanf("%d", &num_componentes);
  
  for (i = 0; i < num_componentes; i++)
  {
    printf("\nDigite o valor para a posicao %d do vetor: ", i+1);
    scanf("%f",&v[i]);
    }
  
  printf("\nValores do vetor dinamico:\n\n");
  
  for (i = 0;i < num_componentes; i++)
  {
    printf("%.2f\n",v[i]);
  }
  
  free(v);
  
  getch();
  return 0;
}
