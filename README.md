# Weekly-problem

知乎编程学习群每周一题 Week 1      2016/2/22-2016/2/28

问题1比较简单，问题2较难，选做1题即可！

问题1：反转字符串

给你一串字符串，你能否把它反转过来呢？不过，如果给你的字符串本身就是回文的话，你只需要输出"palindrome"即可！


	什么是回文？ "ABCCBA","123321","2222","1","BIGAPPLELPPAGIB"

你只需要提交一个程序，输入为一串字符串，输出为另一串字符串。

例子:

	输入："ABC"						输出："CBA"
	输入："Hi,this is apple!"		输出："!elppa si siht,iH"
	输入："BAT360"					输出："063TAB"	
	输入："QWER!@#$123"				输出："321$#@!REWQ"
	输入："1"						输出："palindrome"
	输入："ABCCBA"					输出："palindrome"



问题2：破解密码

那年，你16岁，她也16岁。。。正是羞涩的年纪，为了更好地上课传纸条，她发明了一种新的加密方法防止其他同学的偷看。可是，你能解出她的这段密码吗？

	你拿到她传给你的纸条后，发现上面竟然是一堆乱码"h?lunc"这是什么意思呢？
	此时，你看到了另一串数字[1,2,3,4,5,0]和一个单独的数字2！
	你突发奇想，原来！你需要重组那句乱码，而每个字符对应的位置都是那串数字决定的。
	这样会不会太简单被破解了？所以，加上那个2意味着你要重组两次。


	我们看看该怎么做呢，首先"h?lunc"六个字符对应012345，按照123450的变换后成了"?lunch"，
	因为有个2，我们要变两次，"?lunch"对应012345,按照123450的顺序重组就成了"lunch?" 
	WOW原来是这个样子！


写一段完整的代码（不仅仅是一个程序），给一个乱码字符串，一个数组，和一个整数，把破解好的密码print出来吧！

例子:

	输入："ABC" [2,0,1] 2	        输出："BCA"
	输入："ABCD" [3,2,1,0] 1	        输出："DCBA"
	输入："12345" [3,1,2,4,0] 1		输出："42351"	
