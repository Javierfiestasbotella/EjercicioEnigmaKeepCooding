from enigma import *
import random
'''rotor1=["UBGRXAIQTVYLDÑMHCKWNOJFZEPS","QTVYLDPSUBGRXAIÑMHCKWNOJFZE"]
rotor2=['ÑPODWMELKGIUXCAYTZBNVJSHQRF','CYPTRSÑHBJOLWXKDVMQZIAGUFEN']
rotor3=['VGMDLFBSTCÑXKPWZHOEJNARYIQU','IGNRVUFMYPXSWÑETCZBDALKQJHO']'''
       
r=Rotor("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
rf=Reflector()
e=Enigma("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
#x=input("dime nombre: ")
#print(r.crea_rotor(x))
'''x=r.conexion(16,rotor1)
y=rf.refleja(x)
sol=r.conexion_decodifica(y,rotor1)
print(sol)'''
print(r.rotor1)
print(r.rotor2)
print(r.rotor3)
print(e.posicion_inicial(rotor1,rotor2,rotor3,"A","M","Z"))
print(r.rotor1)
print(r.rotor2)
print(r.rotor3)



