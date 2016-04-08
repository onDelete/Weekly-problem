#include <iostream>
using std::string;

int chSum(string initString);

int main()
{
	string initString = "cccdca";
	printf("%d", chSum(initString));
	return 0;
}

int chSum(string initString)
{
	int len = initString.length();
	int ascii_set[256] = { 0 };

	for (int i = 0; i < len; ++i)
	{
		char temp = tolower(initString[i]);
		++ascii_set[(int)temp];
	}
	int num = 0;
	int sum = 0;
	for (size_t i = (int)'z'; i >= (int)'a'; --i)
	{
		if (ascii_set[i] != 0)
		{
			sum += ((i- (int)'a' + 1)*num*ascii_set[i]);
			num += ascii_set[i];
		}
	}
	return sum;
}
