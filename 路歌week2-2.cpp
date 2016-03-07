#include<iostream>
#include<stack>
using namespace std;

int main()
{
  	stack<char> a;
  	stack<char> b; 
  	char c;

        while((c = getchar()) != EOF && c != '\n') {
                a.push(c);
        }

        while((c = getchar()) != EOF && c != '\n') {
                b.push(c);
        }
	
  	bool key = false;
  	while(b.empty() == false || a.empty() == false) {
  		  if(b.top() == a.top())  {
  	    		b.pop();
  		     	a.pop();
  		  }
  		  else  {
  		    	a.pop();
	  	  }
	  	  
	  	  
		    if(b.empty() == true) {
		      	key = true;
		      	break;
		    }
		    
		    
		    if(a.empty() == true && b.empty() == false) {
		      	key = false;
			      break;
	    	}
	  }
	
	
	  if(key == true)
	  	  cout<<1;
	  else
	  	  cout<<0;
		  
		  
    /*程序结束 */
  	return 0;
}
