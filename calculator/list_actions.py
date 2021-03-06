def add(a: list) -> int:
    s = 0
    for val in a:
        s += val
    return s


def multiply(a: list) -> int:
    s = 1
    for val in a:
        s *= val
    return s
