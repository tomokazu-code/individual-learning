#hanio汉诺塔问题
def hanio(n,first,second,third):
    if n==1:
        print("moving from",first,"to",third)
    else:
        hanio(n-1,first,third,second)
        print(f"moving from {first} to {third}")
        hanio(n-1,second,first,third)
hanio(100,'A','B','C')
