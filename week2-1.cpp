//// 20160301知乎群week2.cpp : 定义控制台应用程序的入口点。
//
// setm git test 
#include "stdafx.h"
#include <iostream>
#include <string>
#include <Windows.h>

using namespace std;

bool isContain(string &str);

int _tmain(int argc, _TCHAR* argv[])
{
	string str;
	cout << "请输入‘o’‘x‘字符组合 ：" << endl;
	//getline(cin, str);
	while (getline(cin, str))
	{
		if (isContain(str))
			cout << "重新输入！" << endl;
		else
			break;
	}

	int length = str.length();
	static int sum = 0;
	
	//可从第二个字符开始判断，如果第一个字符为x，则下一个x的o数量一定大于等于首个x
	for (int i = 1; i < length-1; i++)
	{
		if (str[i] == 'x')
		{
			int left = 0;
			int right = 0;

			int n = 1;
			while (str[i - n] == 'o')
			{
				left++;
				n++;
				if (n > i)
					break;
			}

			int m = 1;
			while (str[i + m] == 'o')
			{
				right++;
				m++;
				if (i + m > length)
					break;
			}
			sum = max(sum, right + left);
		}
	}
	cout<<"符合条件的'O'的最大个数:"<<sum<<endl;
	return 0;
}

bool isContain(string &str)
{
	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] != 'x'&& str[i] != 'o')
			return true;
		else
			return false;
	}
}
