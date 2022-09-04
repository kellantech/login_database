import sqlite3,sys,random,string
connection = sqlite3.connect("login.db")
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS login(un,pwd)")
with open("pepper.txt","a")as f:
	try: 
		f.write(sys.argv[1])
	except IndexError:
		char = string.ascii_letters + string.digits + string.punctuation
		f.write(''.join(random.choice(char) for i in range(10)) )

