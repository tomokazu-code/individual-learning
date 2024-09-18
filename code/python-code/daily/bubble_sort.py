def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            return
x=[6,9,6,4,8,7,6,2,1,5,6]
bubble_sort(x)
print(x)
