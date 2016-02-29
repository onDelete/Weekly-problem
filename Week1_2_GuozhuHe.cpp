//时间复杂度为O(n);
void change(char *str,int rank[],int times)
{
    //字符串和数组长度相同
    int length = strlen(str);
    for(int i = 0;i < times;++i)
    {
        char *temp = (char *)malloc(sizeof(char)*length);
        for(int j = 0;j < length;++j)
        {
            temp[j] = str[rank[j]];
        }
        str = temp;
    }
    str[length] = '\0';
    printf("%s",str);
}
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 10000

void change(char *str,int rank[],int times);

int main(int argc, char const *argv[])
{
    char *str = "ABC";
    int rank[4] = {2,0,1};
    int times = 2;
    change(str,rank,times);

    return 0;
}

void change(char *str,int rank[],int times)
{
    //字符串和数组长度相同
    int length = strlen(str);
    for(int i = 0;i < times;++i)
    {
        char *temp = (char *)malloc(sizeof(char)*length);
        for(int j = 0;j < length;++j)
        {
            temp[j] = str[rank[j]];
        }
        str = temp;
    }
    str[length] = '\0';
    printf("%s",str);
}
*/
