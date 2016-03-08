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
        while((c=getchar())!=EOF && c != '\n') {
                a[i++] = c;
                len_a++;
        }


        i = 0;
        while((c=getchar())!=EOF && c != '\n') {
                b[i++] = c;
                len_b++;
        }

        
        /* 声明int型变量key，代表状态 */
        int key = 0;
        
        for(i = 0; i < len_a - len_b; i++) {
                
                /* 用memcmp函数将a，b两个数组的相应位置的字符进行比较 */
                int temp_result = memcmp(a + i,b,len_b);
                
                /* 若相等，key赋值为1，退出循环 */
                if(temp_result == 0) {
                        key = 1;
                        break;  
                }
        }
        
        
        /* 输出key的值 */
        printf("%d",key);       


        /* 程序结束 */
        return 0;
}

