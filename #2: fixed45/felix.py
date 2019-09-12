def main(n):
    a = []
    b = []

    l = len

    def f(a, b):
        n[a], n[b] = n[b], n[a]

    for i in range(l(n)):
        v = n[i]

        if v == 5 and n[i - 1] != 4:
            if l(b) == 0:
                a += [i]
            else:
                j = b.pop() + 1
                f(j, i)
                
        if v == 4 and n[i + 1] != 5:
            if l(a) == 0:
                b += [i]
            else:
                j = a.pop()
                i += 1
                f(j, i)

    return n