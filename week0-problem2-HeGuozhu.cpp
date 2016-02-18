//部分程序
//时间复杂度分析：创建双向链表O(n)
//循环踢出第三个人：每次减1，直到剩余1个。时间复杂度：O(1+2+3+...+N) = O(N^2)/2
//总的时间复杂度 O(n) + O(N^2)/2 = O(N^2)/2
int function(int N)
{
    if(N < 1)
    {
        return 0;
    }
    //构造双向链表
    tNode *root = (tNode *)malloc(sizeof(tNode));
    root->num = 1;
    root->pre = root;
    root->next = root;

    tNode *temp = root;
    for (int i = 2; i <= N; ++i)
    {
        tNode *item = (tNode *)malloc(sizeof(tNode));
        item->num = i;
        item->pre = temp;
        temp->next = item;
        temp = item;

        if(i == N)
        {
            root->pre = item;
            item->next = root;
        }
    }

	/*
	temp = root;
	while(temp->next != root)
	{
		printf("num:%d pre = %d ,next = %d\n",temp->num,temp->pre->num,temp->next->num);
		temp = temp->next;
	}
	*/

    temp = root;
    int sum = 0;
    while(temp->next != temp)
    {
		sum++;
        if(sum == 3)
        {
            temp->pre->next = temp->next;
            temp->next->pre = temp->pre;
			sum = 0;
		}

        temp = temp->next;
    }

    return temp -> num;
}



//完整程序
/*
#include <cstdio>
#include <cstdlib>
#define MAXSIZE 999999
typedef struct Node tNode;
typedef struct Node
{
    int num;
    tNode *pre;
    tNode *next;
};
int function(int N);
int main(void)
{
    printf("%d", function(1));
    return 0;
}
int function(int N)
{
    if(N < 1)
    {
        return 0;
    }
    //构造双向链表
    tNode *root = (tNode *)malloc(sizeof(tNode));
    root->num = 1;
    root->pre = root;
    root->next = root;
    tNode *temp = root;
    for (int i = 2; i <= N; ++i)
    {
        tNode *item = (tNode *)malloc(sizeof(tNode));
        item->num = i;
        item->pre = temp;
        temp->next = item;
        temp = item;
        if(i == N)
        {
            root->pre = item;
            item->next = root;
        }
    }
	/*
	temp = root;
	while(temp->next != root)
	{
		printf("num:%d pre = %d ,next = %d\n",temp->num,temp->pre->num,temp->next->num);
		temp = temp->next;
	}
	*/

    temp = root;
    int sum = 0;
    while(temp->next != temp)
    {
		sum++;
        if(sum == 3)
        {
            temp->pre->next = temp->next;
            temp->next->pre = temp->pre;
			sum = 0;
		}

        temp = temp->next;
    }

    return temp -> num;
}
*/

