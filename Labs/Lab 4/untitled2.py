#function 1
def noMoreTThanOnce9(x1, x2, x3):
    return not(x1 and x2) and not(x1 and x3) and not(x2 and x3) and not(x1 and x2 and x3)

#function 2
def atLeastOnce(x1, x2, x3):
    return x1 or x2 or x3