arr=list(map(int,input().split()))
n=len(arr)
sum_val=0
for i in range(n-1):
    if arr[i]==0 :
        break
    sum_val += arr[i]
print(sum_val)