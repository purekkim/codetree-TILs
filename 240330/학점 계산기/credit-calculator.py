n = int(input())
arr = list(map(int,input().split()))

avg= sum(arr)/n

def print_avg():
    if avg >= 4.0 :
        print("Perfect")
    elif avg >= 3.0 :
        print("Good")
    else :
        print("Poor")

print(f"{avg:.1f}")
print_avg()