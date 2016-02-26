//week1-2   ————    一个劳伦斯
#include<stdio.h>
#include<string.h>
#define LENGTH 1000

int main()
{
    char input[3*LENGTH+4];                                         //声明input字符串以接收所有输入
    gets(input);                                                    //一次获得所有输入
    
    char mess_pw[LENGTH];                                           //声明mess_pw表示乱码字符串
    int rank[LENGTH];                                               //声明rank表示数组
    int times;                                                      //声明times表示整数
    unsigned long int input_length = strlen(input);                 //声明input_length以确定输入的input字符串的长度
    unsigned long int pw_length = (input_length-4)/3;               //确定mess_pw以及rank的长度
    /*-----从input中解析出mess_pw-----*/
    for(int i=0; i<pw_length+2; i++)
    {
        if(input[i] != '"')
            mess_pw[i-1] = input[i];
    }
    /*-----从input中解析出rank-----*/
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
    /*-----从input中解析出times-----*/
    times = input[input_length-1]-48;
    
    char pw[LENGTH];                                                //声明pw以表示破解后的密码
    /*-----进行mess_pw的破解，并赋值给pw-----*/
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
    /*-----输出破解后的密码-----*/
    printf("\"");
    for(int i=0; i<pw_length; i++)
        printf("%c", pw[i]);
    printf("\"\n");
    /*-----END!!!-----*/
    return 0;
}
