import hashlib,random
def hash(str,hashlen=16):
	salt = random.randint(1,(2**hashlen))
	hash = hashlib.md5(str.encode("ascii")+bytes(salt)).hexdigest()
	
	return f"{salt}${hash}"

