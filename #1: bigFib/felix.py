def main():
    a=0
    b=1

    for x in range(999):
        a , b = b , a + b

    return b