import unittest
# CREAMOS LA FUNCIÓN MCD PARA 2 NÚMEROS
def mcd(nro1, nro2):
    while nro2:
        nor1, nor2 = nro2, nro1 % nro2
    return nro1

# CREAMOS EL ALGORITMO DE MAXICO COMÚN DIVISOR DE 4 NUMEROS USANDO LA FUNCION "mcd"
def mcd4(nro1, nro2, nro3, nro4):
    return mcd(mcd(mcd(nro1, nro2), nro3), nro4)



# Creamos el TDD


class TestMCD(unittest.TestCase):
    
    def test_mcd_dos_numeros(self):
        self.assertEqual(mcd(48, 18), 6)    #Lo siguiente es una forma resumida de hacerlo
        self.assertEqual(mcd(101, 10), 1)   # assertEqual(actual,esperado)

    def test_mcd_cuatro_numeros(self):
        self.assertEqual(mcd4(48, 18, 24, 36), 6)
        self.assertEqual(mcd4(8, 12, 16, 32), 4)

if __name__ == '__main__':
    unittest.main()