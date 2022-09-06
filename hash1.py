import hashlib
pepper = 0
with open("pepper.txt","r") as f:
	pepper = (f.read().replace("\n",""))
def hash(str):
	global pepper
	
	hash = hashlib.sha256(str.encode("ascii")+bytes(pepper.encode('ascii'))).hexdigest()
	
	return f"{hash}"

