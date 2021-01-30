from enigma import *
from colorama import init, Fore, Back, Style

reflector =  ['O', 'D', 'N', 'B', 'K', 'S', 'U', 'I', 'X', 'C', 'V', 'M', 'G', 'J', 'A', 'Y', 'L', 'Z', 'E', 'Q', 'Ñ', 'T', 'F', 'W', 'R', 'H', 'P']
reflectorB=  ['B', 'W', 'V', 'K', 'R', 'P', 'H', 'Z', 'L', 'M', 'E', 'O', 'A', 'S', 'G', 'Y', 'D', 'X', 'F', 'C', 'T', 'U', 'J', 'Ñ', 'N', 'I', 'Q']                



#Pulsar Run o play para empezar: Por ahora solo palabras, no frases y en MAYÚSCULAS.

r = Rotor()
print("------BIENVENIDOS A KEEP"+Fore.RED+"3NI?M4"+Fore.WHITE+"COODING---------")
print(Fore.GREEN+"------------------------------------------------------"+Fore.WHITE)
p_I=input("introduce en mayuscula la letra para la posicion inicial: ")
r.posicionInicial(p_I)
codigo=input(Fore.BLUE+"dime una palabra: "+Fore.WHITE) 
r.codificar(codigo)
p_I=input("introduce en mayuscula la letra para la posicion inicial: ")
r.posicionInicial(p_I)
codigo2=input(Fore.BLUE+"dime que quieres descodificar: "+Fore.WHITE)
r.descodificar(codigo2)






