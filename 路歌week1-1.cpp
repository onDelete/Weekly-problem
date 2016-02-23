#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
        vector<char>v;
        char c;

        /*把键盘上的输入都放到v向量中，换行符作为结束*/
        while((c=getchar())!='\n') {
                v.push_back(c);         
        }

        int len=v.size();
        bool key=true;


        /*判断v中存储的是不是回文串*/
        for(int i=0;i<len/2;i++) {
                if(v.at(i)!=v.at(len-i-1)) {
                        key=false;
                        break;
                }
        }
        
        
        /*若是回文串，输出palindrome*/
        if(key==true) {
                cout<<"palindrome"<<endl;
        }
        /*若不是回文串，用reverse()对向量进行翻转，然后输出*/
        else {
                reverse(v.begin(),v.end());
                for(int i=0;i<len;i++) {
                        cout<<v.at(i);
                }
        }
        
        
        /*程序结束*/
        return 0;
}
