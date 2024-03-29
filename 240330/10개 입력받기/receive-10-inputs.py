arr=list(map(int,input().split()))

cnt=0
for i in arr:
    if i==0:
        break
    cnt +=1

sum_val=sum(arr[:cnt])
avg_val=(sum_val)/(cnt)

print(sum_val,f"{avg_val:.1f}")