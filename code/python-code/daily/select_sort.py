def select_sort(li):
    li_new=[]
    for i in range(len(li)):
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new
