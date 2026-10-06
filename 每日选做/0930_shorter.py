import re

input_string = input().strip()

# 正则表达式
numbers = re.findall(r'\d+', input_string)

for number in numbers:
    print(int(number))
