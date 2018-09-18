from optional import optional_of_nullable, optional_of, empty


def product(x, y):
    if x is None or y is None:
        return 0
    else:
        return x * y


def sum(x, y):
    if x is None and y is None:
        return 0
    elif x is None:
        return y
    elif y is None:
        return x
    return x + y
