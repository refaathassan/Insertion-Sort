ls=[35,65,4,756,232,76,67,345,32,56]
def insetion_sort(Arr):
    for i in range(1,len(Arr)):
        for j in range(i):
            if Arr[i]<Arr[j]:
                Arr[i]+=Arr[j]
                Arr[j]=Arr[i]-ls[j]
                Arr[i]-=Arr[j]
    return Arr
arr=insetion_sort(ls)
print(arr)



        