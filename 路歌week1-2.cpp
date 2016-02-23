#include<iostream>
#include<string>
#include<cassert>
using namespace std;

/*转换程序*/
string unlock(string s, int A[], int num);

int main()
{
        string text = "h?lunc";
        string result;
        int A[] = {1,2,3,4,5,0};

        /*调用unlock函数将转换结果储存于result字符串中*/
        result = unlock(text, A, 2);
        
        /*输出转换后的结果*/
        cout<<result;

        /*程序结束*/
        return 0;
}

string unlock(string s, int A[], int num)
{
        /*测试转换次数是否合法*/
        assert(num >= 0);

        /*若转换次数为0，直接返回原字符串*/
        if(num == 0)
                return s;


        string temp;
        int len = s.size();


        for(int i = 1; i <= num; i++) {
                for(int j = 0; j < len; j++) {
                        /*求出当前对应的位置，将原字符串当前位置的字符加在temp之后*/
                        int location = A[j];
                        temp += s[location];
                }
        
                /*修改一次之后的结果赋给原字符串，准备下一次的修改*/
                s = temp;
        
                /*清空temp字符串*/
                temp.clear();
        }


        /*返回转换的结果*/
        return s;
}
