#include<iostream>
#include<string>
using namespace std;

int search(string s);

int main()
{
        string s;
 

        /* 输入待搜索的字符串,字符串中仅包含'O'和'X'两种字符 */
        cin>>s;


        /* 输出符合题目条件的最大搜索值 */
        cout<<search(s);


        /* 程序结束 */
        return 0;
}

int search(string s)
{
        int len = s.size();
        int max = 0;

        /* 从第二个搜索到倒数第二个 */
        for(int i = 1; i < len - 1; i++) {
                /* 当且仅当当前字符为X时才进行下一步判断 */
                if(s[i] == 'X') {
                        /* 分别设置左右计数变量 */
                        int leftcount = 0;
                        int rightcount = 0;

                        /* 左方搜索 */
                        int j = 1;
                        while(s[i - j] == 'O') {
                                leftcount++;
                                j++;
                        }

                        /* 右方搜索 */
                        j = 1;
                        while(s[i + j] == 'O') {
                                rightcount++;
                                j++;
                        }

                        
                        /* 将当前搜索值与最大搜索值比较,若当前搜索值大于最大搜索值，进行替换 */
                        if(max < leftcount + rightcount)
                                max = leftcount + rightcount;
                }
        }

        /* 返回符合题目条件的最大搜索值 */
        return max;
}
