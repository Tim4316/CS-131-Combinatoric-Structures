((P <= Q) or (P <= R)) <= (P <= (Q or R)) 
not((P <= Q) or (P <= R)) or (P <= (Q or R))  #conditional identities
not((not P or Q) or (not P or R)) or (not P or (Q or R))  #conditional identites
not(not P or (Q or R)) or (not P or (Q or R))  #distributive law
not(not P or (Q or R)) or (not P or (Q or R))  #complement law