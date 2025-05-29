def mul(a,b):
    if b == 1:
        return a
    else:
        return a + mul(a,b-1)

print(mul(4,4))