arr=list(map(int,input().split()))

sum_val=0
for i in range(int(len(arr))) :
    sum_val += int(arr[i])

print(sum_val)