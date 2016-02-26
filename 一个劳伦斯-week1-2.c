//week1-2   ————    一个劳伦斯
#include<stdio.h>
#include<string.h>
#define LENGTH 1000

int main()
{
    char input[3*LENGTH+4];
    char mess_pw[LENGTH];
    int rank[LENGTH];
    int times;
    gets(input);
    unsigned long int input_length = strlen(input);
    unsigned long int pw_length = (input_length-4)/3;
    for(int i=0; i<pw_length+2; i++)
    {
        if(input[i] != '"')
            mess_pw[i-1] = input[i];
    }
    int count = 0;
    for(unsigned long int i=pw_length+2; i<input_length-1; i++)
    {
        if(input[i]!='[' && input[i]!=']')
        {
            if(input[i] == ',')
            {
                count++;
                continue;
            }
            else
                rank[i-(pw_length+3+count)] = input[i]-48;
        }
        else
            continue;
    }
    times = input[input_length-1]-48;
    char pw[LENGTH];
    
    while(times>0)
    {
        for(int i=0; i<pw_length; i++)
        {
            pw[i]=mess_pw[rank[i]];
        }
        for(int i=0; i<pw_length; i++)
        {
            mess_pw[i] = pw[i];
        }
        times--;
    }
    printf("\"");
    for(int i=0; i<pw_length; i++)
        printf("%c", pw[i]);
    printf("\"\n");
    return 0;
}
