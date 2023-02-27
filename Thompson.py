#Universidad del Valle de Guatemala
#Lenguajes de Programacion
#Fernando Jose Garavito Ovando 18071
#Lab "A" NFA, Finito no determinista

#Importamos del archivo la clase

from NNFA import NNFA
from Functions import epsilon, ECC

class TT():
    
    def __init__(self, regex):
        self.regex = regex
        self.Thenext = 0
        self.Analyze()


#El método isalnum() devuelve True si todos los caracteres de la cadena son alfanuméricos (ya sean letras o números). Si no, devuelve False.
    
    def Analyze(self):
        
        i = 0
        regex = ''
        
        while i < len(self.regex):
            regex += self.regex[i]
            if self.regex[i] !="(" and self.regex[i] != "|":
                if i + 1< len(self.regex) and (self.regex[i + 1].isalnum() or self.regex[i + 1] == '(') :
                    regex += "."
            i += 1
        self.regex = regex
    
    def Collect(self):
        Comeback = self.Thenext
        self.Thenext += 1
        return Comeback

    def Find(self,char):
        Symbol1 = self.Collect()
        Symbol2 = self.Collect()
        STATES = set([Symbol1, Symbol2])
        
        if char ==epsilon:
            THEALPHA = set()
        else:
            THEALPHA = set(char)
        IEstate = Symbol1
        FEstate = set([Symbol2])
        transF = {
            Symbol1:{
                char:set([Symbol2])
            },
            Symbol2:{
            }
        }
        return NNFA(STATES,THEALPHA, transF,IEstate, FEstate)

    def NFA3(self, nfaA, nfaB):
        
        SS = self.Collect()
        Estate = self.Collect()
        AA = ECC(nfaA.transF, nfaB.transF)
        AA[SS] = {epsilon: set([nfaA.START, nfaB.START])}

        for Estado in nfaA.Accept:
            AA[Estado][epsilon] = set([Estate])
            
        for Estado in nfaB.Accept:
            AA[Estado][epsilon] = set([Estate])
            
        AA[Estate] = {}
        EE = nfaA.STATES | nfaB.STATES 
        EE.add(SS)
        EE.add(Estate)
        Alpha = nfaA.THEALPHA | nfaB.THEALPHA         
        return NNFA(EE, Alpha, AA, SS, set([Estate]))
    
    def NFA1(self, nfaA, nfaB):
        
        AA = ECC(nfaA.transF, nfaB.transF)
        
        for Estado in nfaA.Accept:
            AA[Estado][epsilon] = set([nfaB.START])
            
        EE = nfaA.STATES | nfaB.STATES
        Alpha = nfaA.THEALPHA | nfaB.THEALPHA
        return NNFA(EE,Alpha, AA,nfaA.START, nfaB.Accept)
    
    def NFA2 (self, nfaA):
        I = self.Collect()
        Estate = self.Collect()
        AA = nfaA.transF
        AA[I] = {}
        AA[I][epsilon] = set([nfaA.START, Estate])
        AA[Estate] = {}
        for Estado in nfaA.Accept:
            AA[Estado][epsilon] = set([nfaA.START, Estate])
        nfaA.STATES.add(I)
        nfaA.STATES.add(Estate)
        return NNFA(nfaA.STATES, nfaA.THEALPHA, AA, I, set([Estate]))
    
#Tomar en cuenta los simbolos que podemos usar en la expresion regular
    def PP(self,op):
        
        if op == '|':
            return 1
        if op == '.':
            return 2
        if op == '*' or op =='+' or op =='?':
            return 3
        return 0

#aplicarOp aplica una función a operandos especificados de una expresión
    def applyOp(self, a,  op, b = None):
        
        if op == '.': return self.NFA1(a,b) 

        if op == '*': return self.NFA2(a)

        if op == '+': return self.NFA1(a,self.NFA2(a))

        if op == '|': return self.NFA3(a,b)

        if op == '?': return self.NFA3(a,self.Find(epsilon))
    
#Verificamos cada uno de los simbolos posibles
    def CR(self):

        NN = []
        SSS = []
        i = 0

        regex = self.regex
        while i < len(regex):

            if regex[i] == ' ':
                i += 1
                continue
            
            elif regex[i] == '(':
                SSS.append(regex[i])
            
            elif regex[i].isalnum():
                NN.append(self.Find(regex[i]))
            
            elif regex[i] == ')':
                while len(SSS) !=0 and SSS[-1] != '(':
                    op = SSS.pop()
                    if op == "*" or op =="+" or op =="?":
                        N1 = NN.pop()
                        NN.append(self.applyOp(N1, op))
                    else:
                        N2 = NN.pop()
                        N1 = NN.pop()
                        NN.append(self.applyOp(N1, op, N2))
                SSS.pop()
            else:
                while (len(SSS) != 0 and self.PP(SSS[-1]) >= self.PP(regex[i])):
                    op = SSS.pop()
                    if op == "*"or op =="+" or op =="?":
                        N1 = NN.pop()
                        NN.append(self.applyOp(N1, op))
                    else:
                        N2 = NN.pop()
                        N1 = NN.pop()
                        NN.append(self.applyOp(N1, op, N2))
                SSS.append(regex[i])
            i +=1
        while len(SSS) != 0:
            op = SSS.pop()
            if op == "*"or op =="+" or op =="?":
                N1 = NN.pop()
                NN.append(self.applyOp(N1, op))
            else:
                N2 = NN.pop()
                N1 = NN.pop()
                NN.append(self.applyOp(N1, op, N2))      
        return NN[-1]


