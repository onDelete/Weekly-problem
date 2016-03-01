
#include<iostream>
#include<string>
using namespace std;

int search(string s);

int main()
{
        string s;
        cin>>s;

        cout<<search(s);

        return 0;
}

int search(string s)
{
        int len = s.size();
        int max = 0;
        for(int i = 1; i < len - 1; i++) {
                if(s[i] == 'O')
                        continue;
                else if(s[i] == 'X') {
                        int leftcount = 0;
                        int rightcount = 0;
                        int j = 1;
                        while(s[i - j] == 'O') {
                                leftcount++;
                                j++;
                        }
                        j = 1;
                        while(s[i + j] == 'O') {
                                rightcount++;
                                j++;
                        }
                        if(max < leftcount + rightcount)
                        max = leftcount + rightcount;
                }
        }
        return max;
}
