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
        
        for(int i = 0; i < len_a - len_b + 1; i++ ) 
        {
                for(int j = 0; j < len_b; j++) 
                {
                        if(a.at(i + j) == b.at(j))
                        {
                                key++;
                        }
                        else
                        {
                                key = 0;
                                break;
                        }
                }
                if(key == len_b)
                {
                        cout<<1;
                        break;
                }
        }

        if(key != len_b)
                cout<<0;

        return 0;
}
