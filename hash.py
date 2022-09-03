import hashlib
pepper = 0
with open("pepper.txt","r") as f:
	pepper = int(f.read().replace("\n",""))
def hash(str):
	global pepper
	
	hash = hashlib.sha256(str.encode("ascii")+bytes(pepper)).hexdigest()
	
	return f"{hash}"

