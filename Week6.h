//* 
//* @author wtlusvm
//* @date   07/04/2016
//* 
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译！
//* 

#ifndef WEEK5_H
#define WEEK5_H

#include <iostream>
#include <string>

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

int Negative(int num)
{
	num = ~num;
	return Add(num, 1);
}

int Minus(int num1, int num2)
{
	return Add(num1, Negative(num2));
}

int Multiply(int num1, int num2)
{
	if (num2 == 0 || num1 == 0)
		return 0;

	int result = 0;
	if (num1 > 0 && num2 > 0)
	{
		while (num2)
		{
			if (num2 & 1)
			{
				result = Add(num1, result);
			}
			num1 = num1 << 1, num2 = num2 >> 1;
		}
	}
	else if (num1 > 0 && num2 < 0)
	{
		num2 = Negative(num2);
		while (num2)
		{
			if (num2 & 1)
			{
				result = Add(num1, result);
			}
			num1 = num1 << 1, num2 = num2 >> 1;
		}
		result = Negative(result);
	}
	if (num1 < 0 && num2 < 0)
	{
		num1 = Negative(num1);
		num2 = Negative(num2);
		while (num2)
		{
			if (num2 & 1)
			{
				result = Add(num1, result);
			}
			num1 = num1 << 1, num2 = num2 >> 1;
		}
	}
	else if (num1 < 0 && num2 > 0)
	{
		num1 = Negative(num1);
		while (num2)
		{
			if (num2 & 1)
			{
				result = Add(num1, result);
			}
			num1 = num1 << 1, num2 = num2 >> 1;
		}
		result = Negative(result);
	}
	return result;
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

int Divide(int num1, int num2)
{
	isZero(num1,num2);
	if ((num1 == 0 && num2 != 0) || ABS(num1) < ABS(num2))
		return 0;

	int result = 0;
	if (num1 > 0 && num2 > 0)
	{
		while (num1 >= num2)
		{
			num1 = Minus(num1, num2);
			result = Add(result, 1);
		}
	}
	else if (num1 > 0 && num2 < 0)
	{
		num2 = Negative(num2);
		while (num1 >= num2)
		{
			num1 = Minus(num1, num2);
			result = Add(result, 1);
		}
		result = Negative(result);
	}
	if (num1 < 0 && num2 < 0)
	{
		num1 = Negative(num1);
		num2 = Negative(num2);
		while (num1 >= num2)
		{
			num1 = Minus(num1, num2);
			result = Add(result, 1);
		}
	}
	else if (num1 < 0 && num2 > 0)
	{
		num1 = Negative(num1);
		while (num1 >= num2)
		{
			num1 = Minus(num1, num2);
			result = Add(result, 1);
		}
		result = Negative(result);
	}
	while (num1 >= num2)
	{
		num1 = Minus(num1, num2);
		result = Add(result, 1);
	}
	return result;
}

int Calculator(std::string &input)
{
	std::remove_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '(') ? true : false; });
	auto tmp5 = std::remove_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == ')') ? true : false; });
	input.erase(tmp5, input.end());

	//分别查找+、-、*、/

	//无要求
	auto tmp1 = std::find_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '+') ? true : false; });
	//tmp134均是end()才是运算符
	auto tmp2 = std::find_if(input.begin() + 1, input.end(),
		[](char tmp) {return (tmp == '-') ? true : false; });
	//无要求
	auto tmp3 = std::find_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '*') ? true : false; });
	//无要求
	auto tmp4 = std::find_if(input.begin(), input.end(),
		[](char tmp) {return (tmp == '/') ? true : false; });

	if (tmp1 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp1));
		int num2 = std::stod(std::string(tmp1 + 1, input.end()));
		return Add(num1, num2);
	}

	if (tmp2 != input.end() && tmp1 == input.end() && tmp3 == input.end() && tmp4 == input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp2));
		int num2 = std::stod(std::string(tmp2 + 1, input.end()));
		return Minus(num1, num2);
	}

	if (tmp3 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp3));
		int num2 = std::stod(std::string(tmp3 + 1, input.end()));
		return Multiply(num1, num2);
	}

	if (tmp4 != input.end())
	{
		int num1 = std::stod(std::string(input.begin(), tmp4));
		int num2 = std::stod(std::string(tmp4 + 1, input.end()));
		return Divide(num1, num2);
	}
}

#endif // !WEEK5_H
