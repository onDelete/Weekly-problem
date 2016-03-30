#include "stdio.h"
#include "malloc.h"

//用链表实现
struct node
{
    int val;
    struct node *next;
};

struct node* createList(int n){
    int i;
    struct node *head, *tmp, *cur;
    for (i = 0; i < n; i++){
        tmp = (struct node *)malloc(sizeof(struct node));
        tmp->val = i + 1;
        tmp->next = NULL;
        if(i == 0){
            head = tmp;
            cur = tmp;
        } else {
            cur->next = tmp;
            cur = tmp;
        }
    }
    cur->next = head;
    return head;
}

void deleteNode(struct node *node){
    struct node* tmp = node->next;
    node->next = tmp->next;
    free(tmp);
}

void printList(struct node* node){
    int i;
    for (i = 0;i < 10; i++){
        printf("%d\t\n", node->val);
        node = node->next;
    }
}

int function(int n){
    int i = 1;
    struct node* head;
    head = createList(n);
    for (i = 0; i < (n - 1) * 2; i++){
        if (i % 2 == 1 && i != 0)
        {
            deleteNode(head);
            head = head->next;
        } else {
            head = head->next;
        }
    }
    return head->val;
}

int main(int argc, char const *argv[])
{
    int n = 5;
    printf("%d\n", function(n));
    return 0;
}
