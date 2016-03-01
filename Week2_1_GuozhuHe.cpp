//时间复杂度为O(n);
//本题主要难点是当被X截断的时候,获得这个X左边的O的个数
//所有我们需要三个变量
//maxNum表示 与X相连的O的最多个数
//nowNum表示  在遇到下一个X截断之前 当前与X相连的O的个数
//leftNum  当遇到X截断时候 可以利用leftNum获得这个X的左边的O的个数
//当发生截断的时候，首先去判断一下是否出现最大个数
//然后要更新这个X的左边O的数量。
void function(char *str)
{
    //记录X是否出现过
    int flag = 0;

    //maxNum表示 与X相连的O的最多个数
    int maxNum = 0;
    //nowNum表示  在遇到下一个X截断之前 当前与X相连的O的个数
    int nowNum = 0;
    //当遇到X截断时候 可以利用leftNum获得这个X的左边的O的个数
    int leftNum = 0;
    int l = strlen(str);
    for(int i = 0;i < strlen(str);++i)
    {
        if(str[i] != 'X')
        {
            ++nowNum;
            ++leftNum;
        }
        else
        {
            flag = 1;
            //遇到X的时候，截断了O。所以判断一下最大值 
            if(maxNum < nowNum)
            {
                maxNum = nowNum;
            }
            nowNum = leftNum;
            leftNum = 0;
        }
        //当到达字符串的末尾,由于没有下一个X截断了。所以要人工检测
        //此处可能出现一个BUG，就是从来没有出现X，所有判定条件利用FLAG检测X是否出现过
        if(flag == 1 && i == strlen(str) - 1)
        {
            if(maxNum < nowNum)
            {
                maxNum = nowNum;
            }
        }
    }
    printf("%d",maxNum);
}
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 10000

void function(char *str);

int main(int argc, char const *argv[])
{
    //char str[MAX_LENGTH];
    //scanf("%s",str);
    char *str = "OOOOOOOOOO";
    function(str);

    return 0;
}

void function(char *str)
{
    //记录X是否出现过
    int flag = 0;

    //maxNum表示 与X相连的O的最多个数
    int maxNum = 0;
    //nowNum表示  在遇到下一个X截断之前 当前与X相连的O的个数
    int nowNum = 0;
    //当遇到X截断时候 可以利用leftNum获得这个X的左边的O的个数
    int leftNum = 0;
    int l = strlen(str);
    for(int i = 0;i < strlen(str);++i)
    {
        if(str[i] != 'X')
        {
            ++nowNum;
            ++leftNum;
        }
        else
        {
            flag = 1;
            //遇到X的时候，截断了O。所以判断一下最大值 
            if(maxNum < nowNum)
            {
                maxNum = nowNum;
            }
            nowNum = leftNum;
            leftNum = 0;
        }
        //当到达字符串的末尾,由于没有下一个X截断了。所以要人工检测
        if(flag == 1 && i == strlen(str) - 1)
        {
            if(maxNum < nowNum)
            {
                maxNum = nowNum;
            }
        }
    }
    printf("%d",maxNum);
}
*/
