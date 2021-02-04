import random
from colorama import init, Fore, Back, Style
class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ-."):
        self.abecedario = abecedario
        self.rotor1=[('Ñ', 'U'), ('E', 'K'), ('F', 'W'), ('V', 'T'), ('A', 'Ñ'), ('D', 'C'), ('X', 'Y'), ('K', 'Z'), ('Q', 'R'), ('H', 'O'), ('J', 'F'), ('L', 'E'), ('S', 'A'), ('W', 'V'), ('U', 'Q'), ('G', 'N'), ('C', 'H'), ('T', 'I'), ('R', 'X'), ('N', 'S'), ('B', 'M'), ('P', 'G'), ('Z', 'D'), ('O', 'B'), ('M', 'P'), ('I', 'J'), ('Y', 'L')]
        self.rotor2=[('T', 'I'), ('M', 'P'), ('A', 'Ñ'), ('W', 'V'), ('S', 'A'), ('N', 'S'), ('E', 'K'), ('H', 'O'), ('O', 'B'), ('J', 'F'), ('Y', 'L'), ('D', 'C'), ('C', 'H'), ('F', 'W'), ('U', 'Q'), ('G', 'N'), ('K', 'Z'), ('Z', 'D'), ('B', 'M'), ('X', 'Y'), ('V', 'T'), ('Q', 'R'), ('R', 'X'), ('I', 'J'), ('P', 'G'), ('Ñ', 'U'), ('L', 'E')]
        self.rotor3=[('U', 'Q'), ('G', 'N'), ('T', 'I'), ('L', 'E'), ('E', 'K'), ('C', 'H'), ('Q', 'R'), ('B', 'M'), ('N', 'S'), ('F', 'W'), ('Z', 'D'), ('Y', 'L'), ('P', 'G'), ('I', 'J'), ('W', 'V'), ('Ñ', 'U'), ('J', 'F'), ('H', 'O'), ('X', 'Y'), ('D', 'C'), ('V', 'T'), ('O', 'B'), ('R', 'X'), ('M', 'P'), ('A', 'Ñ'), ('S', 'A'), ('K', 'Z')]
        self.reflector=[('Z', 'D'), ('E', 'K'), ('Q', 'R'), ('A', 'Ñ'), ('T', 'C'), ('C', 'T'), ('S', 'H'), ('H', 'S'), ('G', 'N'), ('N', 'G'), ('I', 'J'), ('J', 'I'), ('X', 'V'), ('V', 'X'), ('F', 'W'), ('W', 'F'), ('Y', 'Y'), ('L', 'O'), ('O', 'L'), ('M', 'B'), ('B', 'M'), ('U', 'P'), ('P', 'U'), ('D', 'Z'), ('Ñ', 'A'), ('R', 'Q'), ('K', 'E')]
        
    
    
    def codifica_rotor(self,letra,lista,a,b):      
        numeracion=[]
        global orden
        global letra_nueva
        for i in lista:
            d= letra in i[a]
            numeracion.append(d)
        orden=numeracion.index(True)
        letra_nueva=lista[orden][b]
        return letra_nueva
        return orden
    
    
    
    
    
    def codifica_mensaje(self,palabra):
        global letra_nueva
        rotor1=self.rotor1
        rotor2=self.rotor2
        rotor3=self.rotor3
        reflector=self.reflector
        abecedario=self.abecedario
        for letra in palabra:
            self.codifica_rotor(letra,rotor1,0,1)
            self.codifica_rotor(letra_nueva,rotor2,0,1)
            self.codifica_rotor(letra_nueva,rotor3,0,1)
            self.codifica_rotor(letra_nueva,reflector,1,0)# en esta parte al haber parejas iguales con distinta posicion confunde la letra.
            self.codifica_rotor(letra_nueva,rotor3,1,0)
            self.codifica_rotor(letra_nueva,rotor2,1,0)
            self.codifica_rotor(letra_nueva,rotor1,1,0)
            print(Fore.GREEN+letra_nueva+Fore.WHITE,end="")
            
            


    def posicionInicial(self, abc):
        pos=[]
        for i in abc:
            pos.append(i)
        position = self.abecedario.index(pos[0])
        self.rotor1 = self.rotor1[position:] + self.rotor1[:position]
        position = self.abecedario.index(pos[1])
        self.rotor2 = self.rotor2[position:] + self.rotor2[:position]
        position = self.abecedario.index(pos[2])
        self.rotor3 = self.rotor3[position:] + self.rotor3[:position]
       

        


    def avanza(self):
        self.rotor1 = self.rotor1[1:] + self.rotor1[:1]

    def imprime(self):
        print("prueba")
   