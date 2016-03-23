#include <iostream>
#include <vector>
#include <string>
#include <climits>

bool ispalindrome(const std::string &s)
{
	return (s == std::string(s.crbegin(), s.crend()));
}

void reversestring(const std::string &s)
{
	if (ispalindrome(s))
	{
		std::cout << "palindrome" << std::endl;
	}
	else
	{
		for (auto i = s.rbegin(); i < s.rend(); i++)
			std::cout << *i;
		std::cout << std::endl;
	}
}

void decrypt(std::vector<std::string> &s,std::vector<unsigned int> &vi)
{
	std::vector<std::string> temp(s);
	for (std::vector<std::string>::size_type i = 0; i < s.size(); i++)
		s.at(i) = temp.at(vi.at(i));
}

int main()
{
	std::string s;
	std::cout << "Week1,Question 1:\nInput a word please:";
	std::cin >> s;
	reversestring(s);
	//* Question 2:
	std::vector<std::string> vs;
	std::cout << "Week1,Question 1:\nInput a word letterly (enter \"quit\" to end input):" << std::endl;
	while (std::cin >> s && s != "quit")
	{
		vs.push_back(s);
	}
	std::vector<unsigned int> vi;
	unsigned int n;
	std::cout << "Input sequence (enter \"-1\" to end input) :" << std::endl;
	while (std::cin >> n && n !=_UI32_MAX)
	{
		vi.push_back(n);
	}
	if (vi.size() != vs.size())
		std::cout << "The word should have " << vi.size()
		<< " letters, that is, as long as max number of sequence." << std::endl;
	std::cout << "What is the individual number:";
	unsigned int j = 0;
	//std::cin.clear();
	std::cin >> j;
	for (unsigned int i = 0; i < j; i++)
		decrypt(vs, vi);
	for (auto &out : vs)
		std::cout << out;
	std::cout << std::endl;
	return 0;
}
