#include "stdio.h"

void function(char *s, int *l){
    int i = 0;
    while(s[i++])
        ;
    char tmp[i - 1];
    i = 0;
    while(tmp[i]=s[i])
        i++;
   while(i-- > -1)
        s[i] = tmp[l[i]];
}

int main(int argc, char const *argv[])
{
    int i = 2;
    char s[] = "h?lunc";
    int a[] = {1,2,3,4,5,0};

    while(i--)
        function(s, a);
    
    printf("%s\n", s);

    return 0;
}
