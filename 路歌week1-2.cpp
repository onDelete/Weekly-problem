#include<iostream>
#include<string>
#include<cassert>
using namespace std;

string unlock(string &s, int A[], int num);

int main()
{
        string text = "h?lunc";
        string result;
        int A[] = {1,2,3,4,5,0};

        result = unlock(text, A, 2);
        cout<<result;

        return 0;
}

string unlock(string &s, int A[], int num)
{
        assert(num >= 0);


        if(num == 0)
                return s;


        string temp;
        int len = s.size();


        for(int i = 1; i <= num; i++) {
                for(int j = 0; j < len; j++) {
                        int location = A[j];
                        temp += s[location];
                }
                s = temp;
                temp.clear();
        }

        return s;
}
