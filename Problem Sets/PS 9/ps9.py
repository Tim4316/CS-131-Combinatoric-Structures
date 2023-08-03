def collatz_function(a):
    """ which when given a positive number ai returns ai+1 according 
        to the definition of the Collatz sequence, e.g. on input 3 your 
        function should return 10. """
    if a % 2 == 0:
        return a//2
    else:
        return 3 * a + 1
    
def collatz_sequence(a):
    """ returns the Collatz sequence (as a list) starting at a0 = a
    which terminates at some n where an = 1. """
    list = [a]
    while a > 1:
        a = collatz_function(a)
        list = list + [a]
    return list

def smallest_int_with_collatz_length(n):
    """ returns the smallest integer whose Collatz sequence has length at least n """
    small_len = 0
    a = 0
    while n > small_len:
        a = a + 1
        small_len = len(collatz_sequence(a))
    return a

#counterexample = [the smallest counterexample is 500. After 500, it gives the same number.]