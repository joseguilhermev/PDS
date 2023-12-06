# O código está importando a classe `Figlet` do módulo `pyfiglet` e do módulo `time`.
from pyfiglet import Figlet
import time

# Importando as funções do arquivo funcoes.py que criamos a conexão e operações no banco de dados e também contém as funcionalidades em si
import funcoes
import bd

# O código está usando o módulo `pyfiglet` para criar um texto estilizado em ASCII que diz "ACL Linux PDS"
# Em seguida, ele imprime esse texto cercado por uma linha de traços.
# Se houver um erro durante a renderização da arte ASCII, ele imprimirá "Programa de ACL Linux PDS".
try:
    print("---------------------------------------------------------------------------")
    f = Figlet(font="slant")
    print(f.renderText("Gestao de acessos PDS"), end="")
    print("---------------------------------------------------------------------------")
except:
    print("Programa de ACL Linux PDS")

# O bloco de código está implementando uma funcionalidade de login.
while True:
    Usuario = input("Digite o nome de usuário: ")
    Senha = input("Digite a senha: ")
    retorno = funcoes.autenticacao(Usuario, Senha)
    if retorno:
        print()
        print("Logando ...")
        break
    else:
        print("Erro na requisição")
        print()
        continue

# O código está chamando as funções `retornaIdUsuario` e `retornaIdGrupo` do módulo `funcoes`.
IdUsuario = funcoes.retornaIdUsuario(Usuario)
IdGrupo = funcoes.retornaIdGrupo(IdUsuario)

# O bloco de código que você forneceu está implementando um sistema de menu em um loop while. Aqui está um detalhamento de
# O que ele faz:
# Imprime o menu do grupo do usuário.
# Aguarda que o usuário digite uma opção.
# Verifica se o usuário digitou 0. Em caso afirmativo, ele sai do loop.
# Verifica se o grupo do usuário tem permissão para acessar o recurso correspondente à opção que ele digitado.
# Em caso afirmativo, ele chama a função apropriada do módulo `bd`.
# Se o grupo do usuário não tiver permissão para acessar o recurso correspondente à opção
# Se o grupo do usuário não tiver permissão para acessar o recurso correspondente à opção inserida, ele imprime uma mensagem de erro e continua o loop.
while True:
    time.sleep(2)
    try:
        print(funcoes.retorna_menu(IdGrupo))
        opcao = int(input())
        if opcao == 0:
            break

        dict_Grupo = {1: "Aluno", 2: "Professor", 3: "Staff"}
        dict_menuAluno_IdRecurso = {1: 1, 2: 2}
        dict_menuProfessor_IdRecurso = {1: 3, 2: 4, 3: 5, 4: 6, 5: 10}
        dict_menuStaff_IdRecurso = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 10, 8: 9}

        classe = dict_Grupo[IdGrupo]
        # De acordo com a escolha em cada menu é definido o recurso solicitado
        if classe == "Aluno":
            recurso = dict_menuAluno_IdRecurso[opcao]
        elif classe == "Professor":
            recurso = dict_menuProfessor_IdRecurso[opcao]
        elif classe == "Staff":
            recurso = dict_menuStaff_IdRecurso[opcao]

        # Verifica se a permissão para o recurso solicitado tá ativa
        if funcoes.retornaPermissao(IdGrupo, recurso):
            if classe == "Aluno":
                objeto = bd.Aluno(recurso, IdUsuario, IdGrupo)
                objeto.operacao()
            elif classe == "Professor":
                objeto = bd.Professor(recurso, IdUsuario, IdGrupo)
                objeto.operacao()
            elif classe == "Staff":
                objeto = bd.Staff(recurso, IdUsuario, IdGrupo)
                objeto.operacao()
        else:
            print("Erro de permissão")
            continue
    except EOFError:
        print("Ocorreu um erro na sua solicitação")
