#include "stdio.h"
#include "stdbool.h"

typedef int ElemType;

typedef struct Node
{
    ElemType data;
    struct Node * next;
}LNode,*LinkList;

//创建链表
bool InitList(LinkList &L){
    L=new LNode;
    L->next=NULL;
    return true;
}

//取数 （ 传入头结点，取得第几个数，返回的数）
bool GetElem(LinkList L,int i,ElemType &e){
    if (i<1){return false;}
    LinkList p=L;
    int j=0;
    while(p->next&&j<i){
        p=p->next;
        j++;
    }
    if(!p||j>i){return false;}
    e=p->data;
    return true;
}

//插入数据(,插入的位置，插入的元素)
bool InsertList(LinkList &L,int i,ElemType e){
    if (i<1){return false;}
    LinkList p=L;
    int j=0;

    LinkList q=new LNode;
    q->data=e;
    while (p&&j<(i-1)) //要找到i-1的位置
    {
        p=p->next;
        j++;
    }
    if(!p){
        return false;
    }
    q->next=p->next;
    p->next=q;
    return true;
}

//输出函数
bool PrintList(LinkList L){
    LinkList p;
    p=L->next;
    while(p){
        printf("%d\n",p->data);
        p=p->next;
    }
    return true;
}

//求链表长度
int ListLength(LinkList L){
    int len;
    LinkList p=L->next;
    while(p){
        len++;
        p=p->next;
    }
    return len;
}

//删除元素(,删除的位置，删除元素存放到e)
bool deleteElem(LinkList &L,int i,ElemType e){
    if (i<1)return false;
    LinkList p=L;
    int j=0;
    while(p&&j<(i-1)){
        p=p->next;
        j++;
    }
    e=p->next->data;
    LinkList q;
    q=p->next;
    p->next=p->next->next;
    delete q;
    return true;
}
//头插法(,n长度)
bool HeadCreateList(LinkList &L,int n){
    LinkList s;
    L=new LNode;
    L->next=NULL;
    for (int i = 1; i <= n; i++)
    {
        s=new LNode;
        scanf("%d",&s->data);
        s->next=L->next;
        L->next=s;

    }
    return true;
    
}
//尾插法
bool TailCreateList(LinkList &L,int n){
    L=new LNode;
    LinkList s,r=L;
    for(int i=1;i<=n;i++){
        s=new LNode;
        scanf("%d",&s->data);
        r->next=s;
        r=s;
    }
    r->next=NULL;

    return true;
}



int main(){
    LinkList L;
    InitList(L);
    InsertList(L,1,7);
    InsertList(L,2,54);
    PrintList(L);
    int i;
    i=ListLength(L);
    printf("%d\n",i);
    ElemType e;
    deleteElem(L,1,e);
    PrintList(L);
    HeadCreateList(L,3);
    PrintList(L);
    TailCreateList(L,3); 
    PrintList(L);
    return 0;
    
}
