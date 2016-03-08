/* C style version */

#include<stdio.h>
#include<string.h>

const int MAX_SIZE = 1000;

int main()
{
        char a[MAX_SIZE];
        char b[MAX_SIZE];
        char c;

        int len_a = 0;
        int len_b = 0;
        
        int i = 0;
        while((c=getchar())!=EOF && c != '\n')
        {
                a[i++] = c;
                len_a++;
        }

        i = 0;
        while((c=getchar())!=EOF && c != '\n')
        {
                b[i++] = c;
                len_b++;
        }
        
        int key = 0;
        for(i = 0; i < len_a - len_b; i++)
        {
                int temp_result = memcmp(a + i,b,len_b);
                if(temp_result == 0)
                {
                        key = 1;
                        break;  
                }
        }
        
        printf("%d",key);       

        return 0;
}
