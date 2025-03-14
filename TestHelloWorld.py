import unittest
from HelloWorld import ola_mundo_idioma


class TestOlaMundo(unittest.TestCase):
    def test_portugeus(self):
        self.assertEqual(ola_mundo_idioma("pt"), "Ola Mundo")

    def test_ingles(self):
        self.assertEqual(ola_mundo_idioma("en"), "Hello World")

    def test_espanhol(self):
        self.assertEqual(ola_mundo_idioma("es"), "Hola Mundo")

    def test_frances(self):
        self.assertEqual(ola_mundo_idioma("fr"), "Bonjour le monde")

    def test_italiano(self):
        self.assertEqual(ola_mundo_idioma("it"), "Ciao Mondo")

    def test_alemao(self):
        self.assertEqual(ola_mundo_idioma("de"), "Hallo Welt")
    
    def test_japones(self):
        self.assertEqual(ola_mundo_idioma("ja"), "こんにちは世界")


if __name__ == "__main__":
    unittest.main()