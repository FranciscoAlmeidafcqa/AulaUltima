import sqlite3
conexao =sqlite3.connect('db')
cursor=conexao.cursor()
sql ='create table pedido(id int not null,cliente varchar(100),data varchar(20),   primary key (id) )'
cursor.execute(sql)
conexao.commit()
conexao.close()