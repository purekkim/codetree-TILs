def solution():
    n = int(input())
    num = input()
    return n,num

# n개의 줄에 걸쳐 특정 문자열을 출력하는 함수입니다.
def print_num(n,num):  
    cnt=0
    for _ in num:
        print(cnt,end="")
        cnt+=1
    
print_num(n,num)