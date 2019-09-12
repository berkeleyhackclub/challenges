import time

import cody
import sameul
import felix
import milo

def test(module, expected, iterations=10000):
    output = module.main()
    name = module.__name__
    
    if expected != output:
        print(name, "incorect")
        return -1
    
    start = time.time()
    for i in range(iterations):
        module.main()
    end = time.time()

    elapsed = end - start

    print(name, "\t", elapsed)

    return elapsed

def main():
    expected = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    
    test(sameul, expected)
    test(cody, expected)
    test(felix, expected)
    test(milo, expected)

main()