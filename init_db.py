import sqlite3,sys
connection = sqlite3.connect("login.db")
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS login(un,pwd)")
with open("pepper.txt","a")as f:
	f.write(sys.argv[1])
