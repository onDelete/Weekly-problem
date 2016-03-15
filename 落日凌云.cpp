//* 1.无解。4 + 1 + 2，中间那个1必须走两遍或者不走才能把右边的2都利用上。【google了一下……好高端】
//* 2.前提不足以回答问题。小孩都是讨人厌的 + 有逻辑的人都不讨人厌 = 小孩都是没逻辑的 + 没逻辑的（都）会法术 
//* = 小孩会法术 + 没有不会法术又可以控制鳄鱼的人 = Unknown.
//* 这还是没办法给出结果啊，没有不会法术又可以控制鳄鱼的人的意思就是有三种人：【会法术 + 会控制鳄鱼】、
//* 【会法术但不会控制鳄鱼】、【不会法术且不会控制鳄鱼】。
//* 这谁知道小孩能不能控制鳄鱼啊。
#include <iostream>
#include <vector>
#include <algorithm>

long long MyFibonacciNumber(int i)
{
	std::vector<long long> vll{ 1,1,2 };
	for (int j = 3; j <= 93; j++)
	{
		vll.push_back(vll.at(j - 2) + vll.at(j - 1));
	}
	return vll.at(i);
}

//* 讲道理迭代没那么好用
//* long long MyFibonacci_Number(unsigned int i)
//* {
//* 	if (i <= 1)
//* 		return 1;
//* 	else
//* 		return MyFibonacci_Number(i - 1) + MyFibonacci_Number(i - 2);
//* }

//讲道理C++编译器肯定会说：妈的智障
std::vector<int>::size_type FindFunction(std::vector<int> &vi)
{
	//* 如果所有数字都是正/负数，直接返回0
	auto temp = std::find_if(vi.begin(), vi.end(), [](const int i) {return i > 0; });
	auto temp2 = std::find_if(vi.begin(), vi.end(), [](const int i) {return i < 0; });
	if (temp == vi.end() || temp2 == vi.end())
		return 0;
	else
	{
		//* 穷举
		for (std::vector<int>::size_type vs = vi.size(); vs > 1; vs--)
		{
			for (std::vector<int>::size_type j = 0; j < vi.size() + 1 - vs; j++)
			{
				int flag = 0;
				for (std::vector<int>::size_type k = j; k < vs + j; k++)
				{
					flag += vi.at(k);
				}
				if (!flag)
					return vs;
			}
		}
	}
}

int main()
{
	int n;
	std::cout << "斐波拉契数列第几项？（最高第93项）" << std::endl;
	std::cin >> n;
	std::cout << MyFibonacciNumber(n) << std::endl;
	//* 迭代函数速度慢的感人，n>=40就能感受到明显区别，n=80等了好久都没出来，
	//* 我一直以为是我写错了
	//* std::cout << MyFibonacci_Number(n) << std::endl;
	//* 第四题：
	std::vector<int> vi;
	std::cout << "请输入数列，按q+ <enter>取消输入：" << std::endl;
	while (std::cin >> n)
		vi.push_back(n);
	std::cout << FindFunction(vi);
	return 0;
}
