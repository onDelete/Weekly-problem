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
  	
  	
  		/* 两个栈顶相同时都弹出 */
		if(b.top() == a.top())  {
  	    		b.pop();
  		     	a.pop();
		}
		/* 若两个栈顶不相等，弹出a的栈顶，继续与b的栈顶进行判断 */
  		else  {
  		    	a.pop();
  		}
	  	
	  	  
	  	/* 若b栈为空，key赋值为真，退出循环 */
		if(b.empty() == true) {
		      	key = true;
		      	break;
		}
		
		    
		/* 若a栈为空且b栈不为空，key赋值为假，退出循环 */
	        if(a.empty() == true && b.empty() == false) {
	        	key = false;
	        	break;
	    	}
	    	
	    	
	  }
	
	
	/* 根据key的值输出最后结果，key为真输出1，key为假输出0 */
	if(key == true)
		cout<<1;
	else
		cout<<0;
		  
		  
    	/*程序结束 */
  	return 0;
}
