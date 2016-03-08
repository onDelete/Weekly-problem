/* C++ version */

#include<iostream>
#include<vector>
using namespace std;

int main()
{
        vector<char> a;
        vector<char> b;
        char c;
        
        
        while((c = getchar()) != EOF && c != '\n') {
                a.push_back(c);
        }
        
        
        while((c = getchar()) != EOF && c != '\n') {
                b.push_back(c);
        }


        int len_a = a.size();
        int len_b = b.size();


        int key = 0;
        
        
        for(int i = 0; i < len_a - len_b + 1; i++ ) {
                
                /* 将a的当前位置的字符与b当前位置的字符比较，若相等则进行下一位的比较 */
                for(int j = 0; j < len_b; j++) {
                        
                        
                        /* 若相同，key的值加一 */
                        if(a.at(i + j) == b.at(j)) {
                                key++;
                        }
                        /* 若不相同，退出循环，结束此次比较 */
                        else {
                                key = 0;
                                break;
                        }
                        
                        
                }
                
                /* 如果key的值为len_b，满足要求，输出1，退出循环 */
                if(key == len_b) {
                        cout<<1;
                        break;
                }
                
                
        }

        
        /* 整个循环结束之后都不能使key的值为len_b，输出0 */
        if(key != len_b)
                cout<<0;
        
        
        /* 程序结束 */
        return 0;
}
