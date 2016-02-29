//复杂度分析：主要来自字符串的反转，时间度与输入字符串的长度n有关
//时间复杂度为O(n);
void function(char *str,int length)
{
    char newStr[MAXLENGTH];

    int flag = 1;
    for(int i = 0;i < length;++i)
    {
        newStr[i] = str[length - i - 1];
        if(newStr[i] != str[i])
            flag = 0;
    }
    newStr[length] = '\0';

    if(flag == 1)
        printf("palindrome");
    else
        printf("%s",newStr);
}

/*
完整源码
#include <stdio.h>
#include <string.h>
#define MAXLENGTH 100000
void function(char *str,int length);

int main(void)
{
    char str[MAXLENGTH];
    scanf("%s",str);
    
    function(str,strlen(str));

    return 0;
}

void function(char *str,int length)
{
    char newStr[MAXLENGTH];

    int flag = 1;
    for(int i = 0;i < length;++i)
    {
        newStr[i] = str[length - i - 1];
        if(newStr[i] != str[i])
            flag = 0;
    }
    newStr[length] = '\0';

    if(flag == 1)
        printf("palindrome");
    else
        printf("%s",newStr);
}
*/
