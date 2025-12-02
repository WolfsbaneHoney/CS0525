#include <stdio.h>

int main()
{
    int a;
    int b;
    double media;

    printf("Inserisci un numero: ");
    scanf("%d", &a);

    printf("Inserisci il secondo numero: " );
    scanf("%d", &b);

    media = (a+b)/2.0; //numero in float e non intero per evitare arrotondamento

    printf("La media aritmetica è: %lf", media);

    return 0;
}