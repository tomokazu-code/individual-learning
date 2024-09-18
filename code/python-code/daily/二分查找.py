ls1=[6,5,6,5,6,3,2,6,9,]
ls1=sorted(ls1,reverse=True)
num=0
res=0
print(ls1)
while num<=len(ls1):
    if ls1.count(ls1[num])>=2:
        res+=1
        ls1[num]-=1
    else:
        num+=1
    print(ls1)
print(res)


