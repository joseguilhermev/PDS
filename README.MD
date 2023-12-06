# README - Banco de Dados da Aplicação Escolar

## Descrição

Este banco de dados foi desenvolvido para suportar um sistema de gestão escolar. Ele armazena informações sobre alunos, professores, disciplinas, notas, frequências, e outros dados relacionados ao ambiente acadêmico.

## Estrutura do Banco de Dados

### Tabelas Principais

1. **Usuario**

   - Armazena informações sobre usuários, como alunos, professores e staffs.
   - Colunas: id (chave primária), nome, senha.

2. **Grupo**

   - Contém informações sobre os grupos a que os usuários pertencem (ex: Aluno, Professor, Staff).
   - Colunas: id (chave primária), nome.

3. **User_Grupo**

   - Relaciona usuários aos grupos a que pertencem.
   - Colunas: id (chave primária), id_usuario (chave estrangeira), id_grupo (chave estrangeira).

4. **Disciplinas**

   - Armazena informações sobre as disciplinas oferecidas.
   - Colunas: id (chave primária), nome.

5. **Alunos_Disciplina**

   - Relaciona alunos às disciplinas em que estão matriculados.
   - Colunas: id (chave primária), id_usuario (chave estrangeira), id_disciplina (chave estrangeira).

6. **Frequencias**

   - Registra a presença dos alunos em determinadas datas.
   - Colunas: id (chave primária), data, presenca, id_aluno_disciplina (chave estrangeira).

7. **Recursos**

   - Mantém uma lista de recursos disponíveis no sistema.
   - Colunas: id (chave primária), nome.

8. **Acl**
   - Controla as permissões de acesso aos recursos para cada grupo.
   - Colunas: id (chave primária), id_grupo (chave estrangeira), id_recurso (chave estrangeira), permissao (boolean).

### Funcionalidades (Recursos)

1. **Ver notas**: Permite visualizar as notas dos alunos.
2. **Ver frequências**: Permite visualizar as frequências dos alunos.
3. **Ver todas notas**: Permite visualizar as notas de todos os alunos.
4. **Ver todas frequências**: Permite visualizar as frequências de todos os alunos.
5. **Alterar notas dos alunos**: Permite realizar alterações nas notas dos alunos.
6. **Alterar frequências**: Permite realizar alterações nas frequências dos alunos.
7. **Remover alunos da disciplina**: Permite remover alunos de uma disciplina.
8. **Adicionar alunos à disciplina**: Permite adicionar alunos a uma disciplina.
9. **Editar permissões**: Permite editar as permissões de acesso aos recursos.
10. **Ver lista de alunos por disciplina**: Permite visualizar a lista de alunos por disciplina.

### Script para popular o banco de dados

-- Drop existing tables
DROP TABLE IF EXISTS Acl, Alunos_Disciplina, Disciplinas, Frequencias, Grupo, Notas, Recursos, Usuario, User_Grupo;

-- Create tables
CREATE TABLE Usuario (
id SERIAL PRIMARY KEY,
nome VARCHAR(255),
senha VARCHAR(255)
);

CREATE TABLE Grupo (
id SERIAL PRIMARY KEY,
nome VARCHAR(255)
);

CREATE TABLE User_Grupo (
id SERIAL PRIMARY KEY,
id_usuario INT REFERENCES Usuario(id),
id_grupo INT REFERENCES Grupo(id)
);

CREATE TABLE Disciplinas (
id SERIAL PRIMARY KEY,
nome VARCHAR(255)
);

CREATE TABLE Alunos_Disciplina (
id SERIAL PRIMARY KEY,
id_usuario INT REFERENCES Usuario(id),
id_disciplina INT REFERENCES Disciplinas(id)
);

CREATE TABLE Frequencias (
id SERIAL PRIMARY KEY,
data DATE,
presenca BOOLEAN,
id_aluno_disciplina INT REFERENCES Alunos_Disciplina(id)
);

CREATE TABLE Recursos (
id SERIAL PRIMARY KEY,
nome VARCHAR(255)
);

CREATE TABLE Acl (
id SERIAL PRIMARY KEY,
id_grupo INT REFERENCES Grupo(id),
id_recurso INT REFERENCES Recursos(id),
permissao BOOLEAN
);

CREATE TABLE Notas (
id SERIAL PRIMARY KEY,
nota DECIMAL(5, 2),
id_aluno_disciplina INT REFERENCES Alunos_Disciplina(id)
);

-- Insert sample data
INSERT INTO Usuario (nome, senha) VALUES ('Aluno1', 'senha1');
INSERT INTO Usuario (nome, senha) VALUES ('Aluno2', 'senha2');
INSERT INTO Usuario (nome, senha) VALUES ('Professor3', 'senha3');
INSERT INTO Usuario (nome, senha) VALUES ('Staff4', 'senha4');
INSERT INTO Grupo (nome) VALUES ('Aluno');
INSERT INTO Grupo (nome) VALUES ('Professor');
INSERT INTO Grupo (nome) VALUES ('Staff');
INSERT INTO User_Grupo (id_usuario, id_grupo) VALUES (1, 1);
INSERT INTO User_Grupo (id_usuario, id_grupo) VALUES (2, 1);
INSERT INTO User_Grupo (id_usuario, id_grupo) VALUES (3, 2);
INSERT INTO User_Grupo (id_usuario, id_grupo) VALUES (4, 3);
INSERT INTO Disciplinas (nome) VALUES ('Matemática');
INSERT INTO Disciplinas (nome) VALUES ('História');
INSERT INTO Alunos_Disciplina (id_usuario, id_disciplina) VALUES (1, 1);
INSERT INTO Alunos_Disciplina (id_usuario, id_disciplina) VALUES (1, 2);
INSERT INTO Alunos_Disciplina (id_usuario, id_disciplina) VALUES (2, 1);
INSERT INTO Frequencias (data, presenca, id_aluno_disciplina) VALUES ('2023-01-01', TRUE, 1);
INSERT INTO Frequencias (data, presenca, id_aluno_disciplina) VALUES ('2023-01-01', FALSE, 2);
INSERT INTO Frequencias (data, presenca, id_aluno_disciplina) VALUES ('2023-01-01', TRUE, 3);
INSERT INTO Recursos (nome) VALUES ('Ver notas');
INSERT INTO Recursos (nome) VALUES ('Ver frequências');
INSERT INTO Recursos (nome) VALUES ('Ver todas notas');
INSERT INTO Recursos (nome) VALUES ('Ver todas frequências');
INSERT INTO Recursos (nome) VALUES ('Alterar notas dos alunos');
INSERT INTO Recursos (nome) VALUES ('Alterar frequências');
INSERT INTO Recursos (nome) VALUES ('Remover alunos da disciplina');
INSERT INTO Recursos (nome) VALUES ('Adicionar alunos à disciplina');
INSERT INTO Recursos (nome) VALUES ('Editar permissões');
INSERT INTO Recursos (nome) VALUES ('Ver lista de alunos por disciplina');
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (1, 1, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (1, 2, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (2, 3, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (2, 4, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (2, 5, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (2, 6, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (2, 10, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 3, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 4, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 5, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 6, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 7, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 8, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 9, TRUE);
INSERT INTO Acl (id_grupo, id_recurso, permissao) VALUES (3, 10, TRUE);

INSERT INTO Notas (nota, id_aluno_disciplina) VALUES (8.5, 1);
INSERT INTO Notas (nota, id_aluno_disciplina) VALUES (7.0, 2);
INSERT INTO Notas (nota, id_aluno_disciplina) VALUES (7.5, 3);

-- Reset sequence IDs
SELECT setval('usuario_id_seq', (SELECT MAX(id) FROM usuario));
SELECT setval('grupo_id_seq', (SELECT MAX(id) FROM grupo));
SELECT setval('user_grupo_id_seq', (SELECT MAX(id) FROM user_grupo));
SELECT setval('disciplinas_id_seq', (SELECT MAX(id) FROM disciplinas));
SELECT setval('alunos_disciplina_id_seq', (SELECT MAX(id) FROM alunos_disciplina));
SELECT setval('frequencias_id_seq', (SELECT MAX(id) FROM frequencias));
SELECT setval('recursos_id_seq', (SELECT MAX(id) FROM recursos));
SELECT setval('acl_id_seq', (SELECT MAX(id) FROM acl));
SELECT setval('notas_id_seq', (SELECT MAX(id) FROM notas));
