def similarity1(A, B):
    """ return the similarity score between the two strings 
        using the algorithm 
    """
    digit = 0
    for x in A:
        for y in B:
            if x == y:
                digit += 1
    return digit / (len(A) + len(B) - digit)

def similarity2(A, B):
    """ return the similarity score between the two strings 
        using the algorithm 
    """
    numerator = 0
    den1 = 0
    den2 = 0
    for i in range(len(A)):
        numerator += A[i] * B[i]
        den1 += A[i] ** 2
        den2 += B[i] ** 2
    denomenator = (den1 ** 0.5) * (den2 ** 0.5)
    return numerator / denomenator
        
        
        

