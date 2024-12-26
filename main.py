ls=[35,65,4,756,232,76,67,345,32,56]
for i in range(1,len(ls)):
    for j in range(i):
        if ls[i]<ls[j]:
            ls[i]+=ls[j]
            ls[j]=ls[i]-ls[j]
            ls[i]-=ls[j]
print(ls)



        