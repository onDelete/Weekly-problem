#include <stdio.h>
#include <string.h>
#define MAXLENGTH 100000

int main(void)
{
    char str[MAXLENGTH];
    char newStr[MAXLENGTH];
    scanf("%s",str);
    int l = strlen(str);

    int flag = 1;
    for(int i = 0;i < l;++i)
    {
        newStr[i] = str[l - i - 1];
        if(newStr[i] != str[i])
            flag = 0;
    }
    newStr[l] = '\0';

    if(flag == 1)
        printf("palindrome");
    else
        printf("%s",newStr);
    return 0;
}
