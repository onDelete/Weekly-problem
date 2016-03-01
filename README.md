# Weekly-problem
知乎编程学习群每周一题

知乎编程学习群每周一题 Week 2 2016/2/29-2016/3/6

还是两题选做一题，第一题不简单，第二题较难。

问题1： 一维OX

给你一串包含'X'和'O'字符串，如"OXOOOXXXOXXOOOXXXOXO",问这个字符串中，与其中一个X直接相连的O最多有多少个？比如"OXOO",就有三个O与X相连。但是"OXOOOXOO"最多就是五个而不是六个，因为左边的X挡住了最左边的O。

	输入：字符串 输出：整数
	
	例子：
	输入:"OXO"			输出：2
	输入:"OXOOXOXXOOOXO"	输出：3
	输入:"OOXOOOXOXO"		输出：5
	输入:"OOOOOOOOOO"	 	输出：0
	输入:"XXX"			输出：0


问题2: 二维OX

给你一串字符串，一个整数代表每行字符的个数，求与其中一个X直接相连的O最多有多少个？（跟上题一样）

	直接上例子：
		输入："OXOOOXOXOXOXXOX"， "5" 输出：3
		其图像为：
		OXOOO
		XOXOX
		OXXOX
		
		输入："OXOOOXOXOXOXXOX"， "10" 输出：2
		其图像为：
		OXXOXOOXOX
		OXOOXOOXOX
		
		输入："XOOXOOOOOOXOOXOXXXOX"， "5" 输出：4
		其图像为：
		XOOXO
		OOOOO
		XOOXO
		XXXOX
	
		显而易见，输出最小是0，最大只可能是4.
	
	
