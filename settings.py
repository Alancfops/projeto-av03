import sqlite3
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

#TABELA USUARIO
sql_user = '''CREATE TABLE IF NOT EXISTS usuario(
  idUser INTEGER PRIMARY KEY AUTOINCREMENT,
  username varchar(255),
  password varchar(255)
)'''


#TABELA ANOTACAO
sql_anot = '''CREATE TABLE IF NOT EXISTS anotacao (
  idAnotacao INTEGER PRIMARY KEY AUTOINCREMENT,
  conteudo varchar(900),
  idUser references usuario(idUser)
)'''

cursor.execute(sql_user)
cursor.execute(sql_anot)
