n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=list(map(int,input().split()))

avg1=sum(arr1)/4
avg2=sum(arr2)/4
avg3=sum(arr3)/4
avgrange=[avg1,avg2,avg3]

cnt=0
for i in avgrange:
    if int(i) >= 60:
        print("pass")
        cnt += 1
    else :
        print("fail")

print(cnt)