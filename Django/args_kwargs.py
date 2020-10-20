def plus(a, b, *args, **kwargs):
    print(args)     # Tuple
    print(kwargs)   # Dictionary
    return a+b

def all_plus(*args):
    result = 0
    for number in args:
        result += number
    print(result)
    return result

plus(1, 12, 3425, 2, 4, 2, 2, 5, 1, hello=True, aa=False, bsd="asdf")

# (3425, 2, 4, 2, 2, 5, 1)
# {'hello': True, 'aa': False, 'bsd': 'asdf'}

all_plus(1, 43, 23, 546, 352, 2346) # 3311