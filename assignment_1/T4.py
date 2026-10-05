n, m, a = map(int, input().split())
width = min(n, m)
length = max(n, m)

if a >= length:
    print(1)
elif width < a < length:
    if length % a == 0:
        print(length // a)
    else:
        print(length // a + 1)
else:
    if length % a == 0 and width % a == 0:
        print((length // a) * (width // a))
    elif length % a == 0 and width % a != 0:
        print((length // a) * (width // a + 1))
    elif length % a != 0 and width % a == 0:
        print((length // a + 1) * (width // a))
    else:
        print((length // a + 1) * (width // a + 1))
