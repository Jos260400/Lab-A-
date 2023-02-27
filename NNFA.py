#Universidad del Valle de Guatemala
#Lenguajes de Programacion
#Fernando Jose Garavito Ovando 18071
#Lab "A" NFA, Finito no determinista

#Utilizamos graphviz para realizar el grafo
import string
import graphviz

class NNFA():
    
    def __init__(self, STATES ,THEALPHA, transF, START, ACCEPT):
        self.STATES = STATES
        self.THEALPHA = THEALPHA
        self.transF = transF
        self.START = START
        self.Accept = ACCEPT

#Empezamos a colocar el resultado de nuestro grafo

    def render(self, path):
        
        graph = graphviz.Digraph('Automat', format= "png")
        
        for Estado in self.STATES:
            if Estado == self.START:
                graph.node(str(Estado), color = "Blue")
            if Estado in self.Accept:
                graph.node(str(Estado), shape = 'Circle')
            else:
                graph.node(str(Estado))
                
        for node in self.transF.keys():
            for char in self.transF[node].keys():
                Come = self.transF[node][char]
                for item in Come:
                    graph.edge(str(node), str(item), label=char)
        graph.render(path)

