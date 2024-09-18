import itertools
falg=0
fuhao=["+","-","*","/"]

num=[0,0,0,0]
print("请输入四个数字")
num[0],num[1],num[2],num[3]=map(int,input().split())

for i in itertools.permutations(fuhao,3):
    for j in itertools.permutations(num):
        a,b,c,d=j[0],j[1],j[2],j[3]
        x,y,z=i[0],i[1],i[2]
        if eval('((%d%c%d)%c%d)%c%d'%(a,x,b,y,c,z,d))==24:
            falg=1
            print('((%d%c%d)%c%d)%c%d=24'%(a,x,b,y,c,z,d))
            break
        elif eval('(%d%c(%d%c%d))%c%d'%(a,x,b,y,c,z,d))==24:
            falg = 1
            print('(%d%c(%d%c%d))%c%d=24'%(a,x,b,y,c,z,d))
            break
        elif eval('%d%c(%d%c(%d%c%d))'%(a,x,b,y,c,z,d))==24:
            falg = 1
            print('%d%c(%d%c(%d%c%d))=24'%(a,x,b,y,c,z,d))
            break
        elif eval('%d%c((%d%c%d)%c%d)'%(a,x,b,y,c,z,d))==24:
            falg = 1
            print('%d%c((%d%c%d)%c%d)=24'%(a,x,b,y,c,z,d))
            break
        elif eval('(%d%c%d)%c(%d%c%d)'%(a,x,b,y,c,z,d))==24:
            falg = 1
            print('(%d%c%d)%c(%d%c%d)=24'%(a,x,b,y,c,z,d))
            break
    if falg==1:
        break
if falg==0:
    print("输入的数字不符合")

