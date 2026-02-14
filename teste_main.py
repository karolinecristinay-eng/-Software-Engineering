import unittest
from main import Matricula

class TestSistemaMatricula(unittest.TestCase):
    def test_criacao_matricula(self):
        # Verifica se o objeto é criado com os dados corretos
        m = Matricula("123", "Teste Aluno", "Engenharia")
        self.assertEqual(m.nome, "Teste Aluno")
        self.assertEqual(m.status, "Ativa")

if __name__ == "__main__":
    unittest.main()
