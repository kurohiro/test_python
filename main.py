import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 2

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    print('AND(0, 0) = {}'.format(AND(0, 0)))
    print('AND(0, 1) = {}'.format(AND(0, 1)))
    print('AND(1, 0) = {}'.format(AND(1, 0)))
    print('AND(1, 1) = {}'.format(AND(1, 1)))
    print('NAND(0, 0) = {}'.format(NAND(0, 0)))
    print('NAND(0, 1) = {}'.format(NAND(0, 1)))
    print('NAND(1, 0) = {}'.format(NAND(1, 0)))
    print('NAND(1, 1) = {}'.format(NAND(1, 1)))
    print('OR(0, 0) = {}'.format(OR(0, 0)))
    print('OR(0, 1) = {}'.format(OR(0, 1)))
    print('OR(1, 0) = {}'.format(OR(1, 0)))
    print('OR(1, 1) = {}'.format(OR(1, 1)))
    print('XOR(0, 0) = {}'.format(XOR(0, 0)))
    print('XOR(0, 1) = {}'.format(XOR(0, 1)))
    print('XOR(1, 0) = {}'.format(XOR(1, 0)))
    print('XOR(1, 1) = {}'.format(XOR(1, 1)))



