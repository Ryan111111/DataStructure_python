def bubble_sort_norec(lists):
    '''
    冒泡排序 非递归，两层循环
    :param lists:
    :return:
    '''
    count=len(lists)
    for i in range(count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists

def bubble_sort_rec(A,i):
    '''
    冒泡排序，递归版本,一层循环
    :param A:
    :param i:
    :return:
    '''
    if i == 1:
        return
    for j in range(i-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
    bubble_sort_rec(A,i-1)


A = [1,3,5,2,9,4]
bubble_sort_rec(A,len(A))
print(A)

bubble_sort_norec(A)
print(A)



