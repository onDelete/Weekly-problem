#include<stdio.h>
#define MAXSTR 100
int main (void)
{
	int m;
	char str[MAXSTR];
	scanf("%s", str);
	for(m = 0; str[m] != '\0'; m++)
		;
	for(m -= 1; m >= 0; m--)
		putchar(str[m]);
	return 0;
}
