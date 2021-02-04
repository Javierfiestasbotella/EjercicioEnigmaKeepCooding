from enigma import *
from random import shuffle
from colorama import init, Fore, Back, Style
r = Rotor()
r.rotor1=[('Ñ', 'U'), ('E', 'K'), ('F', 'W'), ('V', 'T'), ('A', 'Ñ'), ('D', 'C'), ('X', 'Y'), ('K', 'Z'), ('Q', 'R'), ('H', 'O'), ('J', 'F'), ('L', 'E'), ('S', 'A'), ('W', 'V'), ('U', 'Q'), ('G', 'N'), ('C', 'H'), ('T', 'I'), ('R', 'X'), ('N', 'S'), ('B', 'M'), ('P', 'G'), ('Z', 'D'), ('O', 'B'), ('M', 'P'), ('I', 'J'), ('Y', 'L')]
r.rotor2=[('T', 'I'), ('M', 'P'), ('A', 'Ñ'), ('W', 'V'), ('S', 'A'), ('N', 'S'), ('E', 'K'), ('H', 'O'), ('O', 'B'), ('J', 'F'), ('Y', 'L'), ('D', 'C'), ('C', 'H'), ('F', 'W'), ('U', 'Q'), ('G', 'N'), ('K', 'Z'), ('Z', 'D'), ('B', 'M'), ('X', 'Y'), ('V', 'T'), ('Q', 'R'), ('R', 'X'), ('I', 'J'), ('P', 'G'), ('Ñ', 'U'), ('L', 'E')]
r.rotor3=[('U', 'Q'), ('G', 'N'), ('T', 'I'), ('L', 'E'), ('E', 'K'), ('C', 'H'), ('Q', 'R'), ('B', 'M'), ('N', 'S'), ('F', 'W'), ('Z', 'D'), ('Y', 'L'), ('P', 'G'), ('I', 'J'), ('W', 'V'), ('Ñ', 'U'), ('J', 'F'), ('H', 'O'), ('X', 'Y'), ('D', 'C'), ('V', 'T'), ('O', 'B'), ('R', 'X'), ('M', 'P'), ('A', 'Ñ'), ('S', 'A'), ('K', 'Z')]
r.reflector=[('Z', 'D'), ('E', 'K'), ('Q', 'R'), ('A', 'Ñ'), ('T', 'C'), ('C', 'T'), ('S', 'H'), ('H', 'S'), ('G', 'N'), ('N', 'G'), ('I', 'J'), ('J', 'I'), ('X', 'V'), ('V', 'X'), ('F', 'W'), ('W', 'F'), ('Y', 'Y'), ('L', 'O'), ('O', 'L'), ('M', 'B'), ('B', 'M'), ('U', 'P'), ('P', 'U'), ('D', 'Z'), ('Ñ', 'A'), ('R', 'Q'), ('K', 'E')]



#shuffle (rotor_pruebas)
#print(rotor_pruebas)


print(Fore.GREEN+"Bienvenidos a la segunda versión de Enigama realizada con Listas y tuplas:"+Fore.WHITE)
print(Fore.BLUE+"primero vamos a introducir la posicion inicial: "+Fore.WHITE)
position=input(Fore.RED+"Escribe las 3 letras de la posicion: ")+Fore.WHITE
r.posicionInicial(position)


mensaje=input(Fore.RED+"introduzca la palabra que quiera para por enigma: \n"+Fore.WHITE)
r.codifica_mensaje(mensaje)
print("\n")
iniciar=input("¿Quiere volver a utilizar enigama?: \n")
while iniciar!="no":
    mensaje=input(Fore.BLUE+"introduzca la palabra que quiera para por enigma: \n"+Fore.WHITE)
    r.codifica_mensaje(mensaje)
    print("\n")
    iniciar=input(Fore.BLUE+"¿Quiere volver a utilizar enigama?: \n"+Fore.WHITE)
print(Fore.RED+"Ha sido un placer prestar mis servicios. Hasta pronto."+Fore.WHITE)

'''pas=[2,4,5]
#print(r.rotor1)
r.rotor1 = r.rotor1[pas[1]:] + r.rotor1[:pas[1]]
print(r.rotor1)'''


