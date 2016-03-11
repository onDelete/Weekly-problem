//*
//* @author wtlusvm
//* @date   11/03/2016
//*
//* !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//* !!  由于代码中含有range for语句，在编译时务必加上"-std=c++11"  !!
//* !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//*
//* 问题1：
//* 在北京工作的程序员小明今年过年要回老家，可是对于一个工作繁忙的程序员来说，
//* 如何给家里那么多亲戚朋友选择礼物确实是一个头疼的问题。你能不能帮帮他呢？
//* 你的任务是帮他在北京机场的礼品店里买更可能多的礼物。 你有 X 元钱，
//* 而商店里可供选择的商品是由一个list / array表示的，其中每一项由那个商品的价格代表。
//* （第i个项是第i个商品的价格） 每个商品在商店里只有一个，你的目标是买尽可能"多"的礼物。
//* 你需要写一个function，里面的第一个输入是你所有的钱X， 第二个输入是商品的list：

#include <iostream>
#include <vector>
#include <algorithm>

//* Charge为当前零钱，Price为商品价格列表
int Week0Problem1(double &Charge, std::vector<double> &Price)
{
	//将商品按价格从小到大排序
	std::stable_sort(Price.begin(), Price.end(),
		[](const double &p, const double &q) {return p <= q; });
	int i = 0;
	for (auto &e : Price)
	{
		//如果可以买当前商品
		if (Charge - e >= 0)
		{
			++i;
		}
	}
	return i;
}

int main()
{
	double Charge;
	std::cout << "请问当前你还有多少钱？";
	std::cin >> Charge;
	std::vector<double> Price;
	double p;
	std::cout << std::endl << "现在输入每种商品价格列表，输入非数字以结束输入"
		<< std::endl;
	while (std::cin >> p)
		Price.push_back(p);
	std::cout << "你当前有 " << Charge << " 元，可以购买 " <<
		Week0Problem1(Charge, Price) << " 件商品。";
	return 0;
}
