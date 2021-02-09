import random
from colorama import init, Fore, Back, Style
class Reflector(): 
    
    def __init__(self):
        
        self.reflector=["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "," ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"]
            
    def refleja(self,indice):
        letra=self.reflector[0][indice]
        indice_reflejo=self.reflector[1].index(letra)
        return indice_reflejo    
   
class Rotor():

    def __init__(self):
        self.abecedario=["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "]
        self._pos_ini = None
        self.rotor1=[" UBGRXAIQTVYLDÑMHCKWNOJFZEPS","QTVYLDPSUBGRXAIÑMHCKWNOJFZE "]
        self.rotor2=[' ÑPODWMELKGIUXCAYTZBNVJSHQRF','CYPTRSÑHBJOLWXKDVMQZIAGUFEN ']
        self.rotor3=[' VGMDLFBSTCÑXKPWZHOEJNARYIQU','IGNRVUFMYPXSWÑETCZBDALKQJHO ']
       
    def crea_rotor (self,nombre):
        tamano=28
        abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        desordena=random.sample(abecedario,tamano)
        primero=''.join(desordena)
        desordena=random.sample(abecedario,tamano)
        segundo=''.join(desordena)
        nombre=[primero,segundo]
        return nombre   
    
    def conexion (self,indi,rotor):
        letra=rotor[0][indi]
        conector=rotor[1].index(letra)
        return conector

    def conexion_decodifica(self,indice,rotor):
        letra=rotor[1][indice]
        conector=rotor[0].index(letra)
        return conector


    @property
    def pos_ini(self):
        return self._pos_ini

    @pos_ini.setter
    def pos_ini(self, value):
        self._pos_ini = self.conexion[0].index(value)

class Enigma():
    
    def __init__(self):
        self.abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
        self.rotor1=[" UBGRXAIQTVYLDÑMHCKWNOJFZEPS","QTVYLDPSUBGRXAIÑMHCKWNOJFZE "]
        self.rotor2=[' ÑPODWMELKGIUXCAYTZBNVJSHQRF','CYPTRSÑHBJOLWXKDVMQZIAGUFEN ']
        self.rotor3=[' VGMDLFBSTCÑXKPWZHOEJNARYIQU','IGNRVUFMYPXSWÑETCZBDALKQJHO ']
       
    def posicion_inicial(self,rotora,rotorb,rotorc,a,b,c):
        global rotor1
        global rotor2
        global rotor3
        x=rotora[0].index(a)
        self.rotor1=[rotora[0][x:]+rotora[0][:x],rotora[1][x:]+rotora[1][:x]]
        y=rotorb[0].index(b) 
        self.rotor2=[rotorb[0][y:]+rotorb[0][:y],rotorb[1][y:]+rotorb[1][:y]]
        z=rotorc[0].index(c)
        self.rotor3=[rotorc[0][z:]+rotorc[0][:z],rotorc[1][z:]+rotorc[1][:z]]
        return self.rotor1,self.rotor2,self.rotor3
    
e=Enigma()
rf=Reflector()
r=Rotor()
posini=[]
def start():
    cambio_rotores=input(Fore.BLUE+"Introduce Posicion inicial: trés letras en mayusculas seguidas: "+Fore.WHITE)
    for s in cambio_rotores:
        posini.append(s)
    a=posini[0]
    b=posini[1]
    c=posini[2]
    print("Sobre  la posicion: "+Fore.RED+a,b,c+" ",end="")
    e.posicion_inicial(r.rotor1,r.rotor2,r.rotor3,a,b,c)
    mensaje=input(Fore.BLUE+"Introduce mensaje secreto: "+Fore.WHITE)
    for i in mensaje:#poner una condicion si lo escrito no esta en mayusculas ponerlas. poner tambien espacios para frases
        indice=e.abecedario.index(i) 
        indice=r.conexion(indice,e.rotor1)
        indice=r.conexion(indice,e.rotor2)    
        indice=r.conexion(indice,e.rotor3)
        indice=rf.refleja(indice)
        indice=r.conexion_decodifica(indice,e.rotor3)   
        indice=r.conexion_decodifica(indice,e.rotor2)
        fin=r.conexion_decodifica(indice,e.rotor1)
        mensaje_trans=e.abecedario[fin]
        print(Fore.GREEN+mensaje_trans+Fore.WHITE,end="")

start()





