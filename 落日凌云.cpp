//* 
//* @author wtlusvm
//* @date   07/04/2016
//* 
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译！
//* 
//* 问题： 位运算计算器
//* 
//* 这个问题里，我们想做一个简单的计算器，支持加减乘除。建议写四个加，减，乘，除程序，然后在主程序里要支持
//* “数字(运算符号)数字” 的输入，例如 3 + 5。
//* 
//* 最简单的例子：   输入：2 * 2 输出 ： 4
//* 这个问题可以直接 2 << 1 得到结果，这是最简单的情况了。
//* 有些情况也要分情况讨论。
//* 
//* 我们只用考虑整数的运算，除法不用考虑有小数的情况，比如不用考虑5 / 3，
//* 但是如果你想挑战的话也可以做一下，5 / 3 = 1。
//* 注意：不能用 + -*/ 这些符号，而且要考虑各种特殊情况，比如 2 * 3就不能简单的用 << 做。
//* 希望大家不要胡做，好好想一下。
//* 
//* 注意：本程序支持括号
//* 

#include <iostream>
#include <string>
#include "Week6.h"

int main()
{
	//* Code for debug
	//int num1 = 6, num2 = 3;
	//int num3 = -6, num4 = -3;
	//std::cout << "Code for debug:" << std::endl;
	//std::cout << "----BEGIN----" << std::endl;
	//std::cout << Add(num1, num2) << std::endl;//* 9
	//std::cout << Add(num3, num4) << std::endl;//* -9
	//std::cout << Add(num1, num4) << std::endl;//* 3
	//std::cout << Add(num3, num2) << std::endl;//* -3
	//std::cout << Minus(num1, num2) << std::endl;//* 3
	//std::cout << Minus(num3, num4) << std::endl;//* -3
	//std::cout << Minus(num2, num3) << std::endl;//* 9
	//std::cout << Minus(num3, num2) << std::endl;//* -9
	//std::cout << Multiply(num1, num2) << std::endl;//* 18
	//std::cout << Multiply(num3, num4) << std::endl;//* 18
	//std::cout << Multiply(num1, num4) << std::endl;//* -18
	//std::cout << Multiply(num3, num2) << std::endl;//* -18
	//std::cout << Divide(num1, num2) << std::endl;//* 2
	//std::cout << Divide(num2, num1) << std::endl;//* 0
	//std::cout << Divide(num3, num4) << std::endl;//* 2
	//std::cout << Divide(num4, num3) << std::endl;//* 0
	//std::cout << Divide(num1, num4) << std::endl;//* -2
	//std::cout << Divide(num4, num1) << std::endl;//* 0
	//std::cout << Divide(num3, num2) << std::endl;//* -2
	//std::cout << Divide(num2, num3) << std::endl;//* 0
	//std::cout << "----END----" << std::endl;

	std::string input;
	std::getline(std::cin, input);
	std::cout << Calculator(input) << std::endl;
	return 0;
}
