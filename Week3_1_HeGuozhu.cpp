//时间复杂度O(n*m)
//其实有种更快速的解法
//KMP算法
int function(int arr1[],int length1,int arr2[],int length2)
{
    if(length1 < length2)
        return 0;

    int i=0,j=0;
    while(i < length1 && j < length2)
    {
        if(arr1[i] == arr2[j])
        {
            ++i;
            ++j;
        }
        else
        {
            i -= (j-1);
            j = 0;
        }
    }
    if(j == length2)
        return 1;
    else
        return 0;
}

/*
#include <stdio.h>

int function(int arr1[],int length1,int arr2[],int length2);
int main(int argc, char const *argv[])
{
    int arr1[7] = {1,0,2};
    int arr2[7] = {1,2};
    printf("%d",function(arr1,3,arr2,2));
    return 0;
}

int function(int arr1[],int length1,int arr2[],int length2)
{
    if(length1 < length2)
        return 0;

    int i=0,j=0;
    while(i < length1 && j < length2)
    {
        if(arr1[i] == arr2[j])
        {
            ++i;
            ++j;
        }
        else
        {
            i -= (j-1);
            j = 0;
        }
    }
    if(j == length2)
        return 1;
    else
        return 0;
}
*/
