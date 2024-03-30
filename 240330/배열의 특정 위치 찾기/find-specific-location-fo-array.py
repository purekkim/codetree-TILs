arr=list(map(int,input().split()))

n=len(arr)

cnt=0
sum_even=0
sum_val=0
for i in range(1,n,2):
    sum_even += arr[i]
for i in range(2,n,3):
    sum_val += arr[i]
    cnt += 1
    
avg=sum_val/cnt
print(sum_even,f"{avg:.1f}")