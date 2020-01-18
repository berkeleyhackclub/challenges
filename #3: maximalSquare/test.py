import time
import random

import aiden
import samuel

arr = []
fa = fb = 1000

for i in range(10000):
    arr.append(random.randint(0, 3))

while fa > 0:
    i = random.randint(0, len(arr) - 2)
    
    if arr[i] != 4 and arr[i - 1] != 4 and arr[i + 1] != 4:
        arr[i] = 4

        fa -= 1

while fb > 0:
    i = random.randint(0, len(arr) - 1)
    
    if arr[i] != 5 and arr[i] != 4 and arr[i - 1] != 4:
        arr[i] = 5

        fb -= 1

def param():
    return arr.copy()

def check(param, output):
    for i in range(len(param)):
        if output[i] == 4:
            if output[i + 1] != 5:
                return False

            if param[i] != 4:
                return False

        if output[i] == 5 and output[i - 1] != 4:
            return False

    if sorted(param) != sorted(output):
        return False

    return True

def test(module, iterations=10000):
    name = module.__name__

    #try:
    output = module.main( param() )
    #except Exception as e:
    #    print(name, "\t", "error")
    #    return -1

    if not check(param(), output):
        print(name, "\t", "incorect", output)
        return -1
    
    start = time.time()
    for i in range(iterations):
        module.main( param() )
    end = time.time()

    elapsed = end - start

    print(name, "\t", elapsed)

    with open(module.__file__) as infile:
        words=0
        characters=0
        for line in infile:
            wordslist=line.split()
            characters += sum(len(word) for word in wordslist)
        print("\t", characters)

    return elapsed

def main():
    test(aiden)
    test(samuel)

main()