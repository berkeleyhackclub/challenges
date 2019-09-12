def main(n=1000):
    phi=(1+5**.5)/2
    return int((phi**n-(-phi)**(-n))/(5**.5))