#Universidad del Valle de Guatemala
#Lenguajes de Programacion
#Fernando Jose Garavito Ovando 18071
#Lab "A" NFA, Finito no determinista

#Uso de epsilon
epsilon = "ε"

def EC(NFA, Estado):
    Comeback = set()

    Comeback.add(Estado)
    Noback = [Estado]
    Verify = [Estado]
    while len(Verify) != 0: 
        
        ZEstate = Verify.pop(0)
        try:
            EPSILON = NFA.transF[ZEstate][epsilon]
        except:
            EPSILON = set()
        for D in EPSILON:
            if D not in Noback:
                Verify.append(D)
                Comeback.add(D)
        Noback.append(ZEstate)
    return frozenset(Comeback)

def ECC(NFA, T):
    
    Comeback = set()
    for Estado in T:
        ZClose = EC(NFA, Estado)
        for D in ZClose:
            Comeback.add(D)
    return frozenset(Comeback)

def MM(NFA, T, char):
    
    Comeback = set()
    for Estado in T:
        try:
            STATES = NFA.transF[Estado][char]
        except:
            STATES = set()
        for D in STATES:
            Comeback.add(D)
    return frozenset(Comeback)

#Hacemos uso de las llaves

def ECC(T1, T2):
    NT = {}
    for K in T1:
        NT[K] = T1[K]
    for K in T2:
        NT[K] = T2[K]
    return NT