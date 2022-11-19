import sqlite3
conexao = sqlite3.connect('fifa_1')
cursor = conexao.cursor()


sql = '''
CREATE TABLE conta(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cpf TEXT(11) NOT NULL,
    nome TEXT(50) NOT NULL,
    saldo NUMERIC
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()