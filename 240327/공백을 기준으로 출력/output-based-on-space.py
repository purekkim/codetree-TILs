str1=input()
str2=input()
result=''

combined_strings =str1+str2
for char in combined_strings :
    if char !='':
        result += char

print(result)