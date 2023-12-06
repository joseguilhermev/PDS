# O código está importando o módulo `unittest`, bem como dois outros módulos denominados `funcoes` e `bd`.
# Esses módulos contêm funções e/ou classes que serão usadas nos testes de unidade definidos no código.
import unittest
import funcoes
import bd


class TestFuncoes(unittest.TestCase):
    def test_autenticacao(self):
        """
        A função `test_autenticacao` testa a função `autenticacao` do módulo `funcoes` ao
        comparando os resultados esperados e reais.
        """
        expected_valid = True
        expected_invalid = False

        actual_valid = funcoes.autenticacao("Professor3", "senha3")
        actual_invalid_password = funcoes.autenticacao("user1", "1234")
        actual_invalid_username = funcoes.autenticacao("user2", "123")

        self.assertEqual(actual_valid, expected_valid)
        self.assertEqual(actual_invalid_password, expected_invalid)
        self.assertEqual(actual_invalid_username, expected_invalid)

    def test_retornaIdUsuario(self):
        """
        A função `test_retornaIdUsuario` testa a função `retornaIdUsuario` comparando sua saída
        com uma saída esperada.
        """
        expected_output = 3
        input_username = "Professor3"

        result = funcoes.retornaIdUsuario(input_username)

        self.assertEqual(result, expected_output)

    def test_retornaIdGrupo(self):
        """
        A função `test_retornaIdGrupo` testa a função `retornaIdGrupo` comparando sua saída com
        uma saída esperada.
        """
        expected_output = 2
        input_user_id = 3

        result = funcoes.retornaIdGrupo(input_user_id)

        self.assertEqual(result, expected_output)

    def test_retorna_menu(self):
        """
        A função `test_retorna_menu` testa a função `retorna_menu` comparando sua saída com uma
        saída esperada.
        """
        expected_output = funcoes.menuStaff
        input_group_id = 3

        result = funcoes.retorna_menu(input_group_id)

        self.assertEqual(result, expected_output)

    def test_retornaPermissao(self):
        """
        A função `test_retornaPermissao` testa a função `retornaPermissao` comparando seu resultado
        com uma saída esperada.
        """
        expected_output = True
        input_user_id = 1
        input_user_resource = 1

        result = funcoes.retornaPermissao(input_user_id, input_user_resource)

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
