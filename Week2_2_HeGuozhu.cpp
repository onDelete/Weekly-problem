//时间复杂度为O(n)
void function(char *arr,int colum)
{
    int max = 0;
    int length = strlen(arr);
    for(int i = 0;i < length;++i)
    {
        int now = 0;
        int row = i / colum;
        if(arr[i] == 'X')
        {
            int up = i - colum;
            int down = i + colum;
            int left = i - 1;
            int right = i + 1;
            if(up >= 0 && up < length && arr[up] == 'O')
                ++now;
            if(down >= 0 && down < length && arr[down] == 'O')
                ++now;
            if(left >= row*colum && left < length && arr[left] == 'O')
                ++now;
            if(right < ((row+1)*colum) && right < length && arr[right] == 'O')
                ++now;
        }
        if(now > max)
            max = now;
        if(max == 4)
            break;
    }
    printf("%d",max);
}
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 10000

void function(char *arr,int length);

int main(int argc, char const *argv[])
{
    char arr[MAX_LENGTH]="OXOOOXOXOXOXXOX";
    function(arr,5);

    return 0;
}

void function(char *arr,int colum)
{
    int max = 0;
    int length = strlen(arr);
    for(int i = 0;i < length;++i)
    {
        int now = 0;
        int row = i / colum;
        if(arr[i] == 'X')
        {
            int up = i - colum;
            int down = i + colum;
            int left = i - 1;
            int right = i + 1;
            if(up >= 0 && up < length && arr[up] == 'O')
                ++now;
            if(down >= 0 && down < length && arr[down] == 'O')
                ++now;
            if(left >= row*colum && left < length && arr[left] == 'O')
                ++now;
            if(right < ((row+1)*colum) && right < length && arr[right] == 'O')
                ++now;
        }
        if(now > max)
            max = now;
        if(max == 4)
            break;
    }
    printf("%d",max);
}
*/
