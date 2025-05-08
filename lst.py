
def f(ls):
    for i in range(5):
        ls[i]=i+5
    return ls

ls=[1,2,3,4,5]
arr=[6,7,8,9,0]
ls[0],arr[0]=arr[0],ls[0]

print(ls[0]," ",arr[0])
# ans=f(ls)

# for num in ls:
#     print(num)