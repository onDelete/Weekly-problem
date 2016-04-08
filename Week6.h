//* 
//* @author wtlusvm
//* @date   07/04/2016
//* 
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译！
//* 
//* ^: 按位异或；&：按位与； | ：按位或
//* 计算机系统中，数值一律用补码来表示
//* 有关补码的更多：
//* 中文维基百科：https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8
//* 英文维基百科：https://en.wikipedia.org/wiki/Two%27s_complement
//* 中文百度百科：http://baike.baidu.com/view/377340.htm

#ifndef WEEK5_H
#define WEEK5_H

#include <iostream>
#include <string>
#include <algorithm>

//* 加法运算：将一个整数用二进制表示，其加法运算时，不计进位的和为sum = a^b，进位就是arr = a&b,
//* 迭代执行此过程，直到进位为0
int Add(int num1, int num2)
{
	if (num1 == 0)
		return num2;
	int sum = num1;

	while (num2)
	{
		sum = num1^num2;
		num2 = (num1&num2) << 1;
		num1 = sum;
	}
	return sum;
}

//* 减法运算：a - b = a + (-b)，根据补码的特性，各位取反加1即可。
int Negative(int num)
{
	num = ~num;
	return Add(num, 1);
}

int Minus(int num1, int num2)
{
	return Add(num1, Negative(num2));
}

//* 乘法运算：将b个a相加。
int SubMultiply(int num1, int num2)
{
	int result = 0;
	while (num2)
	{
		if (num2 & 1)
		{
			result = Add(num1, result);
		}
		num1 = num1 << 1, num2 = num2 >> 1;
	}
	return result;
}

int Multiply(int num1, int num2)
{
	if (num2 == 0 || num1 == 0)
		return 0;
	
	if (num1 > 0 && num2 > 0)
	{
		return SubMultiply(num1, num2);
	}

	else if (num1 > 0 && num2 < 0)
	{
		return Negative(SubMultiply(num1, Negative(num2)));
	}

	if (num1 < 0 && num2 < 0)
	{
		return SubMultiply(Negative(num1), Negative(num2));
	}

	else if (num1 < 0 && num2 > 0)
	{
		return Negative(SubMultiply(Negative(num1), num2));
	}
}

void isZero(int num1,int num2)
{
	if (num2 == 0)
	{
		std::cout << "Imagine that you have " << num1 << " cookies, and you split them evenly "
			<< "among 0 friends, How many cookies does each person get? "
			<< "See? It doesn’t make sense. ";
		if (num1 == 0)
		{
			std::cout << "And Cookie Monster is sad that there are no cookies. ";
		}
		std::cout << "And you are sad that you have no friends." << std::endl;
	}
}

int ABS(int num)
{
	if (num >= 0)
		return num;
	else
		return Negative(num);
}

//* 除法运算：除法运算是乘法的逆。看a最多能减去多少个b。
int SubDivide(int num1, int num2)
{
	int result = 0;
	while (num1 >= num2)
	{
		num1 = Minus(num1, num2);
		result = Add(result, 1);
	}
	return result;
}

int Divide(int num1, int num2)
{
	isZero(num1,num2);
	if ((num1 == 0 && num2 != 0) || ABS(num1) < ABS(num2))
		return 0;

	if (num1 > 0 && num2 > 0)
	{
		return SubDivide(num1, num2);
	}

	else if (num1 > 0 && num2 < 0)
	{
		return Negative(SubDivide(num1, Negative(num2)));
	}

	if (num1 < 0 && num2 < 0)
	{
		return SubDivide(Negative(num1), Negative(num2));
	}

	else if (num1 < 0 && num2 > 0)
	{
		return Negative(SubDivide(Negative(num1), num2));
	}
}

int Calculator(std::string &input)
{
	//* 移除括号
	std::remove_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '(') ? true : false; });
	auto tmp5 = std::remove_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == ')') ? true : false; });
	input.erase(tmp5, input.end());

	//* 分别查找+、-、*、/

	auto tmp1 = std::find_if(input.begin() + 1, input.end(),
		[](char tmp) {return (tmp == '+') ? true : false; });
	//* tmp134均是end()才是运算符
	auto tmp2 = std::find_if(input.begin() + 1, input.end(),
		[](char tmp) {return (tmp == '-') ? true : false; });
	
	auto tmp3 = std::find_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '*') ? true : false; });
	
	auto tmp4 = std::find_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '/') ? true : false; });

	//* 加法
	if (tmp1 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp1));
		int num2 = std::stod(std::string(tmp1 + 1, input.end()));
		return Add(num1, num2);
	}

	//* 减法
	if (tmp2 != input.end() && tmp1 == input.end() && tmp3 == input.end() && tmp4 == input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp2));
		int num2 = std::stod(std::string(tmp2 + 1, input.end()));
		return Minus(num1, num2);
	}

	//* 乘法
	if (tmp3 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp3));
		int num2 = std::stod(std::string(tmp3 + 1, input.end()));
		return Multiply(num1, num2);
	}

	//* 除法
	if (tmp4 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp4));
		int num2 = std::stod(std::string(tmp4 + 1, input.end()));
		return Divide(num1, num2);
	}
}

#endif // !WEEK5_H
