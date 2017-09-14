def mul(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]

print(mul(3))
print(mul(9, 8))
