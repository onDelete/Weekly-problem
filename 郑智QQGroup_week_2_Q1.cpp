/************************************************************
*Copyright © 2015年 Dragon. All rights reserved.
*FileName: QQGroup_week_2_Q1.c
*Author: dragon
*Description:通过循环遍历每一个元素若是o则跳过。若是x则检查这个元素相邻的元素若是o则计数，若是x则退出判断；
*Version : 1.0
*Input: 任意一串只有'o','x'的字符串；
*Output: 输出就是所问
*Return: 
*Date: 3/3/2016  by dragon
*other: 新生程序烂 只会用最简单的方法
***********************************************************/
#include <stdio.h>
#include "string.h"
#define  N 100
int main() {
	char str[N];
	int i,j,k,m,n,max = 0,num = 0;
	printf("输入只有‘o’ ‘x’ 的一串字符")
	gets(str);
	//从第一个元素开始判断
	for(i = 0;i<strlen(str);i++){
		//若这个元素是o则跳过，第一个元素是X，则前面不进行判断
		if (str[i] == 'o') continue;
		//元素若是X，则判断这个元素前面的O的个数；
		for(j=i-1,n=0;str[j]=='o';j--){
			if (j < 0) break;
			//进行累加计数
			n++;
		}
		//判断X元素后面O的个数
		for(k=i+1,m=0;str[k]=='o'&&k<strlen(str);k++){
			m++;
		}
		//将前后相加；然后使用冒泡原理求出最大数字；
		num = m+n;
		if (num>=max) {
			max = num;
		}
	}
	//最大的数字就是相邻o最多的
	printf("相邻个数最多为%d",max);
	return 0;
}
