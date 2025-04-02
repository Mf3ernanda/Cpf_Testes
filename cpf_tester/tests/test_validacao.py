import unittest
from app.validacao import validar_cpf

class TestValidacaoCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("11144477735"))

    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("123.456.789-00"))
        self.assertFalse(validar_cpf("000.000.000-00"))
        self.assertFalse(validar_cpf("529.982.247-24"))

    def test_cpf_com_caracteres_invalidos(self):
        self.assertFalse(validar_cpf("52a.982.247-25"))
        self.assertFalse(validar_cpf("529-982-247-25"))
        self.assertFalse(validar_cpf(""))

if __name__ == "__main__":
    unittest.main()
