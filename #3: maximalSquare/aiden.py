def square(a):
    d=0
    for b in range(len(a)):
        for c in range(len(list(a[b]))):
            if list(a[b])[c]=='1':
                g=1
                e=True
                while e:
                    for f in range(g+1):
                        try:
                            if list(a[b+f])[c+g]=='0':
                                e=False
                        except IndexError:
                            e=False
                    for f in range(g+1):
                        try:
                            if list(a[b+g])[c+f]=='0':
                                e=False
                        except IndexError:
                            e=False
                    if e:
                        g+=1
                if g>d:
                    d=g
    return d**2