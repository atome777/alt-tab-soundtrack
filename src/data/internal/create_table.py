import sqlite3

connection = sqlite3.connect("internal.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE "redux" (
	"uuid"	TEXT NOT NULL UNIQUE,
	"cpf_representante"	TEXT NOT NULL,
	"af_codigo"	INTEGER,
	PRIMARY KEY('cpf_representante',"uuid")
)""")
