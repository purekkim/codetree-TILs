# 세 개의 문자열 입력 받기
str1 = input()
str2 = input()
str3 = input()

# 문자열 길이 차 계산 함수 정의
def find_length_difference(str1, str2, str3):
    lengths = [len(str1), len(str2), len(str3)]
    mx = max(lengths)
    mn = min(lengths)
    difference = mx-mn
    return difference

# 함수 호출하여 결과 출력
print(find_length_difference(str1, str2, str3))