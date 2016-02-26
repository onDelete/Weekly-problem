//Reverse_the_String
#include<stdio.h>
#include<string.h>
#define LENGTH 1000
void Reverse_the_String(char a_string[], char r_string[], unsigned long int a_length);

int main(int argc, const char * argv[])
{
    char a_string[LENGTH];
    char r_string[LENGTH];
    gets(a_string);
    unsigned long int a_length = strlen(a_string);
    Reverse_the_String(a_string,r_string,a_length);
    int count = 0;
    for(int i = 0; i < strlen(a_string); i++)
    {
        if(a_string[i] == r_string[i])
        {
            count ++;
        }
    }
    if(count == strlen(a_string))
    {
        printf("palindrome");
    }else
    {
        puts(r_string);
    }
    return 0;
}

void Reverse_the_String(char a_string[LENGTH], char r_string[LENGTH], unsigned long int a_length)
{
    for(int i = 0; i < a_length; i++)
    {
        r_string[i] = a_string[a_length-1-i];
    }
}
