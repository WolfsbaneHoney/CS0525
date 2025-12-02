#include <stdio.h>

int main()
{
    int a;
    int b;
    int risultato;

    printf("Inserisci un numero: ");
    scanf("%d", &a);

    printf("Inserisci il secondo numero: " );
    scanf("%d", &b);

    risultato = a*b;

    printf("Il risultato è: %d", risultato);

    return 0;
}