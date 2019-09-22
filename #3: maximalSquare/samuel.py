import numpy as np
import random

def checkones(M):
    retval = True
    sz = M.shape
    for i in range(sz[0]):
        for j in range(sz[1]):
            if M[i,j] != 1:
                retval = False
    return retval

def main(M):
    sqrsize = 0
    fndsqr = True
    sz = M.shape
    while fndsqr == True:
        sqrsize += 1
        fndsqr = False
        for i in range(sz[0]- sqrsize):
            for j in range(sz[1]- sqrsize):
                if checkones(M[i:i+sqrsize,j:j+sqrsize]):
                    fndsqr = True
        if fndsqr == False:
            sqrsize -= 1
    return sqrsize ** 2