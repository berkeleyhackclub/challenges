#54 chars

def main():
    e=0
    r=1
    t=0

    for x in range(999):
        t=r+e
        e=r
        r=t

    return t