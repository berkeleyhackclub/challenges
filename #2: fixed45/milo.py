def main(a):
    l=len(a)
    A=[0 for i in range(l)]
    tool=[i for i in a if i!=4 and i!=5]
    for i in range(l):
        if a[i]==4:
            A[i]=4
            A[i+1]=5
        elif A[i]!=5:
            A[i]=tool.pop(0) 

    return A