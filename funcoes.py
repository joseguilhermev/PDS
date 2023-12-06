# A linha `import psycopg2` está importando o módulo `psycopg2`, que é um adaptador PostgreSQL para Python.
# Ele permite que programas Python se conectem e interajam com bancos de dados PostgreSQL.
import psycopg2


def autenticacao(usuario, senha):
    """
    A função `autenticacao` verifica se uma determinada combinação de nome de usuário e senha existe em uma tabela de banco de dados
    chamada "Usuario" e retorna True se existir, e False caso contrário.

    @param usuario O parâmetro "usuario" é o nome de usuário do usuário que está tentando se autenticar.
    @param senha O parâmetro "senha" é a senha que está sendo passada para a função. Ele é usado
    Ela é usada para autenticar o usuário, verificando se a senha fornecida corresponde à senha armazenada no
    banco de dados para o nome de usuário fornecido.

    @return um valor booleano. Retorna True se o nome de usuário e a senha fornecidos corresponderem a um registro na tabela
    tabela "Usuario" e False caso contrário.
    """
    conn = conexao()
    if conn == None:
        return
    cur = conn.cursor()
    cur.execute(
        f"""SELECT COUNT(*) AS count FROM Usuario 
                WHERE nome = '{usuario}' AND senha = '{senha}';
                """
    )
    rows = cur.fetchall()
    for data in rows:
        if data[0] > 0:
            return True
        else:
            return False
    conn.close()


def retornaIdUsuario(nome_usuario):
    """
    A função `retornaIdUsuario` recupera o ID de um usuário com base em seu nome de usuário de um banco de dados.

    @param nome_usuario O parâmetro "nome_usuario" é o nome do usuário para o qual você deseja recuperar o ID.
    recuperar o ID.

    @return o ID do usuário com o nome de usuário fornecido.
    """
    conn = conexao()
    if conn == None:
        return
    cur = conn.cursor()
    cur.execute(
        f"""SELECT id FROM Usuario 
                WHERE nome = '{nome_usuario}';"""
    )
    rows = cur.fetchall()
    for data in rows:
        return data[0]
    conn.close()


def retornaIdGrupo(id_usuario):
    """
    A função `retornaIdGrupo` recupera de um banco de dados o ID do grupo associado a um determinado ID de usuário.
    banco de dados.

    @param id_usuario O parâmetro `id_usuario` é o ID do usuário para o qual você deseja recuperar o
    ID do grupo.

    @return o ID do grupo ao qual o usuário pertence.
    """
    conn = conexao()
    if conn == None:
        return
    cur = conn.cursor()
    cur.execute(
        f"""SELECT User_Grupo.id_grupo FROM User_Grupo 
                JOIN Grupo ON User_Grupo.id_grupo = Grupo.id 
                WHERE User_Grupo.id_usuario = '{id_usuario}';"""
    )
    rows = cur.fetchall()
    for data in rows:
        return data[0]
    conn.close()


def retorna_menu(id_grupo):
    """
    A função "retorna_menu" retorna o menu associado a um determinado ID de grupo.

    @param id_grupo O parâmetro "id_grupo" é o identificador de um grupo. Ele é usado para recuperar o menu
    menu correspondente para esse grupo.

    @return o valor associado à chave "id_grupo" no dicionário "dict_menu".
    """
    return dict_menu[id_grupo]


def retornaPermissao(id_grupo, id_recurso):
    """
    A função `retornaPermissao` verifica se um determinado grupo tem permissão para acessar um recurso específico.
    recurso específico.

    @param id_grupo O parâmetro "id_grupo" representa a ID de um grupo, que é usada para identificar um grupo específico no sistema.
    grupo específico no sistema.
    @param id_recurso O parâmetro `id_recurso` representa a ID de um recurso. Ele é usado na consulta SQL
    para verificar se existe uma permissão para um recurso específico.

    @return o resultado da consulta SQL, que é um valor booleano que indica se há uma permissão para o ID do grupo e o recurso fornecidos.
    permissão para o ID do grupo e o ID do recurso fornecidos.
    """
    conn = conexao()
    if conn == None:
        return
    cur = conn.cursor()
    cur.execute(
        f"""SELECT EXISTS (SELECT 1 FROM Acl
    WHERE id_grupo = '{id_grupo}' AND id_recurso = '{id_recurso}'
    AND permissao = TRUE) AS tem_permissao;"""
    )

    rows = cur.fetchall()
    for data in rows:
        return data[0]
    conn.close()


def conexao():
    """
    A função `conexao` estabelece uma conexão com um banco de dados PostgreSQL usando as credenciais
    credenciais fornecidas.

    @return A função `conexao()` retorna um objeto de conexão se a conexão com o banco de dados for
    bem-sucedida. Se houver um erro na conexão com o banco de dados, ela imprime uma mensagem de erro e retorna
    nada.
    """
    try:
        conn = psycopg2.connect(
            database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
        )
        return conn
    except:
        print("Erro ao se conectar com o banco de dados")
        return


# O código está definindo três variáveis: `menuAluno`, `menuProfessor` e `menuStaff`, que são
# cadeias de caracteres de várias linhas que representam menus para diferentes grupos de usuários.
menuAluno = f"""
1- Ver nota
2- Ver frequência
0- Sair
"""

menuProfessor = f"""
1- Ver notas
2- Ver frequências
3- Alterar notas
4- Alterar frequência
5- Ver lista de alunos por disciplina
0- Sair
"""
menuStaff = f"""
1- Ver notas
2- Ver frequência
3- Alterar notas
4- Alterar frequência
5- Remover alunos da disciplina
6- Adicionar alunos a disciplina
7- Ver lista de alunos por disciplina
8- Alterar permissoes
0- Sair
"""

# Pra cada id de um grupo tem o menu desse grupo
dict_menu = {1: menuAluno, 2: menuProfessor, 3: menuStaff}

# O código está definindo as variáveis `DB_NAME`, `DB_USER`, `DB_PASS`, `DB_HOST` e `DB_PORT` que são
# usadas para armazenar as credenciais necessárias para estabelecer uma conexão com um banco de dados PostgreSQL. Essas
# credenciais incluem o nome do banco de dados (`DB_NAME`), o nome de usuário (`DB_USER`), a senha
# senha (`DB_PASS`), o endereço do host (`DB_HOST`) e o número da porta (`DB_PORT`). Essas variáveis são
# posteriormente usadas na função `conexao()` para estabelecer uma conexão com o banco de dados.
DB_NAME = "yvxvamiu"
DB_USER = "yvxvamiu"
DB_PASS = "lPxAVBoQCg5VIBkWn284OHjDvJb5qTHE"
DB_HOST = "isabelle.db.elephantsql.com"
DB_PORT = "5432"
