#Universidad del Valle de Guatemala
#Lenguajes de Programacion
#Fernando Jose Garavito Ovando 18071
#Lab "A" NFA, Finito no determinista

#Importamos del archivo la clase

from Thompson import TT

#Le indicamos al usuario que coloque una expresion regular

A = True
while A:
    
    print("Escriba una expresion regular:")
    regex = input()
    T = TT(regex)
    TNFA = T.CR()
    TNFA.render("NFA")

#Nuestro valor ya fue convertido a su notacion postfix

    R = True
    while R:

#Mostramos el resultado

        C = input()
        Result, TIME = TNFA.Z(C)


