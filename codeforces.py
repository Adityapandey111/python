t=int(input())

while(t > 0):
    n,x=map(int,input().split())
    # x=int(input())

    if x>=n:
        ans=[]
        for i in range(n):
            print(i,end=" ")
    else:
        for i in range(n):
            if i==x:
                continue
            else:
                print(i,end=" ")
        print(x)
    t-=1