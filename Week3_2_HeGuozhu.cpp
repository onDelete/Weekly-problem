//时间复杂度O(n)
int function(int arr1[],int length1,int arr2[],int length2)
{
    if(length2 > length1)
        return 0;

    int n = 0;
    for (int i = 0; i < length1 && n < length2; ++i)
    {
        if(length2 - n > length1 - i)
            break;
        if(arr1[i] == arr2[n])
            ++n;
    }
    if(n == length2)
        return 1;
    else
        return 0;
}


/*
#include <stdio.h>

int function(int arr1[],int length1,int arr2[],int length2);
int main(int argc, char const *argv[])
{
    int arr1[7] = {1,3,2,4,3,5,6};
    int arr2[7] = {1,2,3,6};
    printf("%d",function(arr1,7,arr2,4));
    return 0;
}

int function(int arr1[],int length1,int arr2[],int length2)
{
    if(length2 > length1)
        return 0;

    int n = 0;
    for (int i = 0; i < length1 && n < length2; ++i)
    {
        if(length2 - n > length1 - i)
            break;
        if(arr1[i] == arr2[n])
            ++n;
    }
    if(n == length2)
        return 1;
    else
        return 0;
}
*/
