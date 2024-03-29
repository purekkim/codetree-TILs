def solution():
    n, m = map(int, input().split())
    return n, m

def print_rect(n, m):
    for _ in range(n):
        print("1" * m)

row_num, col_num = solution()
print_rect(row_num, col_num)