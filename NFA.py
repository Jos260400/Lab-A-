#Universidad del Valle de Guatemala
#Lenguajes de Programacion
#Fernando Jose Garavito Ovando 18071
#Lab "A" NFA, Finito no determinista

#Importamos del archivo la clase

from NNFA import NNFA
from Functions import *
import string
import time

class NFA(NNFA):  
      
    def Z(self,Char):
        
        Begin = time.time()
        J = EC(self, self.START)
        G = 0
        
        while(G<len(Char)):
            if Char[G] not in self.THEALPHA:
                return False, (time.time() - Begin)
            J = ECC(self, MM(self,J,Char[G]))
            G +=1
            
        if(len(J & self.Accept) != 0):
            return True, (time.time() - Begin)
        
        else:
            return False, (time.time() - Begin)


