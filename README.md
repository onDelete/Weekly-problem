知乎编程学习群每周一题

知乎编程学习群每周一题 Week 5 2016/3/28 - 2016/4/3

大家有什么问题可以直接在这个文件上端留言，群里问问题有时候看不到，可以直接在这上面交流。
有些同学觉得题简单啊或者麻烦啊，我有时候抽看同学的答案，有些是错的，有些是太复杂。大家做题前可以好好想想有没有什么更简单的写法，如果觉得哪题不好的话可以跳过，做自己感兴趣的就好了，学习编程很多时候都是自己思考的一个过程。


问题1：字符串之和

我们有任意一字符串包括字母（不分大小写），每个字母个代表一个唯一的数字:
	
	A,a = 1
	B,b = 2
	C,c = 3
	.
	.
	.
	Z,z = 26
	
	
我们用一种特殊的算数方法来求得这个字符串的和，那就是：每个字母代表的数字乘以比他大的字母的个数的积，然后所有的积相加。
	
	比如:"abca"
	为 1 * 2 + 2 * 1 + 3 * 0 + 1 * 2 = 6
	第一个 1 * 2 中：1是a所代表的数字，2是因为bc 比a大，所以有两个数字比他大

	例子:
	输入:"abc" 输出：4
	输入:"zxy" 输出: 73
	输入:"cccdca" 输出：17


问题2：草原模拟题 （我觉得这道题比较有趣）

有一片草原上生活着兔子和狼，当然还有草。草，兔子和狼的个数分别是x,y,z。
他们的生物链规则是这样的，每两只兔子可以生一只兔子，每两条狼可以生一只狼。但是他们繁育的条件是必须吃掉相同个数的食物，比如两只兔子要想生一只小兔子，那他们就要吃两根草。草的个数每天都是以二的倍数生长着。比如第一天有3根草，第二天就有6根。我们还要设个规定，草是每天都生长的，但是兔子是每两天吃一次草，狼是每三天吃一次兔子（第一天他们都吃）。

在这个问题里，我们假设生物都不会自然死亡。而如果食物的个数小于等于2，他们就得等。

	举个栗子：
	假如一开始有4根草，2只兔子，2条狼。那么第一天兔子可以吃草，狼不能吃兔子，而草可以生长。他们行动的顺序是狼->兔子->草。
	那么第一天（初始值）: 	x = 4 y = 2 z = 2 (草兔子狼都想繁育）
	第二天:		x = 4 y = 3 z = 2 （草想繁育）
	第三天:		x = 8 y = 3 z = 3  （草兔子想繁育）
	第四天：	x = 12 y = 4 z = 3 （草兔子狼想繁育）
	第五天：	x = 20 y = 3 z = 4  （草想繁育）

问题是，假如草原上一开始有50根草，13只兔子，3条狼，那么多少天后狼的数量能达到 50 呢？
