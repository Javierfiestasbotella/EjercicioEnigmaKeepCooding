import random
from colorama import init, Fore, Back, Style
class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.reflector =['O', 'D', 'N', 'B', 'K', 'S', 'U', 'I', 'X', 'C', 'V', 'M', 'G', 'J', 'A', 'Y', 'L', 'Z', 'E', 'Q', 'Ñ', 'T', 'F', 'W', 'R', 'H', 'P']
        self.reflectorB=['B', 'W', 'V', 'K', 'R', 'P', 'H', 'Z', 'L', 'M', 'E', 'O', 'A', 'S', 'G', 'Y', 'D', 'X', 'F', 'C', 'T', 'U', 'J', 'Ñ', 'N', 'I', 'Q']
        self.rotor1_A=['P', 'O', 'A', 'R', 'G', 'X', 'Y', 'H', 'Q', 'K', 'E', 'Z', 'U', 'M', 'C', 'J', 'D', 'B', 'F', 'I', 'T', 'S', 'W', 'Ñ', 'L', 'V', 'N']
        self.rotor1_B=['J', 'U', 'B', 'T', 'M', 'W', 'Q', 'D', 'F', 'O', 'L', 'I', 'N', 'P', 'Ñ', 'R', 'K', 'V', 'Y', 'Z', 'C', 'E', 'S', 'H', 'G', 'A', 'X']
        self.rotor2_A=['F', 'G', 'Z', 'P', 'X', 'H', 'J', 'N', 'O', 'U', 'C', 'V', 'W', 'Q', 'L', 'Y', 'A', 'M', 'Ñ', 'S', 'B', 'K', 'R', 'E', 'T', 'D', 'I']
        self.rotor2_B=['S', 'Ñ', 'E', 'Q', 'K', 'G', 'P', 'R', 'J', 'A', 'V', 'L', 'W', 'U', 'T', 'H', 'F', 'I', 'B', 'O', 'D', 'M', 'C', 'Z', 'N', 'Y', 'X']
        self.rotor3_A=['D', 'A', 'K', 'W', 'Z', 'B', 'Y', 'U', 'P', 'T', 'O', 'E', 'M', 'F', 'R', 'H', 'V', 'X', 'Ñ', 'I', 'N', 'J', 'S', 'Q', 'G', 'C', 'L']
        self.rotor3_B=['S', 'W', 'U', 'P', 'I', 'F', 'E', 'M', 'B', 'A', 'K', 'X', 'J', 'O', 'H', 'Q', 'R', 'N', 'V', 'G', 'Ñ', 'L', 'D', 'Z', 'T', 'Y', 'C']
        
        
    #Recorrido del mensaje por los rotores codificando cada letra, 
    def codificar(self,palabra):
        for a in palabra: 
            b=self.rotor1_A.index(a)
            a=self.rotor1_B[b]
            #paso por el primer par de rodillos del rotor1
            b=self.rotor2_A.index(a)
            a=self.rotor2_B[b]
            #paso por los dos engranajes del rotor 2
            b=self.rotor3_A.index(a)
            a=self.rotor3_B[b]
            #paso por los engranajes del rotor 3
            b=self.reflector.index(a)
            a=self.reflectorB[b]
            #paso por el reflector
            b=self.rotor3_B.index(a)
            a=self.rotor3_A[b]
            #Camino de vualta
            b=self.rotor2_B.index(a)
            a=self.rotor2_A[b]
            b=self.rotor1_B.index(a)
            a=self.rotor1_A[b] 
            self.avanza()#vuelta del engranaje de la primera tuerca del rotor 1
            print(Fore.GREEN+a,end=" ")
        print("\n"+Fore.WHITE)
    
    #descodificar
    def descodificar(self,palabra):
        for a in palabra: 
            b=self.rotor1_A.index(a)
            a=self.rotor1_B[b]
            #print("primer rotor "+a)
            b=self.rotor2_A.index(a)
            a=self.rotor2_B[b]
            #print("segundo rotor "+a)
            b=self.rotor3_A.index(a)
            a=self.rotor3_B[b]

            b=self.reflectorB.index(a)
            a=self.reflector[b]
           
            
            b=self.rotor3_B.index(a)
            a=self.rotor3_A[b]
            
            b=self.rotor2_B.index(a)
            a=self.rotor2_A[b]
            
            b=self.rotor1_B.index(a)
            a=self.rotor1_A[b]
            self.avanza()
            print(Fore.GREEN+a+Fore.WHITE,end=" ")
            
    
    

       


    # Busca la posicion inicial dentro del rotor1_A, lo corta y lo pone primero y todo el string anterior lo "pega" justo a continuación
    def posicionInicial(self, letra):
        position = self.rotor1_A.index(letra)
        self.rotor1_A = self.rotor1_A[position:] + self.rotor1_A[:position]


#método para avanzar 1 posicion el rotor1_A cada vez que codifica
    def avanza(self):
        self.rotor1_A = list(self.rotor1_A[1:]) + list(self.rotor1_A[:1])



