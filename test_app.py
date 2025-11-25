import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()


    # rota inexistente deve retornar 404
    def test_rota(self):
        response = self.client.get('/rota-que-nao-existe')
        self.assertEqual(response.status_code, 404)

    # login com método errado (GET em vez do POST)
    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 405) 

    # protected com token inválido
    def test_protected_token(self):
        headers = {"Authorization": "Bearer token_falso"}
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 422)  

if __name__ == '__main__':
    unittest.main()