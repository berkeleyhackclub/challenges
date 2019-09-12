def main(n):
    x = []
    y = []
    r = range
    for i in r(len(n)):
        if n[i] == 5:
            x.append(i)
        elif n[i] == 4:
            y.append(i)
    for i in r(len(x)):
        n[x[i]], n[y[i] + 1] = n[y[i] + 1], n[x[i]]
    return n