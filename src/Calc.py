#Operation functions
#Fun fact: the operations are ordered by time. So the first ones you see are the oldest, and the last ones are the newest.

Operations = ["+", "-", "*", "x", ".", "/", "**", "//", "%", "log", "ss", "!", "pm", "lairot", "plus-minus", "lamidu"]
a = 0

#Define Errors:
class LogError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
class SquareRootError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
class LairotError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def add (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x + y
def subtract (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x - y
def multiply (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x * y
def divide (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    if x % y == 0:
        return int(x / y)
    else:
        return x / y
def power (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x ** y
def quotinet (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x // y
def remainder_or_mod (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return x % y
def log (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    assert x > 0, "x cannot be 0 or less"
    assert y > 0, "y cannot be 0 or less"
    global a
    if y == 1:
        return 0
    if (y / x) < 1:
        raise LogError("y is not a power of x")
    elif y == x:
        return a + 1
    else:
        a += 1
        return log(x, (y / x))
def simple_sigma (x : int | float = 4)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert x > 0, "x cannot be less than 1"
    s = 0
    for i in range(x+1):
        s += i
    return s
def factorial (x : int)->int:
    assert isinstance(x, int), "x is not an integer or a floating point number"
    assert x > 1, "x cannot be less than 2"
    s = 1
    for i in range(1, x, -1):
        s *= i
    return s
def plus_minus (x : int | float, y : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    assert isinstance(y, (int, float)), "y is not an integer or floating point number"
    return (x + y, x - y)
def squareroot (x : int | float)->int:
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    s = 0
    for i in range(1, x * 2, x):
        if i == x:
            return s
        else:
            continue
    raise SquareRootError("SquareRoot of x is not a integer")
def lairot (x : int)->int:
    assert isinstance(x, int), "x is not an integer or a floating point number"
    assert x >= 2, "x cannot be less than 3"
    s = x
    for i in range(2, x):
        s /= i
        if s <= 1:
            s *= i
            break
        else:
            continue
    if int(s) < s:
        raise LairotError("Lairot of x is not a integer")
    return int(s)
def lamidu (x : int | float)->int | float: #Very very high chance of a float than a int
    assert isinstance(x, (int, float)), "x is not an integer or a floating point number"
    s = x
    for i in range(2, x):
        s /= i
    return s


#Calculate answer of question

def find_answer (args)->int | float:
    assert isinstance(args, list), "args is not a list"
    check = args[1] == "!" or args[1] == "ss" or args[1] == "lairot" or args[1] == "lamidu"
    if check:
        assert isinstance(args[0], int), f"{args[0]} inside args is not a int"
    else:
        try:
            assert isinstance(args[2], int), f"{args[2]} inside args is not a int"
            assert isinstance(args[0], int), f"{args[0]} inside args is not a int"
        except IndexError:
            raise NameError(f"{args[1]} is not a operation")
    global Operations
    assert args[1] in Operations, f"{args[1]} inside args is not a operation"
    if not check:
        Table = {
            "+" : add(args[0], args[2]),
            "-" : subtract(args[0], args[2]),
            "*" : multiply(args[0], args[2]),
            "/" : divide(args[0], args[2]),
            "**" : power(args[0], args[2]),
            "//" : quotinet(args[0], args[2]),
            "%" : remainder_or_mod(args[0], args[2]),
            "x" : multiply(args[0], args[2]),
            "." : multiply(args[0], args[2]),
            "log" : log(args[0], args[2]),
            "pm" : plus_minus(args[0], args[2]),
            "plus-minus" : plus_minus(args[0], args[2]),
        }
        return Table[args[1]]
    else:
        if args[1] == "!":
            return factorial(args[0])
        elif args[1] == "lairot":
            return lairot(args[0])
        elif args[1] == "lamidu":
            return lamidu(args[0])
        else:
            return simple_sigma(args[0])


if __name__ == '__main__':
    print("Everything works!")
    #print(log(2, 128))