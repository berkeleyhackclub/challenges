#84 char

def main():
    fib = [0,1]
    for i in range(2,1001):
        fib.append(fib[i-1]+fib[i-2])
    return fib[1000]