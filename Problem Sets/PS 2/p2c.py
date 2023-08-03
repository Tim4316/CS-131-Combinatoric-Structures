not((P <= Q) or (Q <= R))
not((not P or Q) or (not Q or R))  #conditional identities
not((Q or not Q) or (R or not P))  #associative laws
not (True or (R or not P))  #complement laws
False  #domination laws