#include "stdio.h"

int function(char *s, int n){
    int res = 0, i = 0, tmp = 0, len;
    while(s[i++])
        ;
    len = i - 1;
    i = 0;
    printf("len =%d\n", len);
    while(s[i++]) {
        if (s[i] == 'X')
        {
            if(i - n >= 0 && s[i - n] == 'O')
                tmp += 1;
            if(i + n < len && s[i + n] == 'O')
                tmp += 1;
            if(i % n != 0 && i - 1 >= 0 && s[i - 1] == 'O')
                tmp += 1;
            if((i + 1) % n != 0 && i + 1 < len && s[i + 1] == 'O')
                tmp += 1;
            res = tmp > res ? tmp : res;
        }
        tmp = 0;
    }
    return res;
}

int main(int argc, char const *argv[])
{
    char s[] = "XOOXOOOOOOXOOXOXXXOX";
    int n = 5;

    printf("%d\n", function(s, n));

    return 0;
}
