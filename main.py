import sqlite3,hash1
def does_user_exist(uname):
	connection = sqlite3.connect("login.db")

	c = connection.cursor()
	ul = c.execute(f"SELECT * FROM login WHERE un='{uname}'").fetchall()
	if len(ul) == 0: return 0
	else: return 1
		
def add_user(uname,pwd):
	connection = sqlite3.connect("login.db")
	c = connection.cursor()
	if does_user_exist(uname)==0:
		qu = f"INSERT INTO login(un,pwd) values ('{escape(uname)}','{(hash1.hash(escape(pwd)+escape(uname)))}')"
		c.execute(qu)
	connection.commit()

def escape(tx):
	return tx.replace("\'","").replace("\"",'').replace("-","").replace("<",'')
	
def check(uname,pwd):
	connection = sqlite3.connect("login.db")
	c = connection.cursor()
	query = f"""SELECT *
  FROM login
 WHERE un = '{escape(uname)}'
   AND pwd  = '{(hash1.hash(escape(pwd)+escape(uname)))}' LIMIT 1
"""
	lst = (c.execute(query).fetchall())
	if lst == []:return 0
	if lst != []:return 1

def print_db():
	connection = sqlite3.connect("login.db")
	c = connection.cursor()
	query = """SELECT *
  FROM login"""
	lst = (c.execute(query).fetchall())
	print(lst)

def del_user(uname, password):
	connection = sqlite3.connect("login.db")
	c = connection.cursor()
	isdel = 0
	if check(uname,password) == 1 : 
		c.execute(f"DELETE FROM login WHERE un='{uname}';");isdel=1
	connection.commit()
	if isdel==1: return 1
	else:return 0

def update_pwd(uname, old_pwd, new_pwd):
	connection = sqlite3.connect("login.db")
	c=connection.cursor()
	if check(uname,old_pwd) == 1:
		query =f"""
 UPDATE login
SET pwd = '{hash1.hash(escape(new_pwd)+escape(uname))}'
WHERE un='{uname}';
 """
		c.execute(query)
		connection.commit()
		return 1
	else: return 0	

def clear_db():
	connection = sqlite3.connect("login.db")
	c=connection.cursor()

	i = input('are you sure? ')
	i2 = input('are you REALLY sure? ')
	if i=='yes' and i2=='yes':
		c.execute("DELETE FROM login;")
	connection.commit()	

add_user('kellan','b')
add_user('k2','kk')
