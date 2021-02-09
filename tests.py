import unittest
import enigma

class ReflectorTest(unittest.TestCase):
    def test_refleja(self):
        reflector = enigma.Reflector()
        self.assertEqual(reflector.refleja(26), 0)
        

class RotorTest(unittest.TestCase):
    def test_construye(self):
        rotor = enigma.Rotor()
        c=[]
        self.assertEqual(rotor.crea_rotor(c),['LQRWNZÑEPBXJVKFYHUMAOCDSTGI', 'VPZIDBNCGTHÑQJLORUAEKFSXYMW'] )

    def test_codifica(self):
        rotor = enigma.Rotor()
        self.assertEqual(rotor.conexion(0,["ABCD","CABD"]), 1)
        self.assertEqual(rotor.conexion_decodifica(2,["ABCD","CABD"]), 1)

    def test_letrasiciales(self):
        pos=enigma.Enigma()
        a="A"
        b="A"
        c="B"
        rotora=["ABC","BCA"]
        rotorb=["BCA","ABC"]
        rotorc=["CAB","BAC"]
        self.assertEqual(pos.posicion_inicial(rotora,rotorb,rotorc,a,b,c),["ABC","BCA"],["ACB","BAC"],["BAC","CAB"])

if __name__== '__main__':
    unittest.main()