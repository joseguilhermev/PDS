import psycopg2
import funcoes
import time


class Aluno:
    def __init__(self, recurso, id_usuario, id_grupo):
        self.recurso = recurso
        self.IdUsuario = id_usuario
        self.IdGrupo = id_grupo

    # Verifico qual funcão irá ser executada
    def operacao(self):
        if self.recurso == 1:
            self.ver_notas()
        elif self.recurso == 2:
            self.ver_frequencias()
        else:
            print("Erro no programa")

    def ver_notas(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Disciplinas.nome, Notas.nota
                    FROM Disciplinas
                    JOIN Alunos_Disciplina ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                    LEFT JOIN Notas ON Alunos_Disciplina.id = Notas.id_aluno_disciplina
                    WHERE Alunos_Disciplina.id_usuario = '{self.IdUsuario}';"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(f"Disciplina: {data[0]} | Nota: {data[1]}")
        conn.close()

    def ver_frequencias(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Disciplinas.nome, Frequencias.data, Frequencias.presenca
                    FROM Frequencias
                    JOIN Alunos_Disciplina ON Frequencias.id_aluno_disciplina = Alunos_Disciplina.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                    LEFT JOIN Notas ON Alunos_Disciplina.id = Notas.id_aluno_disciplina
                    WHERE Alunos_Disciplina.id_usuario = '{self.IdUsuario}';"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(f"Disciplina: {data[0]} | Data: {data[1]} | Presença: {data[2]}")
        conn.close()


class Professor:
    def __init__(self, recurso, id_usuario, id_grupo):
        self.recurso = recurso
        self.IdUsuario = id_usuario
        self.IdGrupo = id_grupo

    # Verifico qual funcão irá ser executada
    def operacao(self):
        if self.recurso == 3:
            self.ver_notas()
        elif self.recurso == 4:
            self.ver_frequencias()
        elif self.recurso == 5:
            self.alterar_notas()
        elif self.recurso == 6:
            self.alterar_frequencias()
        elif self.recurso == 10:
            self.ver_alunos_porDisciplina()
        else:
            print("Erro no programa")

    def ver_notas(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Usuario.nome ,Disciplinas.nome, Notas.nota
                    FROM Notas
                    JOIN Alunos_Disciplina ON Notas.id_aluno_disciplina = Alunos_Disciplina.id
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id;"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(f"Usuário: {data[0]} | Disciplina: {data[1]} | Nota: {data[2]}")
        conn.close()

    def alterar_notas(self):
        disciplina, aluno, novaNota = input(
            "Digite: disciplina , nome do aluno e a nova nota"
        ).split()
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""UPDATE Notas
                    SET nota = '{novaNota}'
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                        JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                        WHERE Usuario.nome = '{aluno}' AND Disciplinas.nome = '{disciplina}');"""
        )
        conn.commit()

    def ver_frequencias(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Usuario.nome, Disciplinas.nome, Frequencias.data, Frequencias.presenca
                    FROM Frequencias
                    JOIN Alunos_Disciplina ON Frequencias.id_aluno_disciplina = Alunos_Disciplina.id
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id;"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(
                f"Aluno: {data[0]} | Disciplina: {data[1]} | Data: {data[2]} | Presença: {data[3]}"
            )
        conn.close()

    def alterar_frequencias(self):
        disciplina, aluno, data = input(
            "Digite: disciplina , nome do aluno, data"
        ).split()
        presenca = input(f"O aluno esteve presente em {data}? Digite Sim ou Não")

        if presenca == "Sim":
            presenca = True
        elif presenca == "Não":
            presenca = False
        else:
            return

        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""UPDATE Frequencias
                    SET presenca = '{presenca}'
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                        JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                        WHERE Usuario.nome = '{aluno}' AND Disciplinas.nome = '{disciplina}'
                        )
                    AND data = '{data}';"""
        )
        conn.commit()

    def ver_alunos_porDisciplina(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""
                    SELECT 
                    Disciplinas.nome AS disciplina,
                    Usuario.nome AS aluno
                    FROM Alunos_Disciplina
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                    ORDER BY Disciplinas.nome, Usuario.nome;"""
        )


class Staff:
    def __init__(self, recurso, id_usuario, id_grupo):
        self.recurso = recurso
        self.IdUsuario = id_usuario
        self.IdGrupo = id_grupo

    # Verifico qual funcão irá ser executada
    def operacao(self):
        if self.recurso == 3:
            self.ver_notas()
        elif self.recurso == 4:
            self.ver_frequencias()
        elif self.recurso == 5:
            self.alterar_notas()
        elif self.recurso == 6:
            self.alterar_frequencias()
        elif self.recurso == 7:
            self.remover_alunos_disciplina()
        elif self.recurso == 8:
            self.adicionar_alunos_disciplina()
        elif self.recurso == 10:
            self.ver_alunos_porDisciplina()
        elif self.recurso == 9:
            self.editar_permissoes()
        else:
            print("Erro no programa")

    def ver_notas(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Usuario.nome ,Disciplinas.nome, Notas.nota
                    FROM Notas
                    JOIN Alunos_Disciplina ON Notas.id_aluno_disciplina = Alunos_Disciplina.id
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id;"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(f"Usuário: {data[0]} | Disciplina: {data[1]} | Nota: {data[2]}")
        conn.close()

    def alterar_notas(self):
        disciplina, aluno, novaNota = input(
            "Digite: disciplina , nome do aluno e a nova nota"
        ).split()
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""UPDATE Notas
                    SET nota = '{novaNota}'
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                        JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                        WHERE Usuario.nome = '{aluno}' AND Disciplinas.nome = '{disciplina}');"""
        )
        conn.commit()

    def ver_frequencias(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""SELECT Usuario.nome, Disciplinas.nome, Frequencias.data, Frequencias.presenca
                    FROM Frequencias
                    JOIN Alunos_Disciplina ON Frequencias.id_aluno_disciplina = Alunos_Disciplina.id
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id;"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(
                f"Aluno: {data[0]} | Disciplina: {data[1]} | Data: {data[2]} | Presença: {data[3]}"
            )
        conn.close()

    def alterar_frequencias(self):
        disciplina, aluno, data = input(
            "Digite: disciplina , nome do aluno, data"
        ).split()
        presenca = input(f"O aluno esteve presente em {data}? Digite Sim ou Não")

        if presenca == "Sim":
            presenca = True
        elif presenca == "Não":
            presenca = False
        else:
            return

        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""UPDATE Frequencias
                    SET presenca = '{presenca}'
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                        JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                        WHERE Usuario.nome = '{aluno}' AND Disciplinas.nome = '{disciplina}'
                        )
                    AND data = '{data}';"""
        )
        conn.commit()

    def remover_alunos_disciplina(self):
        disciplina, aluno = input("Digite: disciplina e o nome do aluno").split()
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""DO $$ 
                    DECLARE 
                    idAluno INT;
                    BEGIN
                    SELECT id INTO idAluno FROM Usuario WHERE nome = '{aluno}'; -- Substitua pelo valor real desejado
                    DELETE FROM Notas
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        WHERE id_usuario = idAluno);
                    DELETE FROM Frequencias
                    WHERE id_aluno_disciplina IN (
                        SELECT Alunos_Disciplina.id
                        FROM Alunos_Disciplina
                        WHERE id_usuario = idAluno);
                    DELETE FROM Alunos_Disciplina
                    WHERE id_usuario = idAluno
                    AND id_disciplina = (SELECT id FROM Disciplinas WHERE nome = '{disciplina}'); -- Substitua pelo valor real desejado
                    END $$;"""
        )
        conn.commit()

    def adicionar_alunos_disciplina(self):
        disciplina, aluno = input("Digite: disciplina e o nome do aluno").split()
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""
                    DO $$ 
                    DECLARE 
                    nomeAluno VARCHAR(100) := '{aluno}'; -- Substitua pelo valor real desejado
                    nomeDisciplina VARCHAR(100) := '{disciplina}'; -- Substitua pelo valor real desejado
                    idAluno INT;
                    idDisciplina INT;
                    BEGIN
                    SELECT id INTO idAluno FROM Usuario WHERE nome = nomeAluno;
                    SELECT id INTO idDisciplina FROM Disciplinas WHERE nome = nomeDisciplina;
                    IF NOT EXISTS (SELECT 1 FROM Alunos_Disciplina WHERE id_usuario = idAluno AND id_disciplina = idDisciplina) THEN
                    INSERT INTO Alunos_Disciplina (id_usuario, id_disciplina)
                    VALUES (idAluno, idDisciplina);
                    RAISE NOTICE 'Aluno adicionado com sucesso à disciplina.';
                    ELSE
                    RAISE NOTICE 'O aluno já está na disciplina.';
                    END IF;
                    END $$;"""
        )
        conn.commit()

    def editar_permissoes(self):
        grupo, recurso = input("Qual grupo e id do recurso deseja alterar?").split()
        permissao = int(
            input(
                "Deseja alterar para qual permissão? Digite '1' p/permitir e '0' p/não permitir"
            )
        )
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""
                    DECLARE @idGrupo INT = {self.IdGrupo};
                    DECLARE @idRecurso INT = {recurso};
                    DECLARE @novaPermissao BIT = {permissao};
                    UPDATE Acl
                    SET permissao = @novaPermissao
                    WHERE id_grupo = @idGrupo AND id_recurso = @idRecurso; """
        )
        conn.commit()

        print()

    def ver_alunos_porDisciplina(self):
        conn = funcoes.conexao()
        if conn == None:
            return
        cur = conn.cursor()
        cur.execute(
            f"""
                    SELECT 
                    Disciplinas.nome AS disciplina,
                    Usuario.nome AS aluno
                    FROM Alunos_Disciplina
                    JOIN Usuario ON Alunos_Disciplina.id_usuario = Usuario.id
                    JOIN Disciplinas ON Alunos_Disciplina.id_disciplina = Disciplinas.id
                    ORDER BY Disciplinas.nome, Usuario.nome;"""
        )
        rows = cur.fetchall()
        for data in rows:
            print(data)
        conn.close()
