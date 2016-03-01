#include<iostream>
#include<string>
using namespace std;

int map[100][100];
int search(int m, int n);

int main()
{
        /* 输入的字符数是n的整倍数 */
        string s；
        cin>>s;


        /* n为字符数组的列数 */
        int n;
        cin>>n;


        /* p用来确定字符串中当前字符, m为字符数组的行数 */
        int p = 0;
        int m = s.size() / n;
        
        
        /* 按位置将字符串中的字符输入到字符数组当中 */
        for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                        map[i][j] = s[p++];
                }
        }


        /* 输出搜索的最大值 */
        cout<<search(m, n);


        /* 程序结束 */
        return 0;
}

int search(int m, int n)
{
        int max = 0;
        
        
        for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {

                        int count = 0;
                        if(map[i][j] == 'X') {
                                /* 分别判断上下左右四个方向的位置是否合法且为字符O，若是，计数器加1 */
                                if( i >= 0 && i < m && j >=0 && j < n && map[i - 1][j] == 'O' )
                                        count++;
                                if( i >= 0 && i < m && j >=0 && j < n && map[i + 1][j] == 'O' )
                                        count++;
                                if( i >= 0 && i < m && j >=0 && j < n && map[i][j - 1] == 'O' )
                                        count++;
                                if( i >= 0 && i < m && j >=0 && j < n && map[i][j + 1] == 'O' )
                                        count++;
                        }
                if(count > max)
                        max = count;
                /* 若max的值已经为4,退出循环  */
                if(max == 4)
                        break;
                }
        }

        /* 返回搜索的最大值 */
        return max;
}
