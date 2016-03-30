//* 
//* @author wtlusvm
//* @date   29/03/2016
//* 
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译
//* 

#include "Week5Question2.h"

void Autotroph::Reproduce(Autotroph &a,int &i)
{
	if (i == 1 && !FirstDayReproduction)
		;
	else
		a.Amount = a.Amount * 2;
}

bool Autotroph::isAvailable(Autotroph &a)
{
	if (a.Amount > 2)
		return true;
	else
		return false;
}

int& Autotroph::itsAmount(Autotroph &a)
{
	return a.Amount;
}

bool Consumer::isAvailable(Consumer &ca, Consumer &cb)
{
	if (ca.Level < cb.Level && ca.Amount > 2)
		return true;
	else
		return false;
}

void Consumer::Reproduce(Consumer &ca, Consumer &cb,int &i)
{
	//* 第一天的繁殖 || 以后繁殖
	if ((i == 1 && cb.FirstDayReproduction && ca.isAvailable(ca, cb)) ||
		((i - 1) % cb.Interval == 0 && ca.isAvailable(ca, cb)))
	{
		//如果一级消费者能够供给所有二级消费者繁殖
		if ((ca.Amount - 2) >= (cb.Amount / 2 * 2))
		{
			ca.Amount = ca.Amount - cb.Amount / 2 * 2;
			cb.Amount = cb.Amount + cb.Amount / 2;
		}
		//一级消费者不能供给所有二级消费者繁殖
		else
		{
			int temp = (ca.Amount - 2) / 2;
			ca.Amount = ca.Amount - temp * 2;
			cb.Amount = cb.Amount + temp;
		}
	}
	//以后的繁殖
	//if ((i - 1) % cb.Interval == 0 && ca.isAvailable(ca, cb))
	//{
	//	ca.Amount = ca.Amount - cb.Amount / 2 * 2;
	//	cb.Amount = cb.Amount + cb.Amount / 2;
	//}
}

void Consumer::Reproduce(Autotroph &a, Consumer &c,int &i)
{
	//第一天繁殖 || 以后的繁殖
	if ((i == 1 && c.FirstDayReproduction && a.isAvailable(a)) ||
		((i - 1) % c.Interval == 0 && a.isAvailable(a)))
	{
		//如果生产者能够供给所有一级消费者繁殖
		if ((a.itsAmount(a) - 2) >= (c.Amount / 2 * 2))
		{
			a.itsAmount(a) = a.itsAmount(a) - c.Amount / 2 * 2;
			c.Amount = c.Amount + c.Amount / 2;
		}
		//生产者不能供给所有一级消费者繁殖
		else
		{
			int temp = (a.itsAmount(a) - 2) / 2;
			a.itsAmount(a) = a.itsAmount(a) - temp * 2;
			c.Amount = c.Amount + temp;
		}
	}
	//if ((i - 1) % c.Interval == 0 && a.isAvailable(a))
	//{
	//	a.itsAmount(a) = a.itsAmount(a) - c.Amount / 2 * 2;
	//	c.Amount = c.Amount + c.Amount / 2;
	//}
}

int Calculator(Autotroph &a, Consumer &ca, Consumer &cb, int &No)
{
	int i = 1;
	for (; cb.Amount < No; i++)
	{
		cb.Reproduce(ca, cb, i);
		ca.Reproduce(a, ca, i);
		a.Reproduce(a, i);
	}
	return i;
}
