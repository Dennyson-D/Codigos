import sqlite3

con = sqlite3.connect('clientes.db')
cur = con.cursor()

def inserir_muitos(conexao,cursor,dados):
    cur.executemany("INSERT INTO clientes(nome, email) VALUES(?,?)", dados)
    con.commit()

def consulta_todos(cursor):
    cur.execute('SELECT * FROM clientes')
    res = cur.fetchall()
    for row in res:
        print(row)

def consulta_um(cursor,id):
    cur.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cur.fetchone()

#exemplo com rowfactory
def consulta_row(cursor,id):
    cur.row_factory = sqlite3.Row # retorna como dict
    cur.execute('SELECT * FROM clientes')
    return cur.fetchone()
    

dados = [
        (' Ana ',' ana@example.com '),
        (' Carlos ',' carlos@email.com '),
        (' Fernanda ',' fernanda@example.com '),
        (' João ',' joao@email.com '),
        (' Mariana ',' mariana@example.com '),
        (' Rafael ',' rafael@email.com '),
        (' Juliana ',' juliana@example.com '),
        (' Lucas ',' lucas@email.com '),
        (' Beatriz ',' beatriz@example.com '),
        (' Thiago ',' thiago@email.com '),

]    

#inserir_muitos(con,cur,dados)

# consulta_todos(cur)
# print(consulta_um(cur,2))

res = consulta_row(cur,1)
print(dict(res))