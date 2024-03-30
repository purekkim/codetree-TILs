n=int(input())
arr=list(map(int,input().split()))

for i in range(n-1,-1,-1) :
    a= arr[i]
    if a%2 == 0 :
        print(a,end=" ")