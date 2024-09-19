#include "stdio.h"
#include "stdbool.h"
#include "stdlib.h"

typedef struct 
{
    char *elem;
    int length; //当前的位置
    int maxsize=50;  //最大长度
}SqList;

//初始化线性表
bool InitList(SqList &L){
    L.elem=new char[L.maxsize];
    if (!L.elem)return false;
    L.length=0;
    return true;
}

//取值 (引用L  ,  获得第i个值 , 将获得的值存入e中)
bool GetElem(SqList &L,int i,int &e){
    if (i<1 || i>L.length)return false;
    e=L.elem[i-1];
    return true;
}


//查找 (将要查找的L传入函数 ，传入要查找的元素， 把查找到的序号存入num)
bool FindElem(SqList L,int e,int &num){
    for(int i=0;i<L.length;i++ ){
        if (L.elem[i]==e){
            num=i+1;
            return true;//当查找到时结束循环,返回true
        }
    }
    return false;//没有找到，返回false
}

//插入元素   (要插入的表L  ,  插入的位置 ,  插入的元素)  
bool InsertList(SqList &L,int i,int e){
    if (i<1 or i>L.length+1)return false;
    //如果内存不够用，将maxsize扩大两倍
    if (L.length==L.maxsize){
        int NewMaxsize=(L.maxsize)*2;
        char *newElem=(char*)realloc(L.elem,NewMaxsize*sizeof(char));
        L.elem=newElem;
    }
    //从表的最末尾元素开始移动，一直到要插入的位置
    for (int j=L.length-1;j>=i-1;j--){ 
        L.elem[j+1]=L.elem[j];
    }
    L.elem[i-1]=e;
    ++L.length;
    return true;
}

//删除元素   (要删除元素的表L，要删除元素的序号，把删除的元素保存到e中后续使用)
bool DelElem(SqList &L,int i ,int &e){
    if (i<1 or i>L.length+1)return false;
    e=L.elem[i-1];
    for (int j=i-1;j<L.length;j++){
        L.elem[j]=L.elem[j+1];
    }
    --L.length;
    return true;
}

//输出顺序表
void PrintList(SqList L){
    for(int i=0;i<L.length;i++){
        printf("%d\n",L.elem[i]);
    }
}

int main(){
    SqList L;
    InitList(L);
    InsertList(L,1,1);
    InsertList(L,2,2);
    InsertList(L,3,3);
    InsertList(L,4,4);
    int i,num;
    DelElem(L,2,i);
    FindElem(L,1,num);
    printf("%d",num);
    PrintList(L);
    return 0;

}

