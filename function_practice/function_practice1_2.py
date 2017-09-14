def print_string(s, result=None):
    'this is an explaination on this function'
    if s == 'red':
        print('apple')
    elif s == 'yellow':
        print('banana')
    elif s == 'green':
        print('melon')
    else:
        print("I don't know")
    return result

print_string('red')
print_string('yellow')
print_string('green')
print_string('blue')
#help(print_string)
