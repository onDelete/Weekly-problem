//*
//* @author wtlusvm
//* @date   29/03/2016
//*
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译
//* 
//* 问题1：字符串之和
//* 
//* 我们有任意一字符串包括字母（不分大小写），每个字母个代表一个唯一的数字 :
//* 
//* A, a = 1
//* B, b = 2
//* C, c = 3
//* .
//* .
//* .
//* Z, z = 26
//* 我们用一种特殊的算数方法来求得这个字符串的和，那就是：每个字母代表的数字乘以
//* 比他大的字母的个数的积，然后所有的积相加。
//* 
//* 比如 : "abca"
//* 	为 1 * 2 + 2 * 1 + 3 * 0 + 1 * 2 = 6
//* 	第一个 1 * 2 中：1是a所代表的数字，2是因为bc 比a大，所以有两个数字比他大
//* 
//* 例子 :
//* 	输入 : "abc" 输出：4
//* 	输入 : "zxy" 输出 : 73
//* 	输入 : "cccdca" 输出：17

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cctype>
#include <map>

void Preprocessor(std::vector<std::string> &vs)
{
	//* remove numbers
	auto AfterRemoveNo = std::remove_if(vs.begin(), vs.end(),
		[](const std::string s) {for (auto tmp : s) return std::isdigit(tmp); });
	vs.erase(AfterRemoveNo, vs.end());
	//* remove puncts
	auto AfterRemovePunct = std::remove_if(vs.begin(), vs.end(),
		[](const std::string s) {for (auto tmp : s) return std::ispunct(tmp); });
	vs.erase(AfterRemovePunct, vs.end());
	//* sort letters
	std::stable_sort(vs.begin(), vs.end());
}

void Calculator(std::vector<std::string> &vs)
{
	std::map<std::string, int> TransMap;
	std::vector<std::string> letters{ "a", "b", "c", "d", "e", "f", "g", "h",
		"i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
		"w", "x", "y", "z" };
	unsigned int No = 1;
	for (auto tmp : letters)
	{
		TransMap[tmp] = No;
		No++;
	}
	//* Debug
	//* std::cout << TransMap.find("a")->second;
	
	unsigned int Total = 0;
	for (auto temp : vs)
	{
		int Multiplier1 = 0;
		for (auto Position = std::find(vs.rbegin(), vs.rend(), temp);
		Position > vs.rbegin(); Position--)
		{
			Multiplier1++;
		}
		int Multiplier2 = TransMap.find(temp)->second;
		Total = Total + Multiplier1*Multiplier2;
	}
	std::cout << Total << std::endl;
}

int main()
{
	std::cout << "Enter a string:";
	std::cout << std::endl;
	std::string s;
	std::vector<std::string> vs;
	std::cin >> s;
	//* convert Uppercase into lowercase
	for (auto &tmp : s)
		tmp = std::tolower(tmp);
	for (auto tmp = s.begin(); tmp < s.end(); tmp++)
		vs.push_back(std::string(tmp, tmp + 1));
	Preprocessor(vs);
	Calculator(vs);
	return 0;
}
