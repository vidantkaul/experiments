import matplotlib.pyplot as plt

class Error: ...
def cn2l (n : int)->list[int]:
    check = str(n)
    L = []
    q = n
    r = 0
    for _ in range(len(check)):
        r = q % 10
        q = q // 10
        L.append(r)
        if q == 0:
            break
    L.reverse()
    return L

def cl2n (L : list):
    copy = L.copy()
    n = 0
    for i, d in enumerate(copy):
        n += d * 10 ** (len(copy) - 1 - i)
    return n

def BAS (L : list):
    copy = L.copy()
    copy.sort()
    l1 = copy.copy()
    copy.reverse()
    return (cl2n(l1), cl2n(copy))

def _play (n : int, do_print: bool = True)->tuple[int, int]:
    assert isinstance(n, int), "ValueError"
    count = 0
    a = n
    if do_print: print(a)
    while True:
        L1 = cn2l(a)
        S,B = BAS(L1)
        m = B - S
        if m == a:
            break
        else:
            a = m
            count += 1
            if do_print: print(a)
            
    return (a, count)

if __name__ == '__main__':
    H = {}
    L1 = []
    L2 = []
    for i in range(1000, 10000):
        v, c = _play(i, False)
        hkey = (v, c)
        if hkey not in H: H[hkey] = []
        H[hkey].append(i)

        L1.append(i)
        L2.append(c)

    for k in H:
        print(k, len(H[k]), H[k])
        print()
    exit(0)
    plt.title("New law graph")
    plt.plot(L1, L2)
    plt.show()
