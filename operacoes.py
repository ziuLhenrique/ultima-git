import sqlite3
conexao =  sqlite3.connect('fifa_1')
cursor = conexao.cursor()

cpf = input('Digite seu cpf:')


sql = '''
SELECT id, cpf, nome, saldo FROM conta WHERE cpf = ?
'''
consulta = cursor.execute(sql, [cpf])

conta  = None
for conta in consulta:
    break

if conta is None:
    print('conta inexistente!')
    exit()

operacao = input('Qual a operação que deseja fazer? (s)aque or (d)eposito:')
valor = int(input('Digite o valor: '))

saldo = conta[3]
if operacao =='s':
    saldo = saldo - valor

elif operacao == 'd':
    saldo = saldo 
else:
    print('conta inexistente!')
    exit()

sql = '''
UPDATE conta SET saldo = ? WHERE cpf = ?
'''
cursor.execute(sql, [saldo, cpf])
conexao.commit()
cursor.close()