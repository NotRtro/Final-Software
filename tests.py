import unittest
from datetime import datetime
from main import Cuenta, Operacion

class TestOperacion(unittest.TestCase):
    def setUp(self):
        self.operacion = Operacion(123, 100) #Creamos una operacion

    def test_init(self):
        self.assertEqual(self.operacion.numero_destino, 123) #Verificamos que el numeor de destino este correcto sean correctos
        self.assertEqual(self.operacion.valor, 100) #Verificamos que los el valor a modificar este bien
        self.assertIsInstance(self.operacion.fecha, datetime) #Verificamos que la fecha esta correcta

class TestCuenta(unittest.TestCase):
    def setUp(self):
        self.cuenta = Cuenta(21345, 'Arnaldo', 200, [123, 456]) #Creamos una cuenta

    def test_init(self):
        self.assertEqual(self.cuenta.numero, 21345) #Verificamos que el numero de cuenta este correcto
        self.assertEqual(self.cuenta.nombre, 'Arnaldo') #Verificamos que el nombre de la cuenta este correcto
        self.assertEqual(self.cuenta.saldo, 200) #Verificamos que el saldo de la cuenta este correcto
        self.assertEqual(self.cuenta.contactos, [123, 456]) #Verificamos que los contactos de la cuenta esten correctos
        self.assertEqual(self.cuenta.operaciones, []) #Verificamos que las operaciones de la cuenta esten correctas (vacio)

    def test_agregar_contacto(self):
        self.cuenta.agregar_contacto('Luisa', 789) #Agregamos un contacto
        self.assertIn({'nombre': 'Luisa', 'numero': 789}, self.cuenta.contactos) #Verificamos que el contacto este en la lista de contactos

    def test_eliminar_contacto(self):
        self.cuenta.eliminar_contacto(123) #Eliminamos un contacto
        self.assertNotIn(123, self.cuenta.contactos) #Verificamos que el contacto ya no este en la lista de contactos

    def test_pagar(self):
        self.assertTrue(self.cuenta.pagar(123, 50)) # Verificamos que se pueda realizar un pago
        self.assertEqual(self.cuenta.saldo, 150) # Verificamos que el saldo este correcto
        self.assertEqual(len(self.cuenta.operaciones), 1) # Verificamos que la operacion se haya guardado

if __name__ == '__main__':
    unittest.main() # Corremos los 5 tests
    