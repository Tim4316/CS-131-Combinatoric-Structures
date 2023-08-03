#function 1
def subset(A, B):
    """ return true if the first set is a proper subset 
        of the second set
    """
    for x in A:
        if x not in B:
            return False
    return True

#function 2
def properSubset(A, B):
    """ return true if the first set is a proper subset 
        of the second set
    """
    if not subset(A, B):
        return False
    for x in B:
        if x not in A:
            return True
    return False