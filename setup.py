import string,random,sqlite3
def write_pepper(str):
	with open("pepper.txt","a")as f:
		f.write(str)

print("welcome to the database setup wizard")
input("press enter to get started! ")
in1 = input("please enter a pepper, or press enter for a radndom one: ")
if in1 == "":
	in2 = input("what length pepper do you want? type length or press enter for 10 ")
	print("writing pepper...",end="")
	ln=10
	if in2 == "": pass
	else: ln=int(in2)
	char = string.ascii_letters + string.digits + string.punctuation
	write_pepper(''.join(random.choice(char) for i in range(ln)) )
else: 
	print("writing pepper...",end="")
	write_pepper(in1)
print("done")	

input("press enter to finish setup")
print('connecting to databse...',end='')
connection = sqlite3.connect("login.db")
c = connection.cursor()
print('done')
print('creating table...',end='')
c.execute("CREATE TABLE IF NOT EXISTS login(un,pwd,priv)")
print('done')
