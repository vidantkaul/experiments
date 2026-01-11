def add (x : int | float, y : int | float): return x + y
def sub (x : int | float, y : int | float): return x - y
def mul (x : int | float, y : int | float): return x * y
def div (x : int | float, y : int | float):
    if y == 0: raise ZeroDivisionError("y cannot be 0")
    else: return x / y
def quotient (x : int | float, y : int | float):  return x // y
def remainder (x : int | float, y : int | float): return x % y
def power (x : float, y : float):                 return x ** y
def squareroot (x : int, y : int):
    assert isinstance(x, int), "x is not an int"
    assert isinstance(y, int), "root is not an int"
    assert y > 1, "root cannot be negitive"
    ans = None
    if x % 2 == 0:
        for i in range(int(x/2)):
            ans = i ** y
            if ans == x:
                return i
            else:
                continue
    else:
        for i in range(x):
            ans = i ** y
            if ans == x:
                return i
            else:
                continue
    return f"squareroot of {x} is not an int"
def log (x : int, y : int = 10):
    assert isinstance(x, int), "x is not an int"
    assert isinstance(y, int), "y is not an int"
    assert x > 0, "x cannot be 0 or less"
    if x < y:
        return 0
    elif x == y:
        return 1
    count = 1
    n = x
    while True:
        n /= y
        if (n * 2) // 2 != n:
            raise ValueError(f"{x} is not a power of 10")
        elif n == y:
            break
        else:
            count += 1
    return count + 1
def round_up (x : int, y : int):
    assert isinstance(x, int), "x is not an int"
    assert x > 0, "x is <= 0"
    assert isinstance(y, int), "y is not an int"
    assert y > 0, "y is <= 0"
    ex = log(y)
    s = str(x)[-ex:]
    return x + (y - int(s))
def round_down (x : int, y : int):
    assert isinstance(x, int), "x is not an int"
    assert x > 0, "x is <= 0"
    assert isinstance(y, int), "y is not an int"
    assert y > 0, "y is <= 0"
    ex = log(y)
    s = str(x)[-ex:]
    return x - (y + int(s))
def gcd (x : int, y : int)->int:
    assert isinstance(x, int), "x is not an int"
    assert isinstance(y, int), "y is not an int"
    if x < y: x, y = y, x
    z = x % y
    if z == 0: return y
    else: return gcd(y, z)
def sigma (end : int | float, start : int | float = 1, steps : int | float = 1):
    assert isinstance(start, (int, float)), "start is not an int or an float"
    assert isinstance(end, (int, float)), "end is not an int or an float"
    assert isinstance(steps, (int, float)), "steps is not an int or an float"
    s = start
    for i in range(start, end, steps): s += i
    return s
