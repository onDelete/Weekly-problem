//时间复杂度为O(n^2)
//主要来自嵌套循环
void function(int *arr,int length)
{
    int flag = 1;
    for(int i = 0;i < length - 1 || flag == 0;++i)
    {
        flag = 1;
        for(int j = 0;j < length - i - 1;j++)
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                flag = 0;
            }
        }
    }

    for(int i = 0;i < length;++i)
    {
        printf("%d ",arr[i]);
    }
}
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 10000

void function(int *arr,int length);

int main(int argc, char const *argv[])
{
    int arr[MAX_LENGTH]={1,5,4,6,7};
    function(arr,5);

    return 0;
}

void function(int *arr,int length)
{
    int flag = 1;
    for(int i = 0;i < length - 1 || flag == 0;++i)
    {
        flag = 1;
        for(int j = 0;j < length - i - 1;j++)
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                flag = 0;
            }
        }
    }

    for(int i = 0;i < length;++i)
    {
        printf("%d ",arr[i]);
    }
}
*/
