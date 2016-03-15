//**********************************************************************
//* 要编译我上传的cpp文件请将此文件文件名改为"week4.h"，否则无法编译！ *
//**********************************************************************

#ifndef  WEEK4_H
#define  WEEK4_H

#include <iostream>
#include <algorithm>
#include <vector>

class LongEqual2Zero {
public:
	LongEqual2Zero(std::vector<int> vi) : member(vi) {  }
	friend std::vector<int>::size_type FindFunction(LongEqual2Zero &vi);
private:
	std::vector<int> member;
};

//讲道理C++编译器肯定会说：妈的智障
std::vector<int>::size_type FindFunction(LongEqual2Zero &vi)
{
	//* 如果所有数字都是正/负数，直接返回0
	auto temp = std::find_if(vi.member.begin(), vi.member.end(), [](const int i) {return i > 0; });
	auto temp2 = std::find_if(vi.member.begin(), vi.member.end(), [](const int i) {return i < 0; });
	if (temp == vi.member.end() || temp2 == vi.member.end())
		return 0;
	else
	{
		//* 穷举
		for (std::vector<int>::size_type vs = vi.member.size(); vs > 1; vs--)
		{
			for (std::vector<int>::size_type j = 0; j < vi.member.size() + 1 - vs; j++)
			{
				int flag = 0;
				for (std::vector<int>::size_type k = j; k < vs + j; k++)
				{
					flag += vi.member.at(k);
				}
				if (!flag)
					return vs;
			}
		}
	}
}

#endif // ! WEEK4_H

