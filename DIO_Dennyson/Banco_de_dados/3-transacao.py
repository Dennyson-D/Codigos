import sqlite3

con = sqlite3.connect('clientes.db')
cur = con.cursor()
cur.row_factory = sqlite3.Row


try:
    cur.execute("INSERT INTO clientes(nome, email) VALUES(?,?)", ('Dennyson','denny@dranzr.com'))
    cur.execute("INSERT INTO clientes(id,nome,email) VALUES(?,?,?)", (2,'teste','erro@gmail.com'))
    con.commit()    
except Exception as erro:    
    print(f'Erro {erro}')
    con.rollback

    














# try:
#     cur.execute('DELETE FROM clientes WHERE id >= 18')
#     con.commit()
# except Exception as er:
#     print(er)
#     con.rollback()    