import sqlite3

con = sqlite3.connect("clientes.db")

cur = con.cursor()

def criar_tabela(cursor,conexao):
    cur.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,nome  VARCHAR(100),email VARCHAR(50))")

def inserir(cursor,conexao,nome,email):
    dados = nome,email
    cur.execute("insert into clientes(nome,email) values(?,?) ", (dados))  #fazer dessa forma "values(?,?) ", (dados)", para evitar códigos injections

    print(cur.execute('Select * from clientes'))

    con.commit()


def updte(cursor,conexao,nome,email,id):
    dados = (nome,email,id)
    cur.execute("UPDATE CLIENTES SET nome = ?, email = ? WHERE id = ?", dados)
    con.commit()

def deletar(cursor,conexao,id):
    dados = (id,) # OBS,  tupla de único valor precisa ter uma virgula no final para nãod ar erro
    cur.execute("DELETE FROM CLIENTES WHERE ID = ?", dados)    
    con.commit()


# inserir(cur,con,'Alicate','ali@dd.com')
# updte(cur,con,'ibra','ibra@gg.com',1)
deletar(cur,con,3)