//第一句话：要控制鳄鱼必须会法术。
//第二句话：没逻辑的人都讨厌。
//第三句话：没逻辑的会法术。
//第四句话：小孩都是讨厌的。
//4——>2——>3——>1，小孩会控制鳄鱼
#include <stdio.h>
//递归函数
int arr(int i){
    if(i == 1|| i ==0)
        return 1;
    else{
            return arr(i-1)+arr(i-2);
        }
}
int main() {
    int n,k;
    printf("输入项数n：");
    scanf("%d",&n);
    k = arr(n-1);
    printf("第%d项该数字为%d\n",n,k);
}
