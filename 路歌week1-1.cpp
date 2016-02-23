#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
        vector<char>v;
        char c;

        while((c=getchar())!='\n') {
                v.push_back(c);
        }

        int len=v.size();
        bool key=true;

        for(int i=0;i<len/2;i++) {
                if(v.at(i)!=v.at(len-i-1)) {
                        key=false;
                        break;
                }
        }

        if(key==true) {
                cout<<"palindrome"<<endl;
        }
        else {
                reverse(v.begin(),v.end());
                for(int i=0;i<len;i++) {
                        cout<<v.at(i);
                }
        }

        return 0;
}
