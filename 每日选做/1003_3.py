import re

s = input().lower()

result = re.sub(r'(.)\1*', lambda m: f'({m.group(1)},{len(m.group(0))})', s)

print(result)
