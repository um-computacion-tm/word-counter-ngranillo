import unittest
from count_words import count_words


class TestCountWords(unittest.TestCase):
    
    def test_holaComoEstas (self):
        resultado = count_words("hola como estas")
        self.assertEqual(resultado, {"hola" : 1,"como" : 1,"estas" : 1})
    
    def test_holaComoEstasHola (self):
        resultado = count_words("hola como estas Hola")
        self.assertEqual(resultado, {"hola" : 2,"como" : 1,"estas" : 1})    
        
if  __name__ == "__main__":
    unittest.main()