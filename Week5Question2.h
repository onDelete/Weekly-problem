//* 
//* @author wtlusvm
//* @date   29/03/2016
//* 
//* 代码中含有C++11语言特性，请使用支持C++11的编译器编译
//* 

#ifndef WEEK5_QUESTION2_H
#define WEEK5_QUESTION2_H

class Consumer;
class Autotroph
{
public:
	friend int Calculator(Autotroph &a, Consumer &ca, Consumer &cb, int &No);
	Autotroph(int a,bool f):Amount(a),FirstDayReproduction(f) {}
	Autotroph(int a):Amount(a),FirstDayReproduction(true) {}
	Autotroph(const Autotroph &) = default;
	Autotroph& operator=(const Autotroph &) = default;
	~Autotroph() = default;
	void Reproduce(Autotroph &a, int &i);
	bool isAvailable(Autotroph &a);
	int& itsAmount(Autotroph &a);
private:
	int Amount;
	bool FirstDayReproduction;
};

class Consumer
{
public:
	friend int Calculator(Autotroph &a, Consumer &ca, Consumer &cb, int &No);
	Consumer(int a, int i) :Amount(a), Level(1), Interval(i), FirstDayReproduction(true) {}
	Consumer(int a, int l, int i) :Amount(a), Level(l), Interval(i), FirstDayReproduction(true) {}
	Consumer(int a, int l, int i, bool f) :Amount(a), Level(l), Interval(i), FirstDayReproduction(f) {}
	Consumer(const Consumer &) = default;
	Consumer& operator=(const Consumer &) = default;
	~Consumer() = default;
	void Reproduce(Consumer &ca, Consumer &cb, int &i);
	void Reproduce(Autotroph &a, Consumer &c, int &i);
	bool isAvailable(Consumer &ca, Consumer &cb);
private:
	int Amount;
	int Level;
	int Interval;
	bool FirstDayReproduction;
};

#endif // !WEEK5_QUESTION2_H
